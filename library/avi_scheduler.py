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
- code: 'avi_scheduler controller=10.10.25.42 username=admin '
            ' password=something'
            ' state=present name=sample_scheduler'
description: "Adds/Deletes Scheduler configuration from Avi Controller."
"""

DOCUMENTATION = '''
---
module: avi_scheduler
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: Scheduler Configuration
description:
    - This module is used to configure Scheduler object
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
            - Backup Configuration to be executed by this scheduler object ref BackupConfiguration.
        type: string
    enabled:
        description:
            - Not present.
        default: True
        type: bool
    end_date_time:
        description:
            - Scheduler end date and time
        type: string
    frequency:
        description:
            - Frequency at which CUSTOM scheduler will run
        type: integer
    frequency_unit:
        description:
            - Unit at which CUSTOM scheduler will run
        type: string
    name:
        description:
            - Name of scheduler
        required: true
        type: string
    run_mode:
        description:
            - Scheduler Run Mode
        type: string
    run_script_ref:
        description:
            - Control script to be executed by this scheduler object ref AlertScriptConfig.
        type: string
    scheduler_action:
        description:
            - Define Scheduler Action
        default: 2
        type: string
    start_date_time:
        description:
            - Scheduler start date and time
        type: string
    tenant_ref:
        description:
            - Not present. object ref Tenant.
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
    description: Scheduler (api/scheduler) object
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
                enabled=dict(
                    type='bool',
                    ),
                end_date_time=dict(
                    type='str',
                    ),
                frequency=dict(
                    type='int',
                    ),
                frequency_unit=dict(
                    type='str',
                    ),
                name=dict(
                    type='str',
                    ),
                run_mode=dict(
                    type='str',
                    ),
                run_script_ref=dict(
                    type='str',
                    ),
                scheduler_action=dict(
                    type='str',
                    ),
                start_date_time=dict(
                    type='str',
                    ),
                tenant_ref=dict(
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
        return avi_ansible_api(module, 'scheduler',
                               set([]))
    except:
        raise


if __name__ == '__main__':
    main()