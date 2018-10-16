#!/usr/bin/python
#
# @author: Gaurav Rastogi (grastogi@avinetworks.com)
#          Eric Anderson (eanderson@avinetworks.com)
# module_check: supported
#
# Copyright: (c) 2017 Gaurav Rastogi, <grastogi@avinetworks.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_update_gslb_dns_vses
author: Shrikant Chaudhari (shrikant.chaudhari@avinetworks.com)
short_description: Module to update gslb's dns_vses configurations.
requirements: [ avisdk ]
options:
    gslb_sites_config:
        description:
            - This is placeholder for sites field in the gslb object. 'dns_vses' field is updated using this.
              Here you can specify configuration for sites field of a gslb object. This field used to update 'dns_vses' 
              in gslb objects. The 'dns_vses' field identifies the DNS VS and the sub-domains it hosts. 
              For more details you can refer to swagger specs 'https://{controller_ip}/swagger/'. From the link, 
              you can find configurable fields under 'dns_vses' property of a gslb object.
extends_documentation_fragment:
    - avi
'''

EXAMPLES = '''
  - name: Configure gslb sites
      avi_update_gslb_dns_vses:
        api_version: 18.1.5
        username: "username"
        password: "password"
        controller: 10.10.28.83
        gslb_sites_config:
            - name: "test-site1"
              dns_vses: 
                - dns_vs_uuid: "virtualservice-f2a711cd-5e78-473f-8f47-d12de660fd62"
            - name: "test-site2"
              dns_vses: 
                - dns_vs_uuid: "virtualservice-c1a63a16-f2a1-4f41-aab4-1e90f92a5e49"
'''

RETURN = '''
obj:
    description: Avi REST resource
    returned: success, changed
    type: dict
'''


from ansible.module_utils.basic import AnsibleModule
try:
    from avi.sdk.avi_api import ApiSession, AviCredentials
    from avi.sdk.utils.ansible_utils import avi_common_argument_spec
    from pkg_resources import parse_version
    import avi.sdk
    sdk_version = getattr(avi.sdk, '__version__', None)
    if ((sdk_version is None) or
            (sdk_version and
             (parse_version(sdk_version) < parse_version('17.1')))):
        # It allows the __version__ to be '' as that value is used in development builds
        raise ImportError
    from avi.sdk.utils.ansible_utils import avi_ansible_api
    HAS_AVI = True
except ImportError:
    HAS_AVI = False


def main():
    argument_specs = dict(
        gslb_sites_config=dict(type='list', ),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    # Create controller session
    api_creds = AviCredentials()
    api_creds.update_from_ansible_module(module)
    api = ApiSession.get_session(
        api_creds.controller, api_creds.username, password=api_creds.password,
        timeout=api_creds.timeout, tenant=api_creds.tenant,
        tenant_uuid=api_creds.tenant_uuid, token=api_creds.token,
        port=api_creds.port)
    path = 'gslb'
    # Get existing gslb objects
    rsp = api.get(path, api_version=api_creds.api_version)
    existing_gslb = rsp.json()
    gslb_obj = existing_gslb['results'][0]
    sites = module.params['gslb_sites_config']
    for site_obj in gslb_obj['sites']:
        for obj in sites:
            config_for = obj.get('ip_addr', None)
            if not config_for:
                return module.fail_json(msg=(
                    "name of gslb site in a configuration is mandatory. Please provide name i.e. gslb site's name."))
            if config_for == site_obj['ip_addresses'][0]['addr']:
                # Modify existing gslb sites object
                for key, val in obj.iteritems():
                    site_obj[key] = val
    module.params.update(gslb_obj)
    module.params.update(
        {
            'avi_api_update_method': 'put',
            'state': 'present'
        }
    )
    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk>=17.1) is not installed. '
            'For more details visit https://github.com/avinetworks/sdk.'))
    return avi_ansible_api(module, 'gslb',
                           set([]))


if __name__ == '__main__':
    main()
