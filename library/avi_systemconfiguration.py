#!/usr/bin/python
#
# @author: Gaurav Rastogi (grastogi@avinetworks.com)
#          Eric Anderson (eanderson@avinetworks.com)
# module_check: supported
# Avi Version: 17.1.1
#
# Copyright: (c) 2017 Gaurav Rastogi, <grastogi@avinetworks.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_systemconfiguration
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>

short_description: Module for setup of SystemConfiguration Avi RESTful Object
description:
    - This module is used to configure SystemConfiguration object
    - more examples at U(https://github.com/avinetworks/devops)
requirements: [ avisdk ]
version_added: "2.3"
options:
    state:
        description:
            - The state that should be applied on the entity.
        default: present
        choices: ["absent", "present"]
        type: str
    avi_api_update_method:
        description:
            - Default method for object update is HTTP PUT.
            - Setting to patch will override that behavior to use HTTP PATCH.
        version_added: "2.5"
        default: put
        choices: ["put", "patch"]
        type: str
    avi_api_patch_op:
        description:
            - Patch operation to use when using avi_api_update_method as patch.
        version_added: "2.5"
        choices: ["add", "replace", "delete"]
        type: str
    admin_auth_configuration:
        description:
            - Adminauthconfiguration settings for systemconfiguration.
        type: dict
    default_license_tier:
        description:
            - Specifies the default license tier which would be used by new clouds.
            - Enum options - ENTERPRISE_16, ENTERPRISE_18.
            - Field introduced in 17.2.5.
            - Default value when not specified in API or module is interpreted by Avi Controller as ENTERPRISE_18.
        version_added: "2.5"
        type: str
    dns_configuration:
        description:
            - Dnsconfiguration settings for systemconfiguration.
        type: dict
    dns_virtualservice_refs:
        description:
            - Dns virtualservices hosting fqdn records for applications across avi vantage.
            - If no virtualservices are provided, avi vantage will provide dns services for configured applications.
            - Switching back to avi vantage from dns virtualservices is not allowed.
            - It is a reference to an object of type virtualservice.
        type: list
    docker_mode:
        description:
            - Boolean flag to set docker_mode.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    email_configuration:
        description:
            - Emailconfiguration settings for systemconfiguration.
        type: dict
    global_tenant_config:
        description:
            - Tenantconfiguration settings for systemconfiguration.
        type: dict
    linux_configuration:
        description:
            - Linuxconfiguration settings for systemconfiguration.
        type: dict
    mgmt_ip_access_control:
        description:
            - Configure ip access control for controller to restrict open access.
        type: dict
    ntp_configuration:
        description:
            - Ntpconfiguration settings for systemconfiguration.
        type: dict
    portal_configuration:
        description:
            - Portalconfiguration settings for systemconfiguration.
        type: dict
    proxy_configuration:
        description:
            - Proxyconfiguration settings for systemconfiguration.
        type: dict
    secure_channel_configuration:
        description:
            - Configure secure channel properties.
            - Field introduced in 18.1.4, 18.2.1.
        version_added: "2.9"
        type: dict
    snmp_configuration:
        description:
            - Snmpconfiguration settings for systemconfiguration.
        type: dict
    ssh_ciphers:
        description:
            - Allowed ciphers list for ssh to the management interface on the controller and service engines.
            - If this is not specified, all the default ciphers are allowed.
        type: list
    ssh_hmacs:
        description:
            - Allowed hmac list for ssh to the management interface on the controller and service engines.
            - If this is not specified, all the default hmacs are allowed.
        type: list
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Unique object identifier of the object.
        type: str
    welcome_workflow_complete:
        description:
            - This flag is set once the initial controller setup workflow is complete.
            - Field introduced in 18.2.3.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        version_added: "2.9"
        type: bool


extends_documentation_fragment:
    - avi
'''

EXAMPLES = """
- name: Example to create SystemConfiguration object
  avi_systemconfiguration:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_systemconfiguration
"""

RETURN = '''
obj:
    description: SystemConfiguration (api/systemconfiguration) object
    returned: success, changed
    type: dict
'''

from ansible.module_utils.basic import AnsibleModule
try:
    from avi.sdk.utils.ansible_utils import avi_common_argument_spec
    from avi.sdk.utils.ansible_utils import (
        avi_ansible_api, avi_common_argument_spec)
    HAS_AVI = True
except ImportError:
    HAS_AVI = False


def main():
    argument_specs = dict(
        state=dict(default='present',
                   choices=['absent', 'present']),
        avi_api_update_method=dict(default='put',
                                   choices=['put', 'patch']),
        avi_api_patch_op=dict(choices=['add', 'replace', 'delete']),
        admin_auth_configuration=dict(type='dict',),
        default_license_tier=dict(type='str',),
        dns_configuration=dict(type='dict',),
        dns_virtualservice_refs=dict(type='list',),
        docker_mode=dict(type='bool',),
        email_configuration=dict(type='dict',),
        global_tenant_config=dict(type='dict',),
        linux_configuration=dict(type='dict',),
        mgmt_ip_access_control=dict(type='dict',),
        ntp_configuration=dict(type='dict',),
        portal_configuration=dict(type='dict',),
        proxy_configuration=dict(type='dict',),
        secure_channel_configuration=dict(type='dict',),
        snmp_configuration=dict(type='dict',),
        ssh_ciphers=dict(type='list',),
        ssh_hmacs=dict(type='list',),
        url=dict(type='str',),
        uuid=dict(type='str',),
        welcome_workflow_complete=dict(type='bool',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk>=17.1) or requests is not installed. '
            'For more details visit https://github.com/avinetworks/sdk.'))
    return avi_ansible_api(module, 'systemconfiguration',
                           set([]))


if __name__ == '__main__':
    main()
