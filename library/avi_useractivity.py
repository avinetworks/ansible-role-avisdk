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
from ansible.module_utils.basic import AnsibleModule
from avi.sdk.utils.ansible_utils import (ansible_return, purge_optional_fields,
    avi_obj_cmp, cleanup_absent_fields, avi_ansible_api)

EXAMPLES = """
- code: 'avi_useractivity controller=10.10.25.42 username=admin '
            ' password=something'
            ' state=present name=sample_useractivity'
description: "Adds/Deletes UserActivity configuration from Avi Controller."
"""

DOCUMENTATION = '''
---
module: avi_useractivity
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: UserActivity Configuration
description:
    - This module is used to configure UserActivity object
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
    concurrent_sessions:
        description:
            - Number of concurrent user sessions open.
        default: 0
        type: integer
    failed_login_attempts:
        description:
            - Number of failed login attempts before a successful login.
        default: 0
        type: integer
    last_login_ip:
        description:
            - IP of the machine the user was last logged in from.
        type: string
    last_login_timestamp:
        description:
            - Timestamp of last login.
        type: string
    last_password_update:
        description:
            - Timestamp of last password update.
        type: string
    logged_in:
        description:
            - Indicates whether the user is logged in or not.
        type: bool
    name:
        description:
            - Name of the user this object refers to.
        type: string
    previous_password:
        description:
            - Stores the previous n passwords  where n is ControllerProperties.max_password_history_count. 
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
    description: UserActivity (api/useractivity) object
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
                concurrent_sessions=dict(
                    type='int',
                    ),
                failed_login_attempts=dict(
                    type='int',
                    ),
                last_login_ip=dict(
                    type='str',
                    ),
                last_login_timestamp=dict(
                    type='str',
                    ),
                last_password_update=dict(
                    type='str',
                    ),
                logged_in=dict(
                    type='bool',
                    ),
                name=dict(
                    type='str',
                    ),
                previous_password=dict(
                    type='list',
                    ),
                url=dict(
                    type='str',
                    ),
                uuid=dict(
                    type='str',
                    ),
                ),
        )
        return avi_ansible_api(module, 'useractivity',
                               set([]))
    except:
        raise


if __name__ == '__main__':
    main()