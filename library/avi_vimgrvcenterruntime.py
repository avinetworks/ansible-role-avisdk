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
- code: 'avi_vimgrvcenterruntime controller=10.10.25.42 username=admin '
            ' password=something'
            ' state=present name=sample_vimgrvcenterruntime'
description: "Adds/Deletes VIMgrVcenterRuntime configuration from Avi Controller."
"""

DOCUMENTATION = '''
---
module: avi_vimgrvcenterruntime
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: VIMgrVcenterRuntime Configuration
description:
    - This module is used to configure VIMgrVcenterRuntime object
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
    api_version:
        description:
            - Not present.
        type: string
    apic_mode:
        description:
            - Not present.
        default: False
        type: bool
    cloud_ref:
        description:
            - Not present. object ref Cloud.
        default: Default-Cloud
        type: string
    datacenter_refs:
        description:
            - Not present. object ref VIMgrDCRuntime.
        type: string
    disc_end_time:
        description:
            - Not present.
        type: string
    disc_start_time:
        description:
            - Not present.
        type: string
    discovered_datacenter:
        description:
            - Not present.
        type: string
    inventory_progress:
        description:
            - Not present.
        type: string
    inventory_state:
        description:
            - Not present.
        type: string
    management_network:
        description:
            - Not present.
        type: string
    name:
        description:
            - Not present.
        required: true
        type: string
    num_clusters:
        description:
            - Not present.
        type: integer
    num_dcs:
        description:
            - Not present.
        type: integer
    num_hosts:
        description:
            - Not present.
        type: integer
    num_nws:
        description:
            - Not present.
        type: integer
    num_vcenter_req_pending:
        description:
            - Not present.
        type: integer
    num_vms:
        description:
            - Not present.
        type: integer
    privilege:
        description:
            - Not present.
        type: string
    progress:
        description:
            - Not present.
        type: integer
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
    vcenter_connected:
        description:
            - Not present.
        default: False
        type: bool
    vcenter_fullname:
        description:
            - Not present.
        type: string
    vcenter_template_se_location:
        description:
            - Not present.
        type: string
    vcenter_url:
        description:
            - Not present.
        required: true
        type: string
'''

RETURN = '''
obj:
    description: VIMgrVcenterRuntime (api/vimgrvcenterruntime) object
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
                api_version=dict(
                    type='str',
                    ),
                apic_mode=dict(
                    type='bool',
                    ),
                cloud_ref=dict(
                    type='str',
                    ),
                datacenter_refs=dict(
                    type='list',
                    ),
                disc_end_time=dict(
                    type='str',
                    ),
                disc_start_time=dict(
                    type='str',
                    ),
                discovered_datacenter=dict(
                    type='str',
                    ),
                inventory_progress=dict(
                    type='str',
                    ),
                inventory_state=dict(
                    type='str',
                    ),
                management_network=dict(
                    type='str',
                    ),
                name=dict(
                    type='str',
                    ),
                num_clusters=dict(
                    type='int',
                    ),
                num_dcs=dict(
                    type='int',
                    ),
                num_hosts=dict(
                    type='int',
                    ),
                num_nws=dict(
                    type='int',
                    ),
                num_vcenter_req_pending=dict(
                    type='int',
                    ),
                num_vms=dict(
                    type='int',
                    ),
                privilege=dict(
                    type='str',
                    ),
                progress=dict(
                    type='int',
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
                vcenter_connected=dict(
                    type='bool',
                    ),
                vcenter_fullname=dict(
                    type='str',
                    ),
                vcenter_template_se_location=dict(
                    type='str',
                    ),
                vcenter_url=dict(
                    type='str',
                    ),
                ),
        )
        return avi_ansible_api(module, 'vimgrvcenterruntime',
                               set([]))
    except:
        raise


if __name__ == '__main__':
    main()