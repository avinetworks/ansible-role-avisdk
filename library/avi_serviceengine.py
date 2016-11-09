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
- code: 'avi_serviceengine controller=10.10.25.42 username=admin '
            ' password=something'
            ' state=present name=sample_serviceengine'
description: "Adds/Deletes ServiceEngine configuration from Avi Controller."
"""

DOCUMENTATION = '''
---
module: avi_serviceengine
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: ServiceEngine Configuration
description:
    - This module is used to configure ServiceEngine object
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
    availability_zone:
        description:
            - Not present.
        type: string
    cloud_ref:
        description:
            - Not present. object ref Cloud.
        default: Default-Cloud
        type: string
    container_mode:
        description:
            - Not present.
        default: False
        type: bool
    controller_created:
        description:
            - Not present.
        default: False
        type: bool
    controller_ip:
        description:
            - Not present.
        type: string
    data_vnics:
        description:
            - Not present.
        type: vNIC
    enable_state:
        description:
            - inorder to disable SE set this field appropriately
        default: 0
        type: string
    flavor:
        description:
            - Not present.
        default: 
        type: string
    host_ref:
        description:
            - Not present. object ref VIMgrHostRuntime.
        type: string
    hypervisor:
        description:
            - Not present.
        type: string
    mgmt_vnic:
        description:
            - Not present.
        type: vNIC
    name:
        description:
            - Not present.
        default: VM name unknown
        type: string
    resources:
        description:
            - Not present.
        type: SeResources
    se_group_ref:
        description:
            - Not present. object ref ServiceEngineGroup.
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
    description: ServiceEngine (api/serviceengine) object
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
                availability_zone=dict(
                    type='str',
                    ),
                cloud_ref=dict(
                    type='str',
                    ),
                container_mode=dict(
                    type='bool',
                    ),
                controller_created=dict(
                    type='bool',
                    ),
                controller_ip=dict(
                    type='str',
                    ),
                data_vnics=dict(
                    type='list',
                    ),
                enable_state=dict(
                    type='str',
                    ),
                flavor=dict(
                    type='str',
                    ),
                host_ref=dict(
                    type='str',
                    ),
                hypervisor=dict(
                    type='str',
                    ),
                mgmt_vnic=dict(
                    type='dict',
                    ),
                name=dict(
                    type='str',
                    ),
                resources=dict(
                    type='dict',
                    ),
                se_group_ref=dict(
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
        return avi_ansible_api(module, 'serviceengine',
                               set([]))
    except:
        raise


if __name__ == '__main__':
    main()