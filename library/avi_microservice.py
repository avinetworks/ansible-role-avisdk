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
- code: 'avi_microservice controller=10.10.25.42 username=admin '
            ' password=something'
            ' state=present name=sample_microservice'
description: "Adds/Deletes MicroService configuration from Avi Controller."
"""

DOCUMENTATION = '''
---
module: avi_microservice
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: MicroService Configuration
description:
    - This module is used to configure MicroService object
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
    application_name:
        description:
            - Not present.
        required: true
        type: string
    containers:
        description:
            - The list of containers for this microservice
        type: MicroServiceContainer
    created_by:
        description:
            - Creator name
        type: string
    description:
        description:
            - Not present.
        type: string
    ip_list:
        description:
            - Flag to indicate if container IP list is provided by cloud connectorThis is applicable for overlay cases.
        type: bool
    name:
        description:
            - Not present.
        required: true
        type: string
    orchestrator_name:
        description:
            - Not present.
        required: true
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
    description: MicroService (api/microservice) object
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
                application_name=dict(
                    type='str',
                    ),
                containers=dict(
                    type='list',
                    ),
                created_by=dict(
                    type='str',
                    ),
                description=dict(
                    type='str',
                    ),
                ip_list=dict(
                    type='bool',
                    ),
                name=dict(
                    type='str',
                    ),
                orchestrator_name=dict(
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
        return avi_ansible_api(module, 'microservice',
                               set([]))
    except:
        raise


if __name__ == '__main__':
    main()