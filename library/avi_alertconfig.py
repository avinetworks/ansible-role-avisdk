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
- code: 'avi_alertconfig controller=10.10.25.42 username=admin '
            ' password=something'
            ' state=present name=sample_alertconfig'
description: "Adds/Deletes AlertConfig configuration from Avi Controller."
"""

DOCUMENTATION = '''
---
module: avi_alertconfig
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: AlertConfig Configuration
description:
    - This module is used to configure AlertConfig object
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
    action_group_ref:
        description:
            - The alert config will trigger the selected alert action, which send send notifications or execute custom scripts. object ref ActionGroupConfig.
        type: string
    alert_rule:
        description:
            - list of filters matching on events or client logs used for triggering alerts.
        required: true
        type: AlertRule
    autoscale_alert:
        description:
            - This alert config applies to auto scale alerts
        type: bool
    category:
        description:
            - Determines whether an alert is raised as soon as the event occurs (Realtime) or the Controller should wait until the specified number of events has occured in the rolling window's time interval.
        required: true
        type: string
    description:
        description:
            - A custom description field.
        type: string
    enabled:
        description:
            - Enable or disable this alert config from generating new alerts.
        default: True
        type: bool
    expiry_time:
        description:
            - An alert is expired and deleted after the expiry time has elapsed.  The original event triggering the alert remains in the event's log.
        default: 86400
        type: integer
    name:
        description:
            - Name of the alert configuration
        required: true
        type: string
    obj_uuid:
        description:
            - UUID of the resource for which alert was raised
        type: string
    recommendation:
        description:
            - Not present
        type: string
    rolling_window:
        description:
            - Only if the Number of Events is reached or exceeded within the Time Window will an alert be generated.
        default: 300
        type: integer
    source:
        description:
            - Signifies system events or the type of client logsused in this alert configuration
        required: true
        type: string
    summary:
        description:
            - Summary of reason why alert is generated
        type: string
    tenant_ref:
        description:
            - Not present. object ref Tenant.
        type: string
    threshold:
        description:
            - An alert is created only when the number of events meets or exceeds this number within the chosen time frame.
        default: 1
        type: integer
    throttle:
        description:
            - Alerts are suppressed (throttled) for this duration of time since the last alert was raised for this alert config.
        default: 600
        type: integer
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
    description: AlertConfig (api/alertconfig) object
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
                action_group_ref=dict(
                    type='str',
                    ),
                alert_rule=dict(
                    type='dict',
                    ),
                autoscale_alert=dict(
                    type='bool',
                    ),
                category=dict(
                    type='str',
                    ),
                description=dict(
                    type='str',
                    ),
                enabled=dict(
                    type='bool',
                    ),
                expiry_time=dict(
                    type='int',
                    ),
                name=dict(
                    type='str',
                    ),
                obj_uuid=dict(
                    type='str',
                    ),
                recommendation=dict(
                    type='str',
                    ),
                rolling_window=dict(
                    type='int',
                    ),
                source=dict(
                    type='str',
                    ),
                summary=dict(
                    type='str',
                    ),
                tenant_ref=dict(
                    type='str',
                    ),
                threshold=dict(
                    type='int',
                    ),
                throttle=dict(
                    type='int',
                    ),
                url=dict(
                    type='str',
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
                    'alertconfig', name,
                    tenant=tenant, tenant_uuid=tenant_uuid)
            except ObjectNotFound:
                return module.exit_json(changed=False)
            if rsp.status_code == 204:
                return module.exit_json(changed=True)
            return module.fail_json(msg=rsp.text)
        existing_obj = api.get_object_by_name(
                'alertconfig', name,
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
                    'alertconfig/%s' % obj_uuid, data=obj,
                    tenant=tenant, tenant_uuid=tenant_uuid)
        else:
            changed = True
            rsp = api.post('alertconfig', data=obj,
                           tenant=tenant, tenant_uuid=tenant_uuid)
        if rsp is None:
            return module.exit_json(changed=changed, obj=existing_obj)
        else:
            return ansible_return(module, rsp, changed)
    except:
        raise


if __name__ == '__main__':
    main()