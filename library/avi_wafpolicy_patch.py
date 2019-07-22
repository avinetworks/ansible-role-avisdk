import json
import collections
from ansible.module_utils.basic import AnsibleModule
from copy import deepcopy

try:
    from avi.sdk.avi_api import ApiSession, AviCredentials
    from avi.sdk.utils.ansible_utils import (
        avi_obj_cmp, cleanup_absent_fields, avi_common_argument_spec,
        ansible_return)
    HAS_AVI = True
except ImportError:
    HAS_AVI = False


def update_patch(base_policy, patch):
    base_policy.pop('_last_modified')
    base_policy.pop('url')
    base_policy.pop('uuid')
    for k, v in base_policy.iteritems():
        if k in patch and not k == 'crs_groups':
            base_policy[k] = patch[k]
    if 'crs_groups' in patch:
        for p_group in patch['crs_groups']:
            base_group = [group for group in base_policy['crs_groups']
                          if group['name'] == p_group['name']]
            if not base_group:
                base_policy['crs_groups'].append(p_group)
                continue

            base_group = base_group[0]
            for p_rule in p_group['rules']:
                base_rule = [rule for rule in base_group['rules']
                              if rule['rule_id'] == p_rule['rule_id']]
                if base_rule:
                    base_rule[0].update(p_rule)
                else:
                    base_group['rules'].append(p_rule)


def main():
    argument_specs = dict(
        base_waf_policy_ref=dict(type='str', required=True),
        name=dict(type='str', required=True),
        patch_file=dict(type='str', required=True),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(argument_spec=argument_specs,
                           supports_check_mode=True)
    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk>=17.1) or requests is not installed. '
            'For more details visit https://github.com/avinetworks/sdk.'))
    api_creds = AviCredentials()
    api_creds.update_from_ansible_module(module)
    api = ApiSession.get_session(
        api_creds.controller, api_creds.username, password=api_creds.password,
        timeout=api_creds.timeout, tenant=api_creds.tenant,
        tenant_uuid=api_creds.tenant_uuid, token=api_creds.token,
        port=api_creds.port, api_version=api_creds.api_version)

    existing_obj = api.get_object_by_name(
        'wafpolicy', module.params.get('name'))
    is_obj_exist = True
    if not existing_obj:
        is_obj_exist = False
        existing_obj = api.get_object_by_name(
            'wafpolicy', module.params.get('base_waf_policy_ref'))


    with open(module.params.get('patch_file'), "r+") as f:
        waf_patch = json.loads(f.read())
        new_obj = deepcopy(existing_obj)
        update_patch(new_obj, waf_patch)

        for crs_group in new_obj['crs_groups']:
            crs_group['rules'] = [rule for rule in crs_group['rules']
                                  if rule.get('state', 'present') == 'present']

        changed = avi_obj_cmp(new_obj, existing_obj)

        if module.check_mode:
            ansible_return(
                module, new_obj, changed, existing_obj=existing_obj,
                api_context=api.get_context())

        rsp = None
        if is_obj_exist:
            data = {'model_name': 'WafPolicy', 'data': new_obj}
            rsp = api.post('macro', data=data)

        else:
            rsp = api.post('wafpolicy', data=new_obj)
            changed = True

        ansible_return(module, rsp, changed, req=new_obj)


if __name__ == '__main__':
    main()

