#!/usr/bin/python
#
# Created on Aug 25, 2016
# @author: Gaurav Rastogi (grastogi@avinetworks.com)
#          Eric Anderson (eanderson@avinetworks.com)
# module_check: not supported
# Avi Version: 16.3
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

import os
# Comment: import * is to make the modules work in ansible 2.0 environments
# from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.basic import *
from avi.sdk.utils.ansible_utils import (ansible_return, purge_optional_fields,
    avi_obj_cmp, cleanup_absent_fields, avi_ansible_api)

EXAMPLES = """
- code: 'avi_backupconfiguration controller=10.10.25.42 username=admin '
            ' password=something'
            ' state=present name=sample_backupconfiguration'
description: "Adds/Deletes BackupConfiguration configuration from Avi Controller."
"""

DOCUMENTATION = '''
---
module: avi_backupconfiguration
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: BackupConfiguration Configuration
description:
    - This module is used to configure BackupConfiguration object
    - more examples at <https://github.com/avinetworks/avi-ansible-samples>
requirements: [ avisdk ]
version_added: 2.3
options:
    controller:
        description:
            - location of the controller. Environment variable AVI_CONTROLLER is default
    username:
        description:
            - username to access the Avi. Environment variable AVI_USERNAME is default
    password:
        description:
            - password of the Avi user. Environment variable AVI_PASSWORD is default
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
    backup_passphrase:
        description:
            - Passphrase of backup configuration
        type: string
    maximum_backups_stored:
        description:
            - Rotate the backup files based on this count.
        default: 4
        type: integer
    name:
        description:
            - Name of backup configuration.
        required: true
        type: string
    remote_directory:
        description:
            - Directory at remote destination with write permission for ssh user.
        type: string
    remote_hostname:
        description:
            - Remote Destination.
        type: string
    save_local:
        description:
            - Local Backup
        type: bool
    ssh_user_ref:
        description:
            - Access Credentials for remote destination. object ref CloudConnectorUser.
        type: string
    tenant_ref:
        description:
            - Not present. object ref Tenant.
        type: string
    upload_to_remote_host:
        description:
            - Remote Backup
        type: bool
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
    description: BackupConfiguration (api/backupconfiguration) object
    returned: success, changed
    type: dict
'''

def main():
    try:
        module = AnsibleModule(
            argument_spec=dict(
                controller=dict(default=os.environ.get('AVI_CONTROLLER', '')),
                username=dict(default=os.environ.get('AVI_USERNAME', '')),
                password=dict(default=os.environ.get('AVI_PASSWORD', '')),
                tenant=dict(default='admin'),
                tenant_uuid=dict(default=''),
                state=dict(default='present',
                           choices=['absent', 'present']),
                backup_passphrase=dict(
                    type='str',
                    ),
                maximum_backups_stored=dict(
                    type='int',
                    ),
                name=dict(
                    type='str',
                    ),
                remote_directory=dict(
                    type='str',
                    ),
                remote_hostname=dict(
                    type='str',
                    ),
                save_local=dict(
                    type='bool',
                    ),
                ssh_user_ref=dict(
                    type='str',
                    ),
                tenant_ref=dict(
                    type='str',
                    ),
                upload_to_remote_host=dict(
                    type='bool',
                    ),
                url=dict(
                    type='str',
                    ),
                uuid=dict(
                    type='str',
                    ),
                ),
        )
        return avi_ansible_api(module, 'backupconfiguration',
                               set(['backup_passphrase']))
    except:
        raise


if __name__ == '__main__':
    main()