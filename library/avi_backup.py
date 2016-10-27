#!/usr/bin/python
#
# Created on Aug 25, 2016
# @author: Gaurav Rastogi (grastogi@avinetworks.com)
#          Eric Anderson (eanderson@avinetworks.com)
# module_check: not supported
#
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#

from ansible.module_utils.basic import AnsibleModule
from avi.sdk.utils.ansible_utils import (ansible_return, purge_optional_fields,
    avi_obj_cmp, cleanup_absent_fields, avi_ansible_api)

EXAMPLES = """
- code: 'avi_backup controller=10.10.25.42 username=admin '
            ' password=something'
            ' state=present name=sample_backup'
description: "Adds/Deletes Backup configuration from Avi Controller."
"""

DOCUMENTATION = '''
---
module: avi_backup
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: Backup Configuration
description:
    - This module is used to configure Backup object
    - more examples at <https://github.com/avinetworks/avi-ansible-samples>
requirements: [ avisdk ]
version_added: 2.1.2
options:
    controller:
        description:
            - location of the controller
        required: true
    username:
        description:
            - username to access the Avi
        required: true
    password:
        description:
            - password of the Avi user
        required: true
    tenant:
        description:
            - tenant for the operations
        default: admin
    tenant_uuid:
        description:
            - tenant uuid for the operations
        default: ''
    state:
        description:
            - The state that should be applied on the entity.
        required: false
        default: present
        choices: ["absent","present"]
    backup_config_ref:
        description:
            - BackupConfiguration Information object ref BackupConfiguration.
        type: string
    file_name:
        description:
            - The file name of backup.
        required: true
        type: string
    local_file_url:
        description:
            - URL to download the backup file
        type: string
    remote_file_url:
        description:
            - URL to download the backup file
        type: string
    scheduler_ref:
        description:
            - Scheduler Information object ref Scheduler.
        type: string
    tenant_ref:
        description:
            - Not present. object ref Tenant.
        type: string
    timestamp:
        description:
            - Unix Timestamp of when the backup file is created
        type: string
    url:
        description:
            - url
        required: true
        type: string
    uuid:
        description:
            - Not present.
        type: string
'''

RETURN = '''
obj:
    description: Backup (api/backup) object
    returned: success, changed
    type: dict
'''


def main():
    try:
        module = AnsibleModule(
            argument_spec=dict(
                controller=dict(required=True),
                username=dict(required=True),
                password=dict(required=True),
                tenant=dict(default='admin'),
                tenant_uuid=dict(default=''),
                state=dict(default='present',
                           choices=['absent', 'present']),
                backup_config_ref=dict(
                    type='str',
                    ),
                file_name=dict(
                    type='str',
                    ),
                local_file_url=dict(
                    type='str',
                    ),
                remote_file_url=dict(
                    type='str',
                    ),
                scheduler_ref=dict(
                    type='str',
                    ),
                tenant_ref=dict(
                    type='str',
                    ),
                timestamp=dict(
                    type='str',
                    ),
                url=dict(
                    type='str',
                    ),
                uuid=dict(
                    type='str',
                    ),
                ),
        )
        return avi_ansible_api(module, 'backup',
                               set([]))
    except:
        raise


if __name__ == '__main__':
    main()