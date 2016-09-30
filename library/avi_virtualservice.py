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


EXAMPLES = '''
- avi_virtualservice:
    controller: 10.10.27.90
    username: admin
    password: AviNetworks123!
    name: newtestvs
    state: present
    performance_limits:
    max_concurrent_connections: 1000
    services:
        - port: 443
          enable_ssl: true
        - port: 80
    ssl_profile_ref: '/api/sslprofile?name=System-Standard'
    application_profile_ref: '/api/applicationprofile?name=System-Secure-HTTP'
    ssl_key_and_certificate_refs:
        - '/api/sslkeyandcertificate?name=System-Default-Cert'
    ip_address:
    addr: 10.90.131.103
    type: V4
    pool_ref: '/api/pool?name=testpool2'
'''
DOCUMENTATION = '''
---
module: avi_virtualservice
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: VirtualService Configuration
description:
    - This module is used to configure VirtualService object
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
    active_standby_se_tag:
        description:
            - This configuration only applies if the VirtualService is in Legacy Active Standby HA mode and Load Distribution among Active Standby is enabled. This field is used to tag the VirtualService so that VirtualServices with the same tag will share the same Active ServiceEngine and VirtualServices with different tags will have different Active ServiceEngines. If one of the ServiceEngine's in the ServiceEngineGroup fails, all VirtualServices will end up using the same Active ServiceEngine. Redistribution of the VirtualServices, once the failed ServiceEngine recovers can either be manual or automated, based on the auto redistribute property of the ServiceEngineGroup
        default: 1
        type: string
    analytics_policy:
        description:
            - Not present.
        type: AnalyticsPolicy
    analytics_profile_ref:
        description:
            - Specifies settings related to analytics. object ref AnalyticsProfile.
        default: System-Analytics-Profile
        type: string
    application_profile_ref:
        description:
            - Enable application layer specific features for the Virtual Service. object ref ApplicationProfile.
        default: System-HTTP
        type: string
    auto_allocate_floating_ip:
        description:
            - Auto-allocate floating/elastic IP from the Cloud infrastructure.
        default: False
        type: bool
    auto_allocate_ip:
        description:
            - Auto-allocate VIP from the provided subnet.
        default: False
        type: bool
    availability_zone:
        description:
            - Availability-zone to place the Virtual Service.
        type: string
    avi_allocated_fip:
        description:
            - (internal-use) FIP allocated by Avi in the Cloud infrastructure.
        default: False
        type: bool
    avi_allocated_vip:
        description:
            - (internal-use) VIP allocated by Avi in the Cloud infrastructure.
        default: False
        type: bool
    client_auth:
        description:
            - HTTP authentication configuration for protected resources.
        type: HTTPClientAuthenticationParams
    cloud_config_cksum:
        description:
            - Checksum of cloud configuration for VS. Internally set by cloud connector
        type: string
    cloud_ref:
        description:
            - Not present. object ref Cloud.
        default: Default-Cloud
        type: string
    cloud_type:
        description:
            - Not present.
        default: 0
        type: string
    connections_rate_limit:
        description:
            - Rate limit the incoming connections to this virtual service
        type: RateProfile
    created_by:
        description:
            - Creator name
        type: string
    delay_fairness:
        description:
            - Select the algorithm for QoS fairness.  This determines how multiple Virtual Services sharing the same Service Engines will prioritize traffic over a congested network.
        default: False
        type: bool
    description:
        description:
            - Not present.
        type: string
    discovered_network_ref:
        description:
            - (internal-use) Discovered networks providing reachability for client facing Virtual Service IP. This field is deprecated. object ref Network.
        type: string
    discovered_networks:
        description:
            - (internal-use) Discovered networks providing reachability for client facing Virtual Service IP. This field is used internally by Avi, not editable by the user.
        type: DiscoveredNetwork
    discovered_subnet:
        description:
            - (internal-use) Discovered subnets providing reachability for client facing Virtual Service IP. This field is deprecated.
        type: IpAddrPrefix
    dns_info:
        description:
            - Service discovery specific data including fully qualified domain name, type and Time-To-Live of the DNS record. 'fqdn' field will be ignored if valid records are provided here.
        type: DnsInfo
    east_west_placement:
        description:
            - Force placement on all SE's in service group (Mesos mode only)
        default: False
        type: bool
    enable_autogw:
        description:
            - Response traffic to clients will be sent back to the source MAC address of the connection, rather than statically sent to a default gateway.
        default: True
        type: bool
    enable_rhi:
        description:
            - Enable Route Health Injection using the BGP Config in the vrf context
        type: bool
    enable_rhi_snat:
        description:
            - Enable Route Health Injection for Source NAT'ted floating IP Address using the BGP Config in the vrf context
        type: bool
    enabled:
        description:
            - Enable or disable the Virtual Service.
        default: True
        type: bool
    floating_ip:
        description:
            - Floating IP to associate with this Virtual Service.
        type: IpAddr
    floating_subnet_uuid:
        description:
            - If auto_allocate_floating_ip is True and more than one floating-ip subnets exist, then the subnet for the floating IP address allocation. This field is applicable only if the VirtualService belongs to an OpenStack or AWS cloud, in which case it is mandatory, if auto_allocate_floating_ip is selected.
        type: string
    flow_dist:
        description:
            - Criteria for flow distribution among SEs.
        default: 1
        type: string
    flow_label_type:
        description:
            - Criteria for flow labelling.
        default: 1
        type: string
    fqdn:
        description:
            - DNS resolvable, fully qualified domain name of the virtualservice. If this field is set, 'dns_info' field is ignored.
        type: string
    host_name_xlate:
        description:
            - Translate the host name sent to the servers to this value.  Translate the host name sent from servers back to the value used by the client.
        type: string
    http_policies:
        description:
            - HTTP Policies applied on the data traffic of the Virtual Service
        type: HTTPPolicies
    ign_pool_net_reach:
        description:
            - Ignore Pool servers network reachability constraints for Virtual Service placement.
        default: False
        type: bool
    ip_address:
        description:
            - IP Address of the Virtual Service.
        type: IpAddr
    ipam_network_subnet:
        description:
            - Subnet and/or Network for allocating VirtualService IP by IPAM Provider module.
        type: IPNetworkSubnet
    limit_doser:
        description:
            - Limit potential DoS attackers who exceed max_cps_per_client significantly to a fraction of max_cps_per_client for a while.
        default: False
        type: bool
    max_cps_per_client:
        description:
            - Maximum connections per second per client IP.
        default: 0
        type: integer
    microservice_ref:
        description:
            - Microservice representing the virtual service object ref MicroService.
        type: string
    name:
        description:
            - Name for the Virtual Service.
        required: true
        type: string
    network_profile_ref:
        description:
            - Determines network settings such as protocol, TCP or UDP, and related options for the protocol. object ref NetworkProfile.
        default: System-TCP-Proxy
        type: string
    network_ref:
        description:
            - Manually override the network on which the Virtual Service is placed. object ref Network.
        type: string
    network_security_policy_ref:
        description:
            - Network security policies for the Virtual Service. object ref NetworkSecurityPolicy.
        type: string
    performance_limits:
        description:
            - Not present.
        type: PerformanceLimits
    pool_group_ref:
        description:
            - The pool group is an object that contains pools. object ref PoolGroup.
        type: string
    pool_ref:
        description:
            - The pool is an object that contains destination servers and related attributes such as load-balancing and persistence. object ref Pool.
        type: string
    port_uuid:
        description:
            - (internal-use) Network port assigned to the Virtual Service IP address.
        type: string
    remove_listening_port_on_vs_down:
        description:
            - Remove listening port if VirtualService is down
        default: False
        type: bool
    requests_rate_limit:
        description:
            - Rate limit the incoming requests to this virtual service
        type: RateProfile
    scaleout_ecmp:
        description:
            - Not present.
        default: False
        type: bool
    se_group_ref:
        description:
            - The Service Engine Group to use for this Virtual Service. Moving to a new SE Group is disruptive to existing connection for this VS. object ref ServiceEngineGroup.
        type: string
    server_network_profile_ref:
        description:
            - Determines the network settings profile for the server side of TCP proxied connections.  Leave blank to use the same settings as the client to VS side of the connection. object ref NetworkProfile.
        type: string
    service_pool_select:
        description:
            - Select pool based on destination port
        type: ServicePoolSelector
    services:
        description:
            - Not present.
        type: Service
    snat_ip:
        description:
            - NAT'ted floating source IP Address(es) for upstream connection to servers
        type: IpAddr
    ssl_key_and_certificate_refs:
        description:
            - Select or create one or two certificates, EC and/or RSA, that will be presented to SSL/TLS terminated connections. object ref SSLKeyAndCertificate.
        type: string
    ssl_profile_ref:
        description:
            - Determines the set of SSL versions and ciphers to accept for SSL/TLS terminated connections. object ref SSLProfile.
        type: string
    ssl_sess_cache_avg_size:
        description:
            - Expected number of SSL session cache entries (may be exceeded).
        default: 1024
        type: integer
    static_dns_records:
        description:
            - List of static DNS records applied to this Virtual Service. These are static entries and no health monitoring is performed against the IP addresses.
        type: DnsRecord
    subnet:
        description:
            - Subnet providing reachability for client facing Virtual Service IP.
        type: IpAddrPrefix
    subnet_uuid:
        description:
            - If auto_allocate_ip is True, then the subnet for the Virtual Service IP address allocation. This field is applicable only if the VirtualService belongs to an OpenStack or AWS cloud, in which case it is mandatory, if auto_allocate is selected.
        type: string
    tenant_ref:
        description:
            - Not present. object ref Tenant.
        type: string
    type:
        description:
            - Specify if this is a normal Virtual Service, or if it is the parent or child of an SNI-enabled virtual hosted Virtual Service.
        default: 1
        type: string
    url:
        description:
            - url
        required: true
        type: string
    use_bridge_ip_as_vip:
        description:
            - Use Bridge IP as VIP on each Host in Mesos deployments
        default: False
        type: bool
    uuid:
        description:
            - UUID of the VirtualService.
        type: string
    vh_domain_name:
        description:
            - The exact name requested from the client's SNI-enabled TLS hello domain name field. If this is a match, the parent VS will forward the connection to this child VS.
        type: string
    vh_parent_vs_uuid:
        description:
            - Specifies the Virtual Service acting as Virtual Hosting (SNI) parent.
        type: string
    vrf_context_ref:
        description:
            - Virtual Routing Context that the Virtual Service is bound to. This is used to provide the isolation of the set of networks the application is attached to. object ref VrfContext.
        type: string
    vs_datascripts:
        description:
            - Datascripts applied on the data traffic of the Virtual Service
        type: VSDataScripts
    weight:
        description:
            - The Quality of Service weight to assign to traffic transmitted from this Virtual Service.  A higher weight will prioritize traffic versus other Virtual Services sharing the same Service Engines. (1-2-4-8)
        default: 1
        type: integer
'''

