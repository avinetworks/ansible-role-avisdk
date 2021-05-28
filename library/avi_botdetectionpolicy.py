#!/usr/bin/python3
# module_check: supported

# Copyright 2021 VMware, Inc.  All rights reserved. VMware Confidential
# SPDX-License-Identifier: Apache License 2.0


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_botdetectionpolicy
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of BotDetectionPolicy Avi RESTful Object
description:
    - This module is used to configure BotDetectionPolicy object
    - more examples at U(https://github.com/avinetworks/devops)
requirements: [ avisdk ]
version_added: "2.7"
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
    allow_list:
        description:
            - Allow the user to skip botmanagement for selected requests.
            - Field introduced in 21.1.1.
        type: dict
    description:
        description:
            - Human-readable description of this bot detection policy.
            - Field introduced in 21.1.1.
        type: str
    ip_location_detector:
        description:
            - The ip location configuration used in this policy.
            - Field introduced in 21.1.1.
        required: true
        type: dict
    ip_reputation_detector:
        description:
            - The ip reputation configuration used in this policy.
            - Field introduced in 21.1.1.
        required: true
        type: dict
    name:
        description:
            - The name of this bot detection policy.
            - Field introduced in 21.1.1.
        required: true
        type: str
    system_bot_mapping_ref:
        description:
            - System-defined rules for classification.
            - It is a reference to an object of type botmapping.
            - Field introduced in 21.1.1.
        type: str
    system_consolidator_ref:
        description:
            - The installation provides an updated ruleset for consolidating the results of different decider phases.
            - It is a reference to an object of type botconfigconsolidator.
            - Field introduced in 21.1.1.
        type: str
    tenant_ref:
        description:
            - The unique identifier of the tenant to which this policy belongs.
            - It is a reference to an object of type tenant.
            - Field introduced in 21.1.1.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    user_agent_detector:
        description:
            - The user-agent configuration used in this policy.
            - Field introduced in 21.1.1.
        required: true
        type: dict
    user_bot_mapping_ref:
        description:
            - User-defined rules for classification.
            - These are applied before the system classification rules.
            - If a rule matches, processing terminates and the system-defined rules will not run.
            - It is a reference to an object of type botmapping.
            - Field introduced in 21.1.1.
        type: str
    user_consolidator_ref:
        description:
            - The user-provided ruleset for consolidating the results of different decider phases.
            - This runs before the system consolidator.
            - If it successfully sets a consolidation, the system consolidator will not change it.
            - It is a reference to an object of type botconfigconsolidator.
            - Field introduced in 21.1.1.
        type: str
    uuid:
        description:
            - A unique identifier to this bot detection policy.
            - Field introduced in 21.1.1.
        type: str


extends_documentation_fragment:
    - avi
'''

EXAMPLES = """
- name: Example to create BotDetectionPolicy object
  avi_botdetectionpolicy:
    controller: 192.168.15.18
    username: admin
    password: something
    state: present
    name: sample_botdetectionpolicy
"""

RETURN = '''
obj:
    description: BotDetectionPolicy (api/botdetectionpolicy) object
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
        allow_list=dict(type='dict',),
        description=dict(type='str',),
        ip_location_detector=dict(type='dict', required=True),
        ip_reputation_detector=dict(type='dict', required=True),
        name=dict(type='str', required=True),
        system_bot_mapping_ref=dict(type='str',),
        system_consolidator_ref=dict(type='str',),
        tenant_ref=dict(type='str',),
        url=dict(type='str',),
        user_agent_detector=dict(type='dict', required=True),
        user_bot_mapping_ref=dict(type='str',),
        user_consolidator_ref=dict(type='str',),
        uuid=dict(type='str',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk>=17.1) or requests is not installed. '
            'For more details visit https://github.com/vmware/alb-sdk.'))
    return avi_ansible_api(module, 'botdetectionpolicy',
                           set())


if __name__ == '__main__':
    main()
