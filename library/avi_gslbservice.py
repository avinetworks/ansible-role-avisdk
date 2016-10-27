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
- code: 'avi_gslbservice controller=10.10.25.42 username=admin '
            ' password=something'
            ' state=present name=sample_gslbservice'
description: "Adds/Deletes GslbService configuration from Avi Controller."
"""

DOCUMENTATION = '''
---
module: avi_gslbservice
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: GslbService Configuration
description:
    - This module is used to configure GslbService object
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
    controller_health_status_enabled:
        description:
            - GS member's overall health status is derived based on a combination of controller and datapath health-status inputs. Datapath status is determined by the association of health monitor profiles, while the controller provided status is determined through this configuration. 
        default: True
        type: bool
    domain_names:
        description:
            - Fully qualified domain name of the Gslb Service.
        type: string
    down_response:
        description:
            - Response to the client query when the Gslb Service is DOWN.
        type: GslbServiceDownResponse
    enabled:
        description:
            - Enable or disable the Gslb Service. If the Gslb Service is enabled, then the VIPs are sent in the DNS responses based on reachability and configured algorithm. If the Gslb Service is disabled, then the VIPs are no longer available in the DNS response.
        default: True
        type: bool
    groups:
        description:
            - Select list of pools belonging to this Gslb Service.
        type: GslbPool
    health_monitor_refs:
        description:
            - Verify VS health by applying one or more health monitors.  Active monitors generate synthetic traffic from DNS Service Engine and to mark a VS up or down based on the response.  object ref GslbHealthMonitor.
        type: string
    health_monitor_scope:
        description:
            - Health monitor probe can be executed for all the members or it can be executed only for Non-Avi members. This operational mode is useful to reduce the number of health monitor probes in case of a hybrid scenario where Avi members can have controller derived status while Non-Avi members can be probed by via health monitor probes in dataplane.
        default: 1
        type: string
    name:
        description:
            - Name for the Gslb Service.
        required: true
        type: string
    num_dns_ip:
        description:
            - Number of IP addresses of this Gslb Service to be returned by the DNS Service. Enter 0 to return all IP addresses.
        type: integer
    tenant_ref:
        description:
            - Not present. object ref Tenant.
        type: string
    ttl:
        description:
            - TTL value in seconds for A records for this Gslb Service served by the DNS Service.
        type: integer
    url:
        description:
            - url
        required: true
        type: string
    uuid:
        description:
            - UUID of the Gslb Service.
        type: string
'''

RETURN = '''
obj:
    description: GslbService (api/gslbservice) object
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
                controller_health_status_enabled=dict(
                    type='bool',
                    ),
                domain_names=dict(
                    type='list',
                    ),
                down_response=dict(
                    type='dict',
                    ),
                enabled=dict(
                    type='bool',
                    ),
                groups=dict(
                    type='list',
                    ),
                health_monitor_refs=dict(
                    type='list',
                    ),
                health_monitor_scope=dict(
                    type='str',
                    ),
                name=dict(
                    type='str',
                    ),
                num_dns_ip=dict(
                    type='int',
                    ),
                tenant_ref=dict(
                    type='str',
                    ),
                ttl=dict(
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
        return avi_ansible_api(module, 'gslbservice',
                               set([]))
    except:
        raise


if __name__ == '__main__':
    main()