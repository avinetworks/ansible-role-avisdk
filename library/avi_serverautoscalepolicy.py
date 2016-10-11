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
- code: 'avi_serverautoscalepolicy controller=10.10.25.42 username=admin '
            ' password=something'
            ' state=present name=sample_serverautoscalepolicy'
description: "Adds/Deletes ServerAutoScalePolicy configuration from Avi Controller."
"""

DOCUMENTATION = '''
---
module: avi_serverautoscalepolicy
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: ServerAutoScalePolicy Configuration
description:
    - This module is used to configure ServerAutoScalePolicy object
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
    description:
        description:
            - Not present.
        type: string
    intelligent_autoscale:
        description:
            - Use Avi intelligent autoscale algorithm where autoscale is performed by comparing load on the pool against estimated capacity of all the servers.
        default: False
        type: bool
    intelligent_scalein_margin:
        description:
            - Maximum extra capacity as percentage of load used by the intelligent scheme. Scalein is triggered when available capacity is more than this margin
        default: 40
        type: integer
    intelligent_scaleout_margin:
        description:
            - Minimum extra capacity as percentage of load used by the intelligent scheme. Scaleout is triggered when available capacity is less than this margin.
        default: 20
        type: integer
    max_scalein_adjustment_step:
        description:
            - Maximum number of servers to scalein simultaneously. The actual number of servers to scalein is chosen such that target number of servers is always more than or equal to the min_size
        default: 1
        type: integer
    max_scaleout_adjustment_step:
        description:
            - Maximum number of servers to scaleout simultaneously. The actual number of servers to scaleout is chosen such that target number of servers is always less than or equal to the max_size
        default: 1
        type: integer
    max_size:
        description:
            - Maximum number of servers after scaleout
        type: integer
    min_size:
        description:
            - No scale-in happens once number of operationally up servers reach min_servers
        type: integer
    name:
        description:
            - Not present.
        required: true
        type: string
    scalein_alertconfig_refs:
        description:
            - Trigger scalein when alerts due to any of these Alert configurations are raised object ref AlertConfig.
        type: string
    scalein_cooldown:
        description:
            - Cooldown period during which no new scalein is triggered to allow previous scalein to successfully complete
        default: 300
        type: integer
    scaleout_alertconfig_refs:
        description:
            - Trigger scaleout when alerts due to any of these Alert configurations are raised object ref AlertConfig.
        type: string
    scaleout_cooldown:
        description:
            - Cooldown period during which no new scaleout is triggered to allow previous scaleout to successfully complete
        default: 300
        type: integer
    tenant_ref:
        description:
            - Not present. object ref Tenant.
        type: string
    url:
        description:
            - url
        required: true
        type: string
    use_predicted_load:
        description:
            - Use predicted load rather than current load
        default: False
        type: bool
    uuid:
        description:
            - Not present.
        type: string
'''

RETURN = '''
obj:
    description: ServerAutoScalePolicy (api/serverautoscalepolicy) object
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
                description=dict(
                    type='str',
                    ),
                intelligent_autoscale=dict(
                    type='bool',
                    ),
                intelligent_scalein_margin=dict(
                    type='int',
                    ),
                intelligent_scaleout_margin=dict(
                    type='int',
                    ),
                max_scalein_adjustment_step=dict(
                    type='int',
                    ),
                max_scaleout_adjustment_step=dict(
                    type='int',
                    ),
                max_size=dict(
                    type='int',
                    ),
                min_size=dict(
                    type='int',
                    ),
                name=dict(
                    type='str',
                    ),
                scalein_alertconfig_refs=dict(
                    type='list',
                    ),
                scalein_cooldown=dict(
                    type='int',
                    ),
                scaleout_alertconfig_refs=dict(
                    type='list',
                    ),
                scaleout_cooldown=dict(
                    type='int',
                    ),
                tenant_ref=dict(
                    type='str',
                    ),
                url=dict(
                    type='str',
                    ),
                use_predicted_load=dict(
                    type='bool',
                    ),
                uuid=dict(
                    type='str',
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
                    'serverautoscalepolicy', name,
                    tenant=tenant, tenant_uuid=tenant_uuid)
            except ObjectNotFound:
                return module.exit_json(changed=False)
            if rsp.status_code == 204:
                return module.exit_json(changed=True)
            return module.fail_json(msg=rsp.text)
        existing_obj = api.get_object_by_name(
                'serverautoscalepolicy', name,
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
                    'serverautoscalepolicy/%s' % obj_uuid, data=obj,
                    tenant=tenant, tenant_uuid=tenant_uuid)
        else:
            changed = True
            rsp = api.post('serverautoscalepolicy', data=obj,
                           tenant=tenant, tenant_uuid=tenant_uuid)
        if rsp is None:
            return module.exit_json(changed=changed, obj=existing_obj)
        else:
            return ansible_return(module, rsp, changed)
    except:
        raise


if __name__ == '__main__':
    main()