RETURN = '''
obj:
    description: VirtualService (api/virtualservice) object
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
                active_standby_se_tag=dict(
                    type='str',
                    ),
                analytics_policy=dict(
                    type='dict',
                    ),
                analytics_profile_ref=dict(
                    type='str',
                    ),
                application_profile_ref=dict(
                    type='str',
                    ),
                auto_allocate_floating_ip=dict(
                    type='bool',
                    ),
                auto_allocate_ip=dict(
                    type='bool',
                    ),
                availability_zone=dict(
                    type='str',
                    ),
                avi_allocated_fip=dict(
                    type='bool',
                    ),
                avi_allocated_vip=dict(
                    type='bool',
                    ),
                client_auth=dict(
                    type='dict',
                    ),
                cloud_config_cksum=dict(
                    type='str',
                    ),
                cloud_ref=dict(
                    type='str',
                    ),
                cloud_type=dict(
                    type='str',
                    ),
                connections_rate_limit=dict(
                    type='dict',
                    ),
                created_by=dict(
                    type='str',
                    ),
                delay_fairness=dict(
                    type='bool',
                    ),
                description=dict(
                    type='str',
                    ),
                discovered_network_ref=dict(
                    type='list',
                    ),
                discovered_networks=dict(
                    type='list',
                    ),
                discovered_subnet=dict(
                    type='list',
                    ),
                dns_info=dict(
                    type='list',
                    ),
                east_west_placement=dict(
                    type='bool',
                    ),
                enable_autogw=dict(
                    type='bool',
                    ),
                enable_rhi=dict(
                    type='bool',
                    ),
                enable_rhi_snat=dict(
                    type='bool',
                    ),
                enabled=dict(
                    type='bool',
                    ),
                floating_ip=dict(
                    type='dict',
                    ),
                floating_subnet_uuid=dict(
                    type='str',
                    ),
                flow_dist=dict(
                    type='str',
                    ),
                flow_label_type=dict(
                    type='str',
                    ),
                fqdn=dict(
                    type='str',
                    ),
                host_name_xlate=dict(
                    type='str',
                    ),
                http_policies=dict(
                    type='list',
                    ),
                ign_pool_net_reach=dict(
                    type='bool',
                    ),
                ip_address=dict(
                    type='dict',
                    ),
                ipam_network_subnet=dict(
                    type='dict',
                    ),
                limit_doser=dict(
                    type='bool',
                    ),
                max_cps_per_client=dict(
                    type='int',
                    ),
                microservice_ref=dict(
                    type='str',
                    ),
                name=dict(
                    type='str',
                    ),
                network_profile_ref=dict(
                    type='str',
                    ),
                network_ref=dict(
                    type='str',
                    ),
                network_security_policy_ref=dict(
                    type='str',
                    ),
                performance_limits=dict(
                    type='dict',
                    ),
                pool_group_ref=dict(
                    type='str',
                    ),
                pool_ref=dict(
                    type='str',
                    ),
                port_uuid=dict(
                    type='str',
                    ),
                remove_listening_port_on_vs_down=dict(
                    type='bool',
                    ),
                requests_rate_limit=dict(
                    type='dict',
                    ),
                scaleout_ecmp=dict(
                    type='bool',
                    ),
                se_group_ref=dict(
                    type='str',
                    ),
                server_network_profile_ref=dict(
                    type='str',
                    ),
                service_pool_select=dict(
                    type='list',
                    ),
                services=dict(
                    type='list',
                    ),
                snat_ip=dict(
                    type='list',
                    ),
                ssl_key_and_certificate_refs=dict(
                    type='list',
                    ),
                ssl_profile_ref=dict(
                    type='str',
                    ),
                ssl_sess_cache_avg_size=dict(
                    type='int',
                    ),
                static_dns_records=dict(
                    type='list',
                    ),
                subnet=dict(
                    type='dict',
                    ),
                subnet_uuid=dict(
                    type='str',
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
                use_bridge_ip_as_vip=dict(
                    type='bool',
                    ),
                uuid=dict(
                    type='str',
                    ),
                vh_domain_name=dict(
                    type='list',
                    ),
                vh_parent_vs_uuid=dict(
                    type='str',
                    ),
                vrf_context_ref=dict(
                    type='str',
                    ),
                vs_datascripts=dict(
                    type='list',
                    ),
                weight=dict(
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
                    'virtualservice', name,
                    tenant=tenant, tenant_uuid=tenant_uuid)
            except ObjectNotFound:
                return module.exit_json(changed=False)
            if rsp.status_code == 204:
                return module.exit_json(changed=True)
            return module.fail_json(msg=rsp.text)
        existing_obj = api.get_object_by_name(
                'virtualservice', name,
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
                    'virtualservice/%s' % obj_uuid, data=obj,
                    tenant=tenant, tenant_uuid=tenant_uuid)
        else:
            changed = True
            rsp = api.post('virtualservice', data=obj,
                           tenant=tenant, tenant_uuid=tenant_uuid)
        if rsp is None:
            return module.exit_json(changed=changed, obj=existing_obj)
        else:
            return ansible_return(module, rsp, changed)
    except:
        raise


if __name__ == '__main__':
    main()