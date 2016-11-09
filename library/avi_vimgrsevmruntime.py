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
- code: 'avi_vimgrsevmruntime controller=10.10.25.42 username=admin '
            ' password=something'
            ' state=present name=sample_vimgrsevmruntime'
description: "Adds/Deletes VIMgrSEVMRuntime configuration from Avi Controller."
"""

DOCUMENTATION = '''
---
module: avi_vimgrsevmruntime
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: VIMgrSEVMRuntime Configuration
description:
    - This module is used to configure VIMgrSEVMRuntime object
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
    cloud_name:
        description:
            - Not present.
        type: string
    cloud_ref:
        description:
            - Not present. object ref Cloud.
        default: Default-Cloud
        type: string
    connection_state:
        description:
            - Not present.
        type: string
    controller_cluster_uuid:
        description:
            - Not present.
        type: string
    controller_ip_addr:
        description:
            - Not present.
        type: string
    creation_in_progress:
        description:
            - Not present.
        type: bool
    deletion_in_progress:
        description:
            - Not present.
        type: bool
    discovery_response:
        description:
            - Not present.
        type: string
    discovery_status:
        description:
            - Not present.
        type: integer
    flavor:
        description:
            - Not present.
        default: 
        type: string
    guest_nic:
        description:
            - Not present.
        type: VIMgrGuestNicRuntime
    host:
        description:
            - Not present.
        type: string
    host_ref:
        description:
            - Not present. object ref VIMgrHostRuntime.
        type: string
    hostid:
        description:
            - Not present.
        type: string
    hypervisor:
        description:
            - Not present.
        type: string
    init_vnics:
        description:
            - Not present.
        type: integer
    last_discovery:
        description:
            - Not present.
        type: integer
    managed_object_id:
        description:
            - Not present.
        required: true
        type: string
    name:
        description:
            - Not present.
        required: true
        type: string
    powerstate:
        description:
            - Not present.
        type: string
    security_group_uuid:
        description:
            - Not present.
        type: string
    segroup_ref:
        description:
            - Not present. object ref ServiceEngineGroup.
        type: string
    server_group_uuid:
        description:
            - Not present.
        type: string
    tenant_ref:
        description:
            - Not present. object ref Tenant.
        default: admin
        type: string
    type:
        description:
            - Not present.
        required: true
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
    vcenter_datacenter_uuid:
        description:
            - Not present.
        type: string
    vcenter_rm_cookie:
        description:
            - Not present.
        type: string
    vcenter_se_type:
        description:
            - Not present.
        type: string
    vcenter_template_vm:
        description:
            - Not present.
        type: bool
    vcenter_vAppName:
        description:
            - Not present.
        type: string
    vcenter_vAppVendor:
        description:
            - Not present.
        type: string
    vcenter_vm_type:
        description:
            - Not present.
        type: string
'''

RETURN = '''
obj:
    description: VIMgrSEVMRuntime (api/vimgrsevmruntime) object
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
                cloud_name=dict(
                    type='str',
                    ),
                cloud_ref=dict(
                    type='str',
                    ),
                connection_state=dict(
                    type='str',
                    ),
                controller_cluster_uuid=dict(
                    type='str',
                    ),
                controller_ip_addr=dict(
                    type='str',
                    ),
                creation_in_progress=dict(
                    type='bool',
                    ),
                deletion_in_progress=dict(
                    type='bool',
                    ),
                discovery_response=dict(
                    type='str',
                    ),
                discovery_status=dict(
                    type='int',
                    ),
                flavor=dict(
                    type='str',
                    ),
                guest_nic=dict(
                    type='list',
                    ),
                host=dict(
                    type='str',
                    ),
                host_ref=dict(
                    type='str',
                    ),
                hostid=dict(
                    type='str',
                    ),
                hypervisor=dict(
                    type='str',
                    ),
                init_vnics=dict(
                    type='int',
                    ),
                last_discovery=dict(
                    type='int',
                    ),
                managed_object_id=dict(
                    type='str',
                    ),
                name=dict(
                    type='str',
                    ),
                powerstate=dict(
                    type='str',
                    ),
                security_group_uuid=dict(
                    type='str',
                    ),
                segroup_ref=dict(
                    type='str',
                    ),
                server_group_uuid=dict(
                    type='str',
                    ),
                tenant_ref=dict(
                    type='str',
                    ),
                type=dict(
                    type='str',
                    ),
                url=dict(
                    type='str',
                    ),
                uuid=dict(
                    type='str',
                    ),
                vcenter_datacenter_uuid=dict(
                    type='str',
                    ),
                vcenter_rm_cookie=dict(
                    type='str',
                    ),
                vcenter_se_type=dict(
                    type='str',
                    ),
                vcenter_template_vm=dict(
                    type='bool',
                    ),
                vcenter_vAppName=dict(
                    type='str',
                    ),
                vcenter_vAppVendor=dict(
                    type='str',
                    ),
                vcenter_vm_type=dict(
                    type='str',
                    ),
                ),
        )
        return avi_ansible_api(module, 'vimgrsevmruntime',
                               set([]))
    except:
        raise


if __name__ == '__main__':
    main()