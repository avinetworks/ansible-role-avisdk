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
    base_policy.pop('_last_modified', '')
    base_policy.pop('url', '')
    for k, v in base_policy.iteritems():
        if k in patch and not k == 'crs_groups':
            base_policy[k] = patch[k]
    if 'crs_groups' in patch:
        base_group_dict = dict()
        # Converting list to dict for quick patch iterations
        for group in base_policy['crs_groups']:
            base_group_dict[group['name']] = group
            rules = group.pop('rules')
            group['rules'] = {}
            for rule in rules:
                base_group_dict[group['name']]['rules'][rule['index']] = rule

        # Iterating over patch and updating base policy rules
        for p_group in patch['crs_groups']:
            base_group = base_group_dict.get(p_group['name'], None)
            if not base_group:
                base_group_dict[p_group['name']] = p_group
                continue
            for p_rule in p_group['rules']:
                base_rule = base_group['rules'].get(p_rule['index'])
                state = base_rule.pop('state', 'present')
                if not state == 'present':
                    base_group['rules'].pop(p_rule['index'])
                    continue
                if base_rule:
                    base_rule.update(p_rule)
                else:
                    base_group['rules'][p_rule['index']] = p_rule

        # Converting dict back to object structure
        for bg_name in base_group_dict:
            base_group_dict[bg_name]['rules'] = sorted(
                base_group_dict[bg_name]['rules'].values(),
                key=lambda i: i['index'])
        base_policy['crs_groups'] = sorted(
            base_group_dict.values(), key=lambda i: i['index'])


def main():
    if not HAS_AVI:
        AnsibleModule.fail_json(msg=('Avi python API SDK (avisdk>=17.1) or requests is not installed. '
            'For more details visit https://github.com/avinetworks/sdk.'))
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

    obj_uuid = None
    existing_obj = api.get_object_by_name(
        'wafpolicy', module.params.get('name'))
    if existing_obj:
        obj_uuid = existing_obj.pop('uuid', None)
    if not existing_obj:
        existing_obj = api.get_object_by_name(
            'wafpolicy', module.params.get('base_waf_policy_ref'))


    with open(module.params.get('patch_file'), "r+") as f:
        waf_patch = json.loads(f.read())
        new_obj = deepcopy(existing_obj)
        update_patch(new_obj, waf_patch)

        changed = avi_obj_cmp(new_obj, existing_obj)

        if module.check_mode:
            ansible_return(
                module, new_obj, changed, existing_obj=existing_obj,
                api_context=api.get_context())

        if obj_uuid:
            new_obj['uuid'] = obj_uuid
            rsp = api.put('wafpolicy/%s' % obj_uuid, data=new_obj)
            changed = True
        else:
            rsp = api.post('wafpolicy', data=new_obj)
            changed = True
        ansible_return(module, rsp, changed, req=new_obj)


if __name__ == '__main__':
    main()

