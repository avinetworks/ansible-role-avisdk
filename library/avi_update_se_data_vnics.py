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
module: avi_update_se_data_vnics
author: Shrikant Chaudhari (shrikant.chaudhari@avinetworks.com)

short_description: Module to update Service Engine's data vnics/vlans configurations.
requirements: [ avisdk ]
options:
    data_vnics_config:
        description:
            - Placeholder for description of property data_vnics of obj type ServiceEngine field.
              Here you can specify configuration for data_vnics property of a service engine.
              For more details you can refer to swagger specs https://{controller_ip}/swagger/
              From above link you can find configurable fields under data_vnics property of a service engine.
extends_documentation_fragment:
    - avi
'''

EXAMPLES = '''
  - name: Update data vnics and vlan interfaces
      avi_update_se_data_vnics:
        avi_credentials:
          controller: "10.10.28.102"
          username: "username"
          password: "password"
          api_version: 18.1.3
        data_vnics_config:
        - if_name: "eth1"
          is_asm: false
          can_se_dp_takeover: true
          is_hsm: false
          is_avi_internal_network: false
          enabled: true
          dhcp_enabled: false
          del_pending: false
          linux_name: "eth3"
          is_mgmt: false
          connected: true
          vlan_interfaces:
            - dhcp_enabled: true
              if_name: "eth3"
              ip6_autocfg_enabled: false
              is_mgmt: false
              vlan_id: 0
              vnic_networks:
                - ip:
                    ip_addr:
                      addr: "10.161.56.155"
                      type: "V4"
                    mask: 24
                  mode: "STATIC"
                  ctlr_alloc: false
              vrf_ref: "https://10.10.28.102/api/vrfcontext/vrfcontext-47f8a632-3ab4-427d-9084-433bc06da26d"
          vnic_networks:
            - ip:
                ip_addr:
                  addr: "10.161.56.154"
                  type: "V4"
                mask: 24
              mode: "STATIC"
              ctlr_alloc: false
          vrf_id: 0
          aggregator_chgd: false
          mtu: 1500
          vrf_ref: "https://10.10.28.102/api/vrfcontext/vrfcontext-47f8a632-3ab4-427d-9084-433bc06da26d"
          ip6_autocfg_enabled: false
          vlan_id: 0
          is_portchannel: false
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
        data_vnics_config=dict(type='list', ),
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
    path = 'serviceengine'
    # Get existing SE object
    rsp = api.get(path, api_version=api_creds.api_version)
    existing_se = rsp.json()
    se_obj = existing_se['results'][0]
    data_vnics_config = module.params['data_vnics_config']
    for d_vnic in se_obj['data_vnics']:
        for obj in data_vnics_config:
            config_for = obj.get('if_name', None)
            if not config_for:
                return module.fail_json(msg=(
                    "if_name in a configuration is mandatory. Please provide if_name i.e. vnic's interface name."))
            if config_for == d_vnic['if_name']:
                # modify existing SE object
                for key, val in obj.iteritems():
                    d_vnic[key] = val
            if config_for == d_vnic['if_name']:
                for key, val in obj.iteritems():
                    d_vnic[key] = val
    module.params.update(se_obj)
    module.params.update(
        {
            'avi_api_update_method': 'put',
            'state': 'present'
        }
    )
    module.params.pop('data_vnics_config')
    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk>=17.1) is not installed. '
            'For more details visit https://github.com/avinetworks/sdk.'))
    return avi_ansible_api(module, 'serviceengine',
                           set([]))


if __name__ == '__main__':
    main()
