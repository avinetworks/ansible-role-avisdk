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


EXAMPLES = '''
- avi_pool:
    controller: 10.10.1.20
    username: avi_user
    password: avi_password
    name: testpool1
    description: testpool1
    state: present
    health_monitor_refs:
        - '/api/healthmonitor?name=System-HTTP'
    servers:
        - ip:
            addr: 10.10.2.20
            type: V4
        - ip:
            addr: 10.10.2.21
            type: V4
'''
DOCUMENTATION = '''
---
module: avi_pool
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: Pool Configuration
description:
    - This module is used to configure Pool object
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
    a_pool:
        description:
            - Name of container cloud application that constitutes A pool in a A-B pool configuration, if different from VS app
        type: string
    ab_pool:
        description:
            - A/B pool configuration.
        type: AbPool
    ab_priority:
        description:
            - Priority of this pool in a A-B pool pair. Internally used
        type: integer
    apic_epg_name:
        description:
            - Synchronize Cisco APIC EPG members with pool servers
        type: string
    application_persistence_profile_ref:
        description:
            - Persistence will ensure the same user sticks to the same server for a desired duration of time. object ref ApplicationPersistenceProfile.
        type: string
    autoscale_launch_config_ref:
        description:
            - Reference to the Launch Configuration Profile object ref AutoScaleLaunchConfig.
        type: string
    autoscale_networks:
        description:
            - Network Ids for the launch configuration
        type: string
    autoscale_policy_ref:
        description:
            - Reference to Server Autoscale Policy object ref ServerAutoScalePolicy.
        type: string
    capacity_estimation:
        description:
            - Inline estimation of capacity of servers.
        default: False
        type: bool
    capacity_estimation_ttfb_thresh:
        description:
            - The maximum time-to-first-byte of a server.
        default: 0
        type: integer
    cloud_config_cksum:
        description:
            - Checksum of cloud configuration for Pool. Internally set by cloud connector
        type: string
    cloud_ref:
        description:
            - Not present. object ref Cloud.
        default: Default-Cloud
        type: string
    connection_ramp_duration:
        description:
            - Duration for which new connections will be gradually ramped up to a server recently brought online.  Useful for LB algorithms that are least connection based.
        default: 10
        type: integer
    created_by:
        description:
            - Creator name
        type: string
    default_server_port:
        description:
            - Traffic sent to servers will use this destination server port unless overridden by the server's specific port attribute. The SSL checkbox enables Avi to server encryption.
        default: 80
        type: integer
    description:
        description:
            - A description of the pool.
        type: string
    domain_name:
        description:
            - Comma separated list of domain names which will be used to verify the common names or subject alternative names presented by server certificates if common name check (host_check_enabled) is enabled.
        type: string
    east_west:
        description:
            - Inherited config from VirtualService.
        type: bool
    enabled:
        description:
            - Enable or disable the pool.  Disabling will terminate all open connections and pause health monitors.
        default: True
        type: bool
    fail_action:
        description:
            - Enable an action - Close Connection, HTTP Redirect, Local HTTP Response, or Backup Pool - when a pool failure happens. By default, a connection will be closed, in case the pool experiences a failure.
        type: FailAction
    fewest_tasks_feedback_delay:
        description:
            - Periodicity of feedback for fewest tasks server selection algorithm.
        default: 10
        type: integer
    graceful_disable_timeout:
        description:
            - Used to gracefully disable a server. Virtual service waits for the specified time before terminating the existing connections  to the servers that are disabled.
        default: 1
        type: integer
    health_monitor_refs:
        description:
            - Verify server health by applying one or more health monitors.  Active monitors generate synthetic traffic from each Service Engine and mark a server up or down based on the response. The Passive monitor listens to client to server communication and raises or lowers the ratio of traffic destined to a server based on successful responses. object ref HealthMonitor.
        type: string
    host_check_enabled:
        description:
            - Enable common name check for server certificate. If enabled and no explicit domain name is specified, Avi will use the incoming host header to do the match.
        default: False
        type: bool
    inline_health_monitor:
        description:
            - The Passive monitor will monitor client to server connections and requests and adjust traffic load to servers based on successful responses.  This may alter the expected behavior of the LB method, such as Round Robin.
        default: True
        type: bool
    ipaddrgroup_ref:
        description:
            - Use list of servers from Ip Address Group object ref IpAddrGroup.
        type: string
    lb_algorithm:
        description:
            - The load balancing algorithm will pick a server within the pool's list of available servers.
        default: 1
        type: string
    lb_algorithm_consistent_hash_hdr:
        description:
            - HTTP header name to be used for the hash key.
        type: string
    lb_algorithm_hash:
        description:
            - Criteria used as a key for determining the hash between the client and  server.
        default: 1
        type: string
    max_concurrent_connections_per_server:
        description:
            - The maximum number of concurrent connections allowed to each server within the pool.
        default: 0
        type: integer
    max_conn_rate_per_server:
        description:
            - Rate Limit connections to each server.
        type: RateProfile
    name:
        description:
            - The name of the pool.
        required: true
        type: string
    networks:
        description:
            - (internal-use) Networks designated as containing servers for this pool.  The servers may be further narrowed down by a filter. This field is used internally by Avi, not editable by the user.
        type: NetworkFilter
    pki_profile_ref:
        description:
            - Avi will validate the SSL certificate present by a server against the selected PKI Profile. object ref PKIProfile.
        type: string
    placement_networks:
        description:
            - Manually select the networks and subnets used to provide reachability to the pool's servers.  Specify the Subnet using the following syntax  10.1.1.0/24. If the Pool Servers are not directly connected, but routable from the ServiceEngine, please also provide the appropriate static routes to reach the Servers in the VRF configuration.
        type: PlacementNetwork
    prst_hdr_name:
        description:
            - Header name for custom header persistence
        type: string
    request_queue_depth:
        description:
            - Minimum number of requests to be queued when pool is full.
        default: 128
        type: integer
    request_queue_enabled:
        description:
            - Enable request queue when pool is full
        default: False
        type: bool
    rewrite_host_header_to_server_name:
        description:
            - Rewrite incoming Host Header to server name of the server to which the request is proxied.  Enabling this feature rewrites Host Header for requests to all servers in the pool.
        default: False
        type: bool
    rewrite_host_header_to_sni:
        description:
            - If SNI server name is specified, rewrite incoming host header to the SNI server name.
        default: False
        type: bool
    server_auto_scale:
        description:
            - Server AutoScale. Not used anymore.
        default: False
        type: bool
    server_count:
        description:
            - Not present.
        default: 0
        type: integer
    server_name:
        description:
            - Fully qualified DNS hostname which will be used in the TLS SNI extension in server connections if SNI is enabled. If no value is specified, Avi will use the incoming host header instead.
        type: string
    server_reselect:
        description:
            - Server reselect configuration for HTTP requests.
        type: HTTPServerReselect
    servers:
        description:
            - The pool directs load balanced traffic to this list of destination servers. The servers can be configured by IP address, name, network or via IP Address Group
        type: Server
    sni_enabled:
        description:
            - Enable TLS SNI for server connections. If disabled, Avi will not send the SNI extension as part of the handshake.
        default: True
        type: bool
    ssl_key_and_certificate_ref:
        description:
            - Service Engines will present a client SSL certificate to the server. object ref SSLKeyAndCertificate.
        type: string
    ssl_profile_ref:
        description:
            - When enabled, Avi re-encrypts traffic to the backend servers. The specific SSL profile defines which ciphers and SSL versions will be supported. object ref SSLProfile.
        type: string
    tenant_ref:
        description:
            - Not present. object ref Tenant.
        type: string
    url:
        description:
            - url
        required: true
        type: string
    use_service_port:
        description:
            - Do not translate the client's destination port when sending the connection to the server.  The pool or servers specified service port will still be used for health monitoring.  This feature is only applicable for a Virtual Service configured with the application type set to L4.
        default: False
        type: bool
    uuid:
        description:
            - UUID of the pool
        type: string
    vrf_ref:
        description:
            - Virtual Routing Context that the pool is bound to. This is used to provide the isolation of the set of networks the pool is attached to. The pool inherits the Virtual Routing Conext of the Virtual Service, and this field is used only internally, and is set by pb-transform. object ref VrfContext.
        type: string
'''

