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
- code: 'avi_controllerproperties controller=10.10.25.42 username=admin '
            ' password=something'
            ' state=present name=sample_controllerproperties'
description: "Adds/Deletes ControllerProperties configuration from Avi Controller."
"""

DOCUMENTATION = '''
---
module: avi_controllerproperties
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: ControllerProperties Configuration
description:
    - This module is used to configure ControllerProperties object
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
    allow_unauthenticated_apis:
        description:
            - Allow unauthenticated access for special APIs
        default: False
        type: bool
    allow_unauthenticated_nodes:
        description:
            - Not present.
        default: False
        type: bool
    api_idle_timeout:
        description:
            - Not present.
        default: 15
        type: integer
    attach_ip_retry_interval:
        description:
            - Not present.
        default: 360
        type: integer
    attach_ip_retry_limit:
        description:
            - Not present.
        default: 4
        type: integer
    cluster_ip_gratuitous_arp_period:
        description:
            - Not present.
        default: 60
        type: integer
    crashed_se_reboot:
        description:
            - Not present.
        default: 900
        type: integer
    dead_se_detection_timer:
        description:
            - Not present.
        default: 360
        type: integer
    dns_refresh_period:
        description:
            - Not present.
        default: 60
        type: integer
    dummy:
        description:
            - Not present.
        type: integer
    fatal_error_lease_time:
        description:
            - Not present.
        default: 120
        type: integer
    max_dead_se_in_grp:
        description:
            - Not present.
        default: 1
        type: integer
    max_pcap_per_tenant:
        description:
            - Maximum number of pcap files stored per tenant
        default: 4
        type: integer
    max_seq_vnic_failures:
        description:
            - Not present.
        default: 3
        type: integer
    persistence_key_rotate_period:
        description:
            - Not present.
        default: 60
        type: integer
    query_host_fail:
        description:
            - Not present.
        default: 180
        type: integer
    se_create_timeout:
        description:
            - Not present.
        default: 900
        type: integer
    se_failover_attempt_interval:
        description:
            - Interval between attempting failovers to an SE
        default: 300
        type: integer
    se_offline_del:
        description:
            - Not present.
        default: 172000
        type: integer
    se_vnic_cooldown:
        description:
            - Not present.
        default: 120
        type: integer
    secure_channel_cleanup_timeout:
        description:
            - Not present.
        default: 60
        type: integer
    secure_channel_controller_token_timeout:
        description:
            - Not present.
        default: 60
        type: integer
    secure_channel_se_token_timeout:
        description:
            - Not present.
        default: 60
        type: integer
    seupgrade_fabric_pool_size:
        description:
            - Not present.
        default: 20
        type: integer
    seupgrade_segroup_min_dead_timeout:
        description:
            - Not present.
        default: 360
        type: integer
    ssl_certificate_expiry_warning_days:
        description:
            - Number of days for SSL Certificate expiry warning
        type: integer
    unresponsive_se_reboot:
        description:
            - Not present.
        default: 300
        type: integer
    upgrade_lease_time:
        description:
            - Not present.
        default: 360
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
    vnic_op_fail_time:
        description:
            - Not present.
        default: 180
        type: integer
    vs_apic_scaleout_timeout:
        description:
            - Time to wait for the scaled out SE to become ready before marking the scaleout done, applies to APIC configuration only
        default: 360
        type: integer
    vs_awaiting_se_timeout:
        description:
            - Not present.
        default: 60
        type: integer
    vs_key_rotate_period:
        description:
            - Not present.
        default: 60
        type: integer
    vs_se_bootup_fail:
        description:
            - Not present.
        default: 300
        type: integer
    vs_se_create_fail:
        description:
            - Not present.
        default: 1500
        type: integer
    vs_se_ping_fail:
        description:
            - Not present.
        default: 60
        type: integer
    vs_se_vnic_fail:
        description:
            - Not present.
        default: 300
        type: integer
    vs_se_vnic_ip_fail:
        description:
            - Not present.
        default: 120
        type: integer
    warmstart_se_reconnect_wait_time:
        description:
            - Not present.
        default: 300
        type: integer
'''

RETURN = '''
obj:
    description: ControllerProperties (api/controllerproperties) object
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
                allow_unauthenticated_apis=dict(
                    type='bool',
                    ),
                allow_unauthenticated_nodes=dict(
                    type='bool',
                    ),
                api_idle_timeout=dict(
                    type='int',
                    ),
                attach_ip_retry_interval=dict(
                    type='int',
                    ),
                attach_ip_retry_limit=dict(
                    type='int',
                    ),
                cluster_ip_gratuitous_arp_period=dict(
                    type='int',
                    ),
                crashed_se_reboot=dict(
                    type='int',
                    ),
                dead_se_detection_timer=dict(
                    type='int',
                    ),
                dns_refresh_period=dict(
                    type='int',
                    ),
                dummy=dict(
                    type='int',
                    ),
                fatal_error_lease_time=dict(
                    type='int',
                    ),
                max_dead_se_in_grp=dict(
                    type='int',
                    ),
                max_pcap_per_tenant=dict(
                    type='int',
                    ),
                max_seq_vnic_failures=dict(
                    type='int',
                    ),
                persistence_key_rotate_period=dict(
                    type='int',
                    ),
                query_host_fail=dict(
                    type='int',
                    ),
                se_create_timeout=dict(
                    type='int',
                    ),
                se_failover_attempt_interval=dict(
                    type='int',
                    ),
                se_offline_del=dict(
                    type='int',
                    ),
                se_vnic_cooldown=dict(
                    type='int',
                    ),
                secure_channel_cleanup_timeout=dict(
                    type='int',
                    ),
                secure_channel_controller_token_timeout=dict(
                    type='int',
                    ),
                secure_channel_se_token_timeout=dict(
                    type='int',
                    ),
                seupgrade_fabric_pool_size=dict(
                    type='int',
                    ),
                seupgrade_segroup_min_dead_timeout=dict(
                    type='int',
                    ),
                ssl_certificate_expiry_warning_days=dict(
                    type='list',
                    ),
                unresponsive_se_reboot=dict(
                    type='int',
                    ),
                upgrade_lease_time=dict(
                    type='int',
                    ),
                url=dict(
                    type='str',
                    ),
                uuid=dict(
                    type='str',
                    ),
                vnic_op_fail_time=dict(
                    type='int',
                    ),
                vs_apic_scaleout_timeout=dict(
                    type='int',
                    ),
                vs_awaiting_se_timeout=dict(
                    type='int',
                    ),
                vs_key_rotate_period=dict(
                    type='int',
                    ),
                vs_se_bootup_fail=dict(
                    type='int',
                    ),
                vs_se_create_fail=dict(
                    type='int',
                    ),
                vs_se_ping_fail=dict(
                    type='int',
                    ),
                vs_se_vnic_fail=dict(
                    type='int',
                    ),
                vs_se_vnic_ip_fail=dict(
                    type='int',
                    ),
                warmstart_se_reconnect_wait_time=dict(
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
                    'controllerproperties', name,
                    tenant=tenant, tenant_uuid=tenant_uuid)
            except ObjectNotFound:
                return module.exit_json(changed=False)
            if rsp.status_code == 204:
                return module.exit_json(changed=True)
            return module.fail_json(msg=rsp.text)
        existing_obj = api.get_object_by_name(
                'controllerproperties', name,
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
                    'controllerproperties/%s' % obj_uuid, data=obj,
                    tenant=tenant, tenant_uuid=tenant_uuid)
        else:
            changed = True
            rsp = api.post('controllerproperties', data=obj,
                           tenant=tenant, tenant_uuid=tenant_uuid)
        if rsp is None:
            return module.exit_json(changed=changed, obj=existing_obj)
        else:
            return ansible_return(module, rsp, changed)
    except:
        raise


if __name__ == '__main__':
    main()