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
from copy import deepcopy
from avi.sdk.avi_api import ApiSession, ObjectNotFound
from avi.sdk.utils.ansible_utils import (ansible_return, purge_optional_fields,
    avi_obj_cmp, cleanup_absent_fields)

EXAMPLES = """
- code: 'avi_vimgrvmruntime controller=10.10.25.42 username=admin '
            ' password=something'
            ' state=present name=sample_vimgrvmruntime'
description: "Adds/Deletes VIMgrVMRuntime configuration from Avi Controller."
"""

DOCUMENTATION = '''
---
module: avi_vimgrvmruntime
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: VIMgrVMRuntime Configuration
description:
    - This module is used to configure VIMgrVMRuntime object
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
    availability_zone:
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
    controller_vm:
        description:
            - Not present.
        type: bool
    cpu_reservation:
        description:
            - Not present.
        type: integer
    cpu_shares:
        description:
            - Not present.
        type: integer
    creation_in_progress:
        description:
            - Not present.
        type: bool
    guest_nic:
        description:
            - Not present.
        type: VIMgrGuestNicRuntime
    host:
        description:
            - Not present.
        type: string
    init_vnics:
        description:
            - Not present.
        type: integer
    managed_object_id:
        description:
            - Not present.
        required: true
        type: string
    mem_shares:
        description:
            - Not present.
        type: integer
    memory:
        description:
            - Not present.
        type: integer
    memory_reservation:
        description:
            - Not present.
        type: integer
    name:
        description:
            - Not present.
        required: true
        type: string
    num_cpu:
        description:
            - Not present.
        type: integer
    powerstate:
        description:
            - Not present.
        type: string
    se_ver:
        description:
            - Not present.
        default: 1
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
    vcenter_vnic_discovered:
        description:
            - Not present.
        type: bool
    vm_lb_weight:
        description:
            - Not present.
        type: integer
'''

RETURN = '''
obj:
    description: VIMgrVMRuntime (api/vimgrvmruntime) object
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
                availability_zone=dict(
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
                controller_vm=dict(
                    type='bool',
                    ),
                cpu_reservation=dict(
                    type='int',
                    ),
                cpu_shares=dict(
                    type='int',
                    ),
                creation_in_progress=dict(
                    type='bool',
                    ),
                guest_nic=dict(
                    type='list',
                    ),
                host=dict(
                    type='str',
                    ),
                init_vnics=dict(
                    type='int',
                    ),
                managed_object_id=dict(
                    type='str',
                    ),
                mem_shares=dict(
                    type='int',
                    ),
                memory=dict(
                    type='int',
                    ),
                memory_reservation=dict(
                    type='int',
                    ),
                name=dict(
                    type='str',
                    ),
                num_cpu=dict(
                    type='int',
                    ),
                powerstate=dict(
                    type='str',
                    ),
                se_ver=dict(
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
                vcenter_vnic_discovered=dict(
                    type='bool',
                    ),
                vm_lb_weight=dict(
                    type='int',
                    ),
                ),
        )
        api = ApiSession.get_session(
                module.params['controller'],
                module.params['username'],
                module.params['password'],
                tenant=module.params['tenant'])

        state = module.params['state']
        name = module.params['name']
        sensitive_fields = set([])

        obj = deepcopy(module.params)
        obj.pop('state', None)
        obj.pop('controller', None)
        obj.pop('username', None)
        obj.pop('password', None)
        tenant = obj.pop('tenant', '')
        tenant_uuid = obj.pop('tenant_uuid', '')
        obj.pop('cloud_ref', None)

        purge_optional_fields(obj, module)

        if state == 'absent':
            try:
                rsp = api.delete_by_name(
                    'vimgrvmruntime', name,
                    tenant=tenant, tenant_uuid=tenant_uuid)
            except ObjectNotFound:
                return module.exit_json(changed=False)
            if rsp.status_code == 204:
                return module.exit_json(changed=True)
            return module.fail_json(msg=rsp.text)
        existing_obj = api.get_object_by_name(
                'vimgrvmruntime', name,
                tenant=tenant, tenant_uuid=tenant_uuid,
                params={'include_refs': '', 'include_name': ''})
        changed = False
        rsp = None
        if existing_obj:
            # this is case of modify as object exists. should find out
            # if changed is true or not
            changed = not avi_obj_cmp(obj, existing_obj, sensitive_fields)
            cleanup_absent_fields(obj)
            if changed:
                obj_uuid = existing_obj['uuid']
                rsp = api.put(
                    'vimgrvmruntime/%s' % obj_uuid, data=obj,
                    tenant=tenant, tenant_uuid=tenant_uuid)
        else:
            changed = True
            rsp = api.post('vimgrvmruntime', data=obj,
                           tenant=tenant, tenant_uuid=tenant_uuid)
        if rsp is None:
            return module.exit_json(changed=changed, obj=existing_obj)
        else:
            return ansible_return(module, rsp, changed)
    except:
        raise


if __name__ == '__main__':
    main()