RETURN = '''
obj:
    description: Pool (api/pool) object
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
                a_pool=dict(
                    type='str',
                    ),
                ab_pool=dict(
                    type='dict',
                    ),
                ab_priority=dict(
                    type='int',
                    ),
                apic_epg_name=dict(
                    type='str',
                    ),
                application_persistence_profile_ref=dict(
                    type='str',
                    ),
                autoscale_launch_config_ref=dict(
                    type='str',
                    ),
                autoscale_networks=dict(
                    type='list',
                    ),
                autoscale_policy_ref=dict(
                    type='str',
                    ),
                capacity_estimation=dict(
                    type='bool',
                    ),
                capacity_estimation_ttfb_thresh=dict(
                    type='int',
                    ),
                cloud_config_cksum=dict(
                    type='str',
                    ),
                cloud_ref=dict(
                    type='str',
                    ),
                connection_ramp_duration=dict(
                    type='int',
                    ),
                created_by=dict(
                    type='str',
                    ),
                default_server_port=dict(
                    type='int',
                    ),
                description=dict(
                    type='str',
                    ),
                domain_name=dict(
                    type='list',
                    ),
                east_west=dict(
                    type='bool',
                    ),
                enabled=dict(
                    type='bool',
                    ),
                fail_action=dict(
                    type='dict',
                    ),
                fewest_tasks_feedback_delay=dict(
                    type='int',
                    ),
                graceful_disable_timeout=dict(
                    type='int',
                    ),
                health_monitor_refs=dict(
                    type='list',
                    ),
                host_check_enabled=dict(
                    type='bool',
                    ),
                inline_health_monitor=dict(
                    type='bool',
                    ),
                ipaddrgroup_ref=dict(
                    type='str',
                    ),
                lb_algorithm=dict(
                    type='str',
                    ),
                lb_algorithm_consistent_hash_hdr=dict(
                    type='str',
                    ),
                lb_algorithm_hash=dict(
                    type='str',
                    ),
                max_concurrent_connections_per_server=dict(
                    type='int',
                    ),
                max_conn_rate_per_server=dict(
                    type='dict',
                    ),
                name=dict(
                    type='str',
                    ),
                networks=dict(
                    type='list',
                    ),
                pki_profile_ref=dict(
                    type='str',
                    ),
                placement_networks=dict(
                    type='list',
                    ),
                prst_hdr_name=dict(
                    type='str',
                    ),
                request_queue_depth=dict(
                    type='int',
                    ),
                request_queue_enabled=dict(
                    type='bool',
                    ),
                rewrite_host_header_to_server_name=dict(
                    type='bool',
                    ),
                rewrite_host_header_to_sni=dict(
                    type='bool',
                    ),
                server_auto_scale=dict(
                    type='bool',
                    ),
                server_count=dict(
                    type='int',
                    ),
                server_name=dict(
                    type='str',
                    ),
                server_reselect=dict(
                    type='dict',
                    ),
                servers=dict(
                    type='list',
                    ),
                sni_enabled=dict(
                    type='bool',
                    ),
                ssl_key_and_certificate_ref=dict(
                    type='str',
                    ),
                ssl_profile_ref=dict(
                    type='str',
                    ),
                tenant_ref=dict(
                    type='str',
                    ),
                url=dict(
                    type='str',
                    ),
                use_service_port=dict(
                    type='bool',
                    ),
                uuid=dict(
                    type='str',
                    ),
                vrf_ref=dict(
                    type='str',
                    ),
                ),
        )
        return avi_ansible_api(module, 'pool',
                               set([]))
    except:
        raise


if __name__ == '__main__':
    main()