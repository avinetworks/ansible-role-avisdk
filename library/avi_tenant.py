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
module: avi_tenant
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of Tenant Avi RESTful Object
description:
    - This module is used to configure Tenant object
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
    config_settings:
        description:
            - Tenantconfiguration settings for tenant.
        type: dict
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 21.1.1.
        type: dict
    created_by:
        description:
            - Creator of this tenant.
        type: str
    description:
        description:
            - User defined description for the object.
        type: str
    enforce_label_group:
        description:
            - The referred label groups are enforced on the tenant if this is set to true.if this is set to false, the label groups are suggested for the
            - tenant.
            - Field introduced in 20.1.5.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    label_group_refs:
        description:
            - The label_groups to be enforced on the tenant.
            - This is strictly enforced only if enforce_label_group is set to true.
            - It is a reference to an object of type labelgroup.
            - Field introduced in 20.1.5.
        type: list
    local:
        description:
            - Boolean flag to set local.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    name:
        description:
            - Name of the object.
        required: true
        type: str
    suggested_object_labels:
        description:
            - Suggestive pool of key value pairs for recommending assignment of labels to objects in the user interface.
            - Every entry is unique in both key and value.
            - Field deprecated in 20.1.5.
            - Field introduced in 20.1.2.
            - Maximum of 256 items allowed.
        type: list
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

- name: Create Tenant using Service Engines in provider mode
  avi_tenant:
    avi_credentials: "{{ avi_credentials }}"
    config_settings:
      se_in_provider_context: false
      tenant_access_to_provider_se: true
      tenant_vrf: false
    description: VCenter, Open Stack, AWS Virtual services
    local: true
    name: Demo
"""

RETURN = '''
obj:
    description: Tenant (api/tenant) object
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
        config_settings=dict(type='dict',),
        configpb_attributes=dict(type='dict',),
        created_by=dict(type='str',),
        description=dict(type='str',),
        enforce_label_group=dict(type='bool',),
        label_group_refs=dict(type='list',),
        local=dict(type='bool',),
        name=dict(type='str', required=True),
        suggested_object_labels=dict(type='list',),
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
    return avi_ansible_api(module, 'tenant',
                           set())


if __name__ == '__main__':
    main()
