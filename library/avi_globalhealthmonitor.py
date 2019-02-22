#!/usr/bin/python
#
# Created on Aug 25, 2016
# @author: Gaurav Rastogi (grastogi@avinetworks.com) GitHub ID: grastogi23
#
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
from avi.sdk.avi_api import ApiSession, ObjectNotFound, AviCredentials
from avi.sdk.utils.ansible_utils import (ansible_return, purge_optional_fields,
                                         avi_obj_cmp, cleanup_absent_fields, avi_common_argument_spec)

EXAMPLES = """
- code: 'avi_globalhealthmonitor controller=10.10.25.42 username=admin '
            ' password=something'
            ' state=present name=sample_globalhealthmonitor'
description: "Adds/Deletes GlobalHealthMonitor configuration from Avi Controller."
"""

DOCUMENTATION = '''
---
module: avi_globalhealthmonitor
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: GlobalHealthMonitor Configuration
description:
    - This module is used to configure GlobalHealthMonitor object
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
    dns_monitor:
        description:
            - Not present.
        type: HealthMonitorDNS
    external_monitor:
        description:
            - Not present.
        type: HealthMonitorExternal
    failed_checks:
        description:
            - Number of continuous failed health checks before the server is marked down.
        default: 2
        type: integer
    http_monitor:
        description:
            - Not present.
        type: HealthMonitorHttp
    https_monitor:
        description:
            - Not present.
        type: HealthMonitorHttp
    monitor_port:
        description:
            - Use this port instead of the port defined for the server in the Pool. If the monitor succeeds to this port, the load balanced traffic will still be sent to the port of the server defined within the Pool.
        type: integer
    name:
        description:
            - A user friendly name for this health monitor.
        required: true
        type: string
    receive_timeout:
        description:
            - A valid response from the server is expected within the receive timeout window.  This timeout must be less than the send interval.  If server status is regularly flapping up and down, consider increasing this value.
        default: 4
        type: integer
    send_interval:
        description:
            - Frequency, in seconds, that monitors are sent to a server.
        default: 5
        type: integer
    successful_checks:
        description:
            - Number of continuous successful health checks before server is marked up.
        default: 2
        type: integer
    tcp_monitor:
        description:
            - Not present.
        type: HealthMonitorTcp
    tenant_ref:
        description:
            - Not present. object ref Tenant.
        type: string
    type:
        description:
            - Type of the health monitor.
        required: true
        type: string
    udp_monitor:
        description:
            - Not present.
        type: HealthMonitorUdp
    url:
        description:
            - url
        required: true
        type: string
    uuid:
        description:
            - UUID of the health monitor.
        type: string
'''

RETURN = '''
obj:
    description: GlobalHealthMonitor (api/globalhealthmonitor) object
    returned: success, changed
    type: dict
'''


def main():
    argument_specs = dict(
        controller=dict(required=True),
        username=dict(required=True),
        password=dict(required=True),
        tenant=dict(default='admin'),
        tenant_uuid=dict(default=''),
        state=dict(default='present',
                   choices=['absent', 'present']),
        description=dict(type='str',),
        dns_monitor=dict(type='dict',),
        external_monitor=dict(type='dict',),
        failed_checks=dict(type='int',),
        http_monitor=dict(type='dict',),
        https_monitor=dict(type='dict',),
        monitor_port=dict(type='int',),
        name=dict(type='str',),
        receive_timeout=dict(type='int',),
        send_interval=dict(type='int',),
        successful_checks=dict(type='int',),
        tcp_monitor=dict(type='dict',),
        tenant_ref=dict(type='str',),
        type=dict(type='str',),
        udp_monitor=dict(type='dict',),
        url=dict(type='str',),
        uuid=dict(type='str',),
    ),
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(argument_spec=argument_specs)
    api_creds = AviCredentials()
    api_creds.update_from_ansible_module(module)
    api = ApiSession.get_session(
        module.params['controller'],
        module.params['username'],
        module.params['password'],
        tenant=module.params['tenant'],
        idp=api_creds.idp,
    )
    state = module.params['state']
    name = module.params['name']

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
                'globalhealthmonitor', name,
                tenant=tenant, tenant_uuid=tenant_uuid)
        except ObjectNotFound:
            return module.exit_json(changed=False)
        if rsp.status_code == 204:
            return module.exit_json(changed=True)
        return module.fail_json(msg=rsp.text)
    existing_obj = api.get_object_by_name(
        'globalhealthmonitor', name,
        tenant=tenant, tenant_uuid=tenant_uuid,
        params={'include_refs': '', 'include_name': ''})
    changed = False
    rsp = None
    if existing_obj:
        # this is case of modify as object exists. should find out
        # if changed is true or not
        changed = not avi_obj_cmp(obj, existing_obj)
        cleanup_absent_fields(obj)
        if changed:
            obj_uuid = existing_obj['uuid']
            rsp = api.put(
                'globalhealthmonitor/%s' % obj_uuid, data=obj,
                tenant=tenant, tenant_uuid=tenant_uuid)
    else:
        changed = True
        rsp = api.post('globalhealthmonitor', data=obj,
                       tenant=tenant, tenant_uuid=tenant_uuid)
    if rsp is None:
        return module.exit_json(changed=changed, obj=existing_obj)
    else:
        return ansible_return(module, rsp, changed)


if __name__ == '__main__':
    main()