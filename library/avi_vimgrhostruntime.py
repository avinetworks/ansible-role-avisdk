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
- code: 'avi_vimgrhostruntime controller=10.10.25.42 username=admin '
            ' password=something'
            ' state=present name=sample_vimgrhostruntime'
description: "Adds/Deletes VIMgrHostRuntime configuration from Avi Controller."
"""

DOCUMENTATION = '''
---
module: avi_vimgrhostruntime
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: VIMgrHostRuntime Configuration
description:
    - This module is used to configure VIMgrHostRuntime object
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
    cloud_ref:
        description:
            - Not present. object ref Cloud.
        default: Default-Cloud
        type: string
    cluster_name:
        description:
            - Not present.
        type: string
    cluster_uuid:
        description:
            - Not present.
        type: string
    cntlr_accessible:
        description:
            - Not present.
        default: True
        type: bool
    connection_state:
        description:
            - Not present.
        default: connected
        type: string
    cpu_hz:
        description:
            - Not present.
        type: integer
    maintenance_mode:
        description:
            - Not present.
        type: bool
    managed_object_id:
        description:
            - Not present.
        required: true
        type: string
    mem:
        description:
            - Not present.
        type: integer
    mgmt_portgroup:
        description:
            - Not present.
        default: 
        type: string
    name:
        description:
            - Not present.
        required: true
        type: string
    network_uuids:
        description:
            - Not present.
        type: string
    num_cpu_cores:
        description:
            - Not present.
        type: integer
    num_cpu_packages:
        description:
            - Not present.
        type: integer
    num_cpu_threads:
        description:
            - Not present.
        type: integer
    pnics:
        description:
            - Not present.
        type: CdpLldpInfo
    powerstate:
        description:
            - Not present.
        type: string
    quarantine_start_ts:
        description:
            - Not present.
        type: string
    quarantined:
        description:
            - Not present.
        type: bool
    quarantined_periods:
        description:
            - Not present.
        default: 1
        type: integer
    se_fail_cnt:
        description:
            - Not present.
        type: integer
    se_success_cnt:
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
    vm_refs:
        description:
            - Not present. object ref VIMgrVMRuntime.
        type: string
'''

RETURN = '''
obj:
    description: VIMgrHostRuntime (api/vimgrhostruntime) object
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
                cloud_ref=dict(
                    type='str',
                    ),
                cluster_name=dict(
                    type='str',
                    ),
                cluster_uuid=dict(
                    type='str',
                    ),
                cntlr_accessible=dict(
                    type='bool',
                    ),
                connection_state=dict(
                    type='str',
                    ),
                cpu_hz=dict(
                    type='int',
                    ),
                maintenance_mode=dict(
                    type='bool',
                    ),
                managed_object_id=dict(
                    type='str',
                    ),
                mem=dict(
                    type='int',
                    ),
                mgmt_portgroup=dict(
                    type='str',
                    ),
                name=dict(
                    type='str',
                    ),
                network_uuids=dict(
                    type='list',
                    ),
                num_cpu_cores=dict(
                    type='int',
                    ),
                num_cpu_packages=dict(
                    type='int',
                    ),
                num_cpu_threads=dict(
                    type='int',
                    ),
                pnics=dict(
                    type='list',
                    ),
                powerstate=dict(
                    type='str',
                    ),
                quarantine_start_ts=dict(
                    type='str',
                    ),
                quarantined=dict(
                    type='bool',
                    ),
                quarantined_periods=dict(
                    type='int',
                    ),
                se_fail_cnt=dict(
                    type='int',
                    ),
                se_success_cnt=dict(
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
                vm_refs=dict(
                    type='list',
                    ),
                ),
        )
        return avi_ansible_api(module, 'vimgrhostruntime',
                               set([]))
    except:
        raise


if __name__ == '__main__':
    main()