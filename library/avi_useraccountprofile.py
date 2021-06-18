#!/usr/bin/python
# module_check: supported

# Avi Version: 17.1.1
# Copyright 2021 VMware, Inc.  All rights reserved. VMware Confidential
# SPDX-License-Identifier: Apache License 2.0


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_useraccountprofile
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of UserAccountProfile Avi RESTful Object
description:
    - This module is used to configure UserAccountProfile object
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
    account_lock_timeout:
        description:
            - Lock timeout period (in minutes).
            - Default is 30 minutes.
            - Unit is min.
            - Default value when not specified in API or module is interpreted by Avi Controller as 30.
        type: int
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 21.1.1.
        type: dict
    credentials_timeout_threshold:
        description:
            - The time period after which credentials expire.
            - Default is 180 days.
            - Unit is days.
            - Default value when not specified in API or module is interpreted by Avi Controller as 180.
        type: int
    max_concurrent_sessions:
        description:
            - Maximum number of concurrent sessions allowed.
            - There are unlimited sessions by default.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    max_login_failure_count:
        description:
            - Number of login attempts before lockout.
            - Default is 3 attempts.
            - Allowed values are 3-20.
            - Special values are 0 - 'unlimited login attempts allowed.'.
            - Default value when not specified in API or module is interpreted by Avi Controller as 3.
        type: int
    max_password_history_count:
        description:
            - Maximum number of passwords to be maintained in the password history.
            - Default is 4 passwords.
            - Default value when not specified in API or module is interpreted by Avi Controller as 4.
        type: int
    name:
        description:
            - Name of the object.
        required: true
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Unique object identifier of the object.
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

- name: Example to create UserAccountProfile object
  avi_useraccountprofile:
    avi_credentials: "{{ avi_credentials }}"
    state: present
    name: sample_useraccountprofile
"""

RETURN = '''
obj:
    description: UserAccountProfile (api/useraccountprofile) object
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
        account_lock_timeout=dict(type='int',),
        configpb_attributes=dict(type='dict',),
        credentials_timeout_threshold=dict(type='int',),
        max_concurrent_sessions=dict(type='int',),
        max_login_failure_count=dict(type='int',),
        max_password_history_count=dict(type='int',),
        name=dict(type='str', required=True),
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
    return avi_ansible_api(module, 'useraccountprofile',
                           set())


if __name__ == '__main__':
    main()
