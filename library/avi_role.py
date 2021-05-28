#!/usr/bin/python3
# module_check: supported

# Avi Version: 17.1.1
# Copyright 2021 VMware, Inc.  All rights reserved. VMware Confidential
# SPDX-License-Identifier: Apache License 2.0


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_role
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of Role Avi RESTful Object
description:
    - This module is used to configure Role object
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
    allow_unlabelled_access:
        description:
            - Allow access to unlabelled objects.
            - Field introduced in 20.1.5.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 21.1.1.
        type: dict
    filters:
        description:
            - Filters for granular object access control based on object labels.
            - Multiple filters are merged using the and operator.
            - If empty, all objects according to the privileges will be accessible to the user.
            - Field introduced in 20.1.3.
            - Maximum of 4 items allowed.
        type: list
    name:
        description:
            - Name of the object.
        required: true
        type: str
    privileges:
        description:
            - List of permission.
        type: list
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
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
- name: Example to create Role object
  avi_role:
    controller: 192.168.15.18
    username: admin
    password: something
    state: present
    name: sample_role
"""

RETURN = '''
obj:
    description: Role (api/role) object
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
        allow_unlabelled_access=dict(type='bool',),
        configpb_attributes=dict(type='dict',),
        filters=dict(type='list',),
        name=dict(type='str', required=True),
        privileges=dict(type='list',),
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
    return avi_ansible_api(module, 'role',
                           set())


if __name__ == '__main__':
    main()
