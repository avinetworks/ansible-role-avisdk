#!/usr/bin/python
# module_check: supported

# Copyright 2021 VMware, Inc.  All rights reserved. VMware Confidential
# SPDX-License-Identifier: Apache License 2.0


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_backupconfiguration
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of BackupConfiguration Avi RESTful Object
description:
    - This module is used to configure BackupConfiguration object
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
    aws_access_key:
        description:
            - Aws access key id.
            - Field introduced in 18.2.3.
            - Allowed in enterprise with any value edition, enterprise with cloud services edition.
        version_added: "2.9"
        type: str
    aws_bucket_id:
        description:
            - Aws bucket.
            - Field introduced in 18.2.3.
            - Allowed in enterprise with any value edition, enterprise with cloud services edition.
        version_added: "2.9"
        type: str
    aws_secret_access:
        description:
            - Aws secret access key.
            - Field introduced in 18.2.3.
            - Allowed in enterprise with any value edition, enterprise with cloud services edition.
        version_added: "2.9"
        type: str
    backup_file_prefix:
        description:
            - Prefix of the exported configuration file.
            - Field introduced in 17.1.1.
            - Allowed in enterprise with any value edition, essentials edition, basic edition, enterprise with cloud services edition.
        type: str
    backup_passphrase:
        description:
            - Default passphrase for configuration export and periodic backup.
            - Allowed in enterprise with any value edition, essentials edition, basic edition, enterprise with cloud services edition.
        type: str
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 21.1.1.
            - Allowed in enterprise with any value edition, essentials with any value edition, basic with any value edition, enterprise with cloud services
            - edition.
        type: dict
    maximum_backups_stored:
        description:
            - Rotate the backup files based on this count.
            - Allowed values are 1-20.
            - Allowed in enterprise with any value edition, essentials edition, basic edition, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 4.
        type: int
    name:
        description:
            - Name of backup configuration.
            - Allowed in enterprise with any value edition, essentials edition, basic edition, enterprise with cloud services edition.
        required: true
        type: str
    remote_directory:
        description:
            - Directory at remote destination with write permission for ssh user.
            - Allowed in enterprise with any value edition, essentials edition, basic edition, enterprise with cloud services edition.
        type: str
    remote_file_transfer_protocol:
        description:
            - Remote file transfer protocol type.
            - Enum options - SCP, SFTP.
            - Field introduced in 22.1.1.
            - Allowed in enterprise with any value edition, basic(allowed values- scp,sftp) edition, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as SCP.
        type: str
    remote_hostname:
        description:
            - Remote destination.
            - Allowed in enterprise with any value edition, essentials edition, basic edition, enterprise with cloud services edition.
        type: str
    save_local:
        description:
            - Local backup.
            - Allowed in enterprise with any value edition, essentials edition, basic edition, enterprise with cloud services edition.
        type: bool
    ssh_user_ref:
        description:
            - Access credentials for remote destination.
            - It is a reference to an object of type cloudconnectoruser.
            - Allowed in enterprise with any value edition, essentials edition, basic edition, enterprise with cloud services edition.
        type: str
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
            - Allowed in enterprise with any value edition, essentials edition, basic edition, enterprise with cloud services edition.
        type: str
    upload_to_remote_host:
        description:
            - Remote backup.
            - Allowed in enterprise with any value edition, essentials edition, basic edition, enterprise with cloud services edition.
        type: bool
    upload_to_s3:
        description:
            - Cloud backup.
            - Field introduced in 18.2.3.
            - Allowed in enterprise with any value edition, enterprise with cloud services edition.
        version_added: "2.9"
        type: bool
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

- name: Example to create BackupConfiguration object
  avi_backupconfiguration:
    avi_credentials: "{{ avi_credentials }}"
    state: present
    name: sample_backupconfiguration
"""

RETURN = '''
obj:
    description: BackupConfiguration (api/backupconfiguration) object
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
        aws_access_key=dict(type='str', no_log=True,),
        aws_bucket_id=dict(type='str',),
        aws_secret_access=dict(type='str', no_log=True,),
        backup_file_prefix=dict(type='str',),
        backup_passphrase=dict(type='str', no_log=True,),
        configpb_attributes=dict(type='dict',),
        maximum_backups_stored=dict(type='int',),
        name=dict(type='str', required=True),
        remote_directory=dict(type='str',),
        remote_file_transfer_protocol=dict(type='str',),
        remote_hostname=dict(type='str',),
        save_local=dict(type='bool',),
        ssh_user_ref=dict(type='str',),
        tenant_ref=dict(type='str',),
        upload_to_remote_host=dict(type='bool',),
        upload_to_s3=dict(type='bool',),
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
    return avi_ansible_api(module, 'backupconfiguration',
                           ['aws_access_key', 'aws_secret_access', 'backup_passphrase'])


if __name__ == '__main__':
    main()
