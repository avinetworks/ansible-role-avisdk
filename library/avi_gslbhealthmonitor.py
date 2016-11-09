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
- code: 'avi_gslbhealthmonitor controller=10.10.25.42 username=admin '
            ' password=something'
            ' state=present name=sample_gslbhealthmonitor'
description: "Adds/Deletes GslbHealthMonitor configuration from Avi Controller."
"""

DOCUMENTATION = '''
---
module: avi_gslbhealthmonitor
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: GslbHealthMonitor Configuration
description:
    - This module is used to configure GslbHealthMonitor object
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
    description: GslbHealthMonitor (api/gslbhealthmonitor) object
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
                description=dict(
                    type='str',
                    ),
                dns_monitor=dict(
                    type='dict',
                    ),
                external_monitor=dict(
                    type='dict',
                    ),
                failed_checks=dict(
                    type='int',
                    ),
                http_monitor=dict(
                    type='dict',
                    ),
                https_monitor=dict(
                    type='dict',
                    ),
                monitor_port=dict(
                    type='int',
                    ),
                name=dict(
                    type='str',
                    ),
                receive_timeout=dict(
                    type='int',
                    ),
                send_interval=dict(
                    type='int',
                    ),
                successful_checks=dict(
                    type='int',
                    ),
                tcp_monitor=dict(
                    type='dict',
                    ),
                tenant_ref=dict(
                    type='str',
                    ),
                type=dict(
                    type='str',
                    ),
                udp_monitor=dict(
                    type='dict',
                    ),
                url=dict(
                    type='str',
                    ),
                uuid=dict(
                    type='str',
                    ),
                ),
        )
        return avi_ansible_api(module, 'gslbhealthmonitor',
                               set([]))
    except:
        raise


if __name__ == '__main__':
    main()