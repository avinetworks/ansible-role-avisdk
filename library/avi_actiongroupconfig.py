#!/usr/bin/python
# module_check: supported

# Copyright 2021 VMware, Inc.  All rights reserved. VMware Confidential
# SPDX-License-Identifier: Apache License 2.0


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_actiongroupconfig
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of ActionGroupConfig Avi RESTful Object
description:
    - This module is used to configure ActionGroupConfig object
    - more examples at U(https://github.com/avinetworks/devops)
requirements: [ avisdk ]
version_added: "2.4"
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
        choices: ["add", "replace", "delete", "remove"]
        type: str
    avi_patch_path:
        description:
            - Patch path to use when using avi_api_update_method as patch.
        type: str
    avi_patch_value:
        description:
            - Patch value to use when using avi_api_update_method as patch.
        type: str
    action_script_config_ref:
        description:
            - Reference of the action script configuration to be used.
            - It is a reference to an object of type alertscriptconfig.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    autoscale_trigger_notification:
        description:
            - Trigger notification to autoscale manager.
            - Allowed in enterprise edition with any value, essentials edition(allowed values- false), basic edition(allowed values- false), enterprise with
            - cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
        type: dict
    description:
        description:
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    email_config_ref:
        description:
            - Select the email notification configuration to use when sending alerts via email.
            - It is a reference to an object of type alertemailconfig.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: str
    external_only:
        description:
            - Generate alert only to external destinations.
            - Allowed in enterprise edition with any value, essentials edition(allowed values- false), basic edition(allowed values- false), enterprise with
            - cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        required: true
        type: bool
    level:
        description:
            - When an alert is generated, mark its priority via the alert level.
            - Enum options - ALERT_LOW, ALERT_MEDIUM, ALERT_HIGH.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as ALERT_LOW.
        required: true
        type: str
    name:
        description:
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        required: true
        type: str
    snmp_trap_profile_ref:
        description:
            - Select the snmp trap notification to use when sending alerts via snmp trap.
            - It is a reference to an object of type snmptrapprofile.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: str
    syslog_config_ref:
        description:
            - Select the syslog notification configuration to use when sending alerts via syslog.
            - It is a reference to an object of type alertsyslogconfig.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str


extends_documentation_fragment:
    - avi
'''

EXAMPLES = """
- hosts: all
  vars:
    avi_credentials:
      username: "admin"
      password: "something"
      controller: "192.168.15.18"
      api_version: "21.1.1"

- name: Example to create ActionGroupConfig object
  avi_actiongroupconfig:
    avi_credentials: "{{ avi_credentials }}"
    state: present
    name: sample_actiongroupconfig
"""

RETURN = '''
obj:
    description: ActionGroupConfig (api/actiongroupconfig) object
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
        avi_api_patch_op=dict(choices=['add', 'replace', 'delete', 'remove']),
        avi_patch_path=dict(type='str',),
        avi_patch_value=dict(type='str',),
        action_script_config_ref=dict(type='str',),
        autoscale_trigger_notification=dict(type='bool',),
        configpb_attributes=dict(type='dict',),
        description=dict(type='str',),
        email_config_ref=dict(type='str',),
        external_only=dict(type='bool', required=True),
        level=dict(type='str', required=True),
        name=dict(type='str', required=True),
        snmp_trap_profile_ref=dict(type='str',),
        syslog_config_ref=dict(type='str',),
        tenant_ref=dict(type='str',),
        url=dict(type='str',),
        uuid=dict(type='str',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk>=17.1) or requests is not installed. '
            'For more details visit https://github.com/vmware/alb-sdk.'))
    return avi_ansible_api(module, 'actiongroupconfig',
                           set())


if __name__ == '__main__':
    main()
