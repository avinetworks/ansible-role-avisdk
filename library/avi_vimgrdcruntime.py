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
- code: 'avi_vimgrdcruntime controller=10.10.25.42 username=admin '
            ' password=something'
            ' state=present name=sample_vimgrdcruntime'
description: "Adds/Deletes VIMgrDCRuntime configuration from Avi Controller."
"""

DOCUMENTATION = '''
---
module: avi_vimgrdcruntime
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: VIMgrDCRuntime Configuration
description:
    - This module is used to configure VIMgrDCRuntime object
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
    cloud_ref:
        description:
            - Not present. object ref Cloud.
        default: Default-Cloud
        type: string
    cluster_refs:
        description:
            - Not present. object ref VIMgrClusterRuntime.
        type: string
    host_refs:
        description:
            - Not present. object ref VIMgrHostRuntime.
        type: string
    interested_hosts:
        description:
            - Not present.
        type: VIMgrInterestedEntity
    interested_nws:
        description:
            - Not present.
        type: VIMgrInterestedEntity
    interested_vms:
        description:
            - Not present.
        type: VIMgrInterestedEntity
    inventory_state:
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
    nw_refs:
        description:
            - Not present. object ref VIMgrNWRuntime.
        type: string
    pending_vcenter_reqs:
        description:
            - Not present.
        type: integer
    sevm_refs:
        description:
            - Not present. object ref VIMgrSEVMRuntime.
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
    vcenter_uuid:
        description:
            - Not present.
        type: string
    vm_refs:
        description:
            - Not present. object ref VIMgrVMRuntime.
        type: string
'''

RETURN = '''
obj:
    description: VIMgrDCRuntime (api/vimgrdcruntime) object
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
                cloud_ref=dict(
                    type='str',
                    ),
                cluster_refs=dict(
                    type='list',
                    ),
                host_refs=dict(
                    type='list',
                    ),
                interested_hosts=dict(
                    type='list',
                    ),
                interested_nws=dict(
                    type='list',
                    ),
                interested_vms=dict(
                    type='list',
                    ),
                inventory_state=dict(
                    type='int',
                    ),
                managed_object_id=dict(
                    type='str',
                    ),
                name=dict(
                    type='str',
                    ),
                nw_refs=dict(
                    type='list',
                    ),
                pending_vcenter_reqs=dict(
                    type='int',
                    ),
                sevm_refs=dict(
                    type='list',
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
                vcenter_uuid=dict(
                    type='str',
                    ),
                vm_refs=dict(
                    type='list',
                    ),
                ),
        )
        return avi_ansible_api(module, 'vimgrdcruntime',
                               set([]))
    except:
        raise


if __name__ == '__main__':
    main()