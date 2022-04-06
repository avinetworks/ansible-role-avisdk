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
module: avi_backup
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of Backup Avi RESTful Object
description:
    - This module is used to configure Backup object
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
    backup_config_ref:
        description:
            - Backupconfiguration information.
            - It is a reference to an object of type backupconfiguration.
            - Allowed in enterprise with any value edition, essentials edition, basic edition, enterprise with cloud services edition.
        type: str
    file_name:
        description:
            - The file name of backup.
            - Allowed in enterprise with any value edition, essentials edition, basic edition, enterprise with cloud services edition.
        required: true
        type: str
    local_file_url:
        description:
            - Url to download the backup file.
            - Allowed in enterprise with any value edition, essentials edition, basic edition, enterprise with cloud services edition.
        type: str
    remote_file_url:
        description:
            - Url to download the backup file.
            - Allowed in enterprise with any value edition, essentials edition, basic edition, enterprise with cloud services edition.
        type: str
    scheduler_ref:
        description:
            - Scheduler information.
            - It is a reference to an object of type scheduler.
            - Allowed in enterprise with any value edition, essentials edition, basic edition, enterprise with cloud services edition.
        type: str
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
            - Allowed in enterprise with any value edition, essentials edition, basic edition, enterprise with cloud services edition.
        type: str
    timestamp:
        description:
            - Unix timestamp of when the backup file is created.
            - Allowed in enterprise with any value edition, essentials edition, basic edition, enterprise with cloud services edition.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Allowed in enterprise with any value edition, essentials edition, basic edition, enterprise with cloud services edition.
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

- name: Example to create Backup object
  avi_backup:
    avi_credentials: "{{ avi_credentials }}"
    state: present
    name: sample_backup
"""

RETURN = '''
obj:
    description: Backup (api/backup) object
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
        backup_config_ref=dict(type='str',),
        file_name=dict(type='str', required=True),
        local_file_url=dict(type='str',),
        remote_file_url=dict(type='str',),
        scheduler_ref=dict(type='str',),
        tenant_ref=dict(type='str',),
        timestamp=dict(type='str',),
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
    return avi_ansible_api(module, 'backup',
                           set())


if __name__ == '__main__':
    main()
