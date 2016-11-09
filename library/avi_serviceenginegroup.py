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

EXAMPLES = """
- code: 'avi_serviceenginegroup controller=10.10.25.42 username=admin '
            ' password=something'
            ' state=present name=sample_serviceenginegroup'
description: "Adds/Deletes ServiceEngineGroup configuration from Avi Controller."
"""

DOCUMENTATION = '''
---
module: avi_serviceenginegroup
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: ServiceEngineGroup Configuration
description:
    - This module is used to configure ServiceEngineGroup object
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
    active_standby:
        description:
            - Service Engines in active/standby mode for HA failover
        default: False
        type: bool
    advertise_backend_networks:
        description:
            - Advertise reach-ability of backend server networks via ADC through BGP for default gateway feature.
        default: False
        type: bool
    aggressive_failure_detection:
        description:
            - Enable aggressive failover configuration for ha.
        default: False
        type: bool
    algo:
        description:
            - If 'compact' placement algorithm is used, Virtual Services are placed on existing Service Engines until they all have the maximum number of Virtual Services. Otherwise, Virtual Services are distributed to as many Service Engines as possible.
        default: 1
        type: string
    auto_rebalance:
        description:
            - If 'Auto Rebalance' is selected, Virtual Services will be automatically migrated when the load on Service Engines falls below the minimum threshold or goes above the maximum threshold. Otherwise, an Alert is generated instead of automatically performing the migration.
        default: False
        type: bool
    auto_rebalance_interval:
        description:
            - Frequency of rebalance, if 'Auto rebalance' is enabled
        default: 300
        type: integer
    auto_redistribute_active_standby_load:
        description:
            - Redistribution of virtual services from the takeover SE to the replacement SE can cause momentary traffic loss. If the auto-redistribute load option is left in its default off state, any desired rebalancing requires calls to REST API.
        default: False
        type: bool
    buffer_se:
        description:
            - Excess Service Engine capacity provisioned for HA failover
        default: 1
        type: integer
    cloud_ref:
        description:
            - Not present. object ref Cloud.
        default: Default-Cloud
        type: string
    connection_memory_percentage:
        description:
            - Percentage of memory for connection state. This will come at the expense of memory used for HTTP in-memory cache.
        default: 50
        type: integer
    cpu_reserve:
        description:
            - Not present.
        default: False
        type: bool
    cpu_socket_affinity:
        description:
            - Allocate all the CPU cores for the Service Engine Virtual Machines  on the same CPU socket. Applicable only for vCenter Cloud.
        default: False
        type: bool
    custom_tag:
        description:
            - Custom tag will be used to create the tags for SE instance in AWS. Note this is not the same as the prefix for SE name
        type: CustomTag
    dedicated_dispatcher_core:
        description:
            - Dedicate the core that handles packet receive/transmit from the network to just the dispatching function. Don't use it for TCP/IP and SSL functions.
        default: False
        type: bool
    description:
        description:
            - Not present.
        type: string
    disk_per_se:
        description:
            - Amount of disk space for each of the Service Engine virtual machines.
        default: 10
        type: integer
    distribute_load_active_standby:
        description:
            - Use both the active and standby Service Engines for Virtual Service placement in the legacy active standby HA mode.
        default: False
        type: bool
    enable_routing:
        description:
            - Enable routing for this ServiceEngineGroup 
        default: False
        type: bool
    extra_config_multiplier:
        description:
            - Multiplier for extra config to support large VS/Pool config.
        default: 0.0
        type: float
    floating_intf_ip:
        description:
            - If ServiceEngineGroup is configured for Legacy 1+1 Active Standby HA Mode, Floating IP's will be advertised only by the Active SE in the Pair. Virtual Services in this group must be disabled/enabled for any changes to the Floating IP's to take effect. If manual load distribution among the Active Standby ServiceEngines is enabled, Floating IP's provided here will be advertised only by the Active ServiceEngine hosting all the VirtualServices tagged with Active Standby SE 1 Tag.
        type: IpAddr
    floating_intf_ip_se_2:
        description:
            - This field is applicable only if the ServiceEngineGroup is configured for Legacy 1+1 Active Standby HA Mode, with manual load distribution among the Active Standby ServiceEngines enabled. Floating IP's provided here will be advertised only by the Active ServiceEngine hosting all the VirtualServices tagged with Active Standby SE 2 Tag.
        type: IpAddr
    ha_mode:
        description:
            - High Availability mode for all the Virtual Services using this Service Engine group.
        default: 2
        type: string
    hardwaresecuritymodulegroup_ref:
        description:
            - Not present. object ref HardwareSecurityModuleGroup.
        type: string
    hm_on_standby:
        description:
            - Enable active health monitoring from the standby SE for all placed virtual services.
        default: True
        type: bool
    host_attribute_key:
        description:
            - Key of a Key,Value pair identifying a set of hosts. Currently used to separate North-South and East-West ServiceEngine sizing requirements, specifically in Container ecosystems, where ServiceEngines on East-West traffic nodes are typically smaller than those on North-South traffic nodes.
        type: string
    host_attribute_value:
        description:
            - Value of a Key,Value pair identifying a set of hosts. Currently used to separate North-South and East-West ServiceEngine sizing requirements, specifically in Container ecosystems, where ServiceEngines on East-West traffic nodes are typically smaller than those on North-South traffic nodes.
        type: string
    hypervisor:
        description:
            - Override default hypervisor
        type: string
    instance_flavor:
        description:
            - Instance/Flavor type for SE instance
        type: string
    iptables:
        description:
            - Iptable Rules
        type: IptableRuleSet
    least_load_core_selection:
        description:
            - Select core with least load for new flow.
        default: True
        type: bool
    log_disksz:
        description:
            - Maximum disk capacity (in MB) to be allocated to an SE. This is exclusively used for debug and log data.
        default: 10000
        type: integer
    max_cpu_usage:
        description:
            - When CPU utilization exceeds this maximum threshold, Virtual Services hosted on this Service Engine may be rebalanced to other Service Engines to lighten the load. A new Service Engine may be created as part of this process.
        default: 80
        type: integer
    max_scaleout_per_vs:
        description:
            - Maximum number of active Service Engines for the Virtual Service.
        default: 4
        type: integer
    max_se:
        description:
            - Maximum number of Services Engines in this group.
        default: 10
        type: integer
    max_vs_per_se:
        description:
            - Maximum number of Virtual Services that can be placed on a single Service Engine.
        default: 10
        type: integer
    mem_reserve:
        description:
            - Not present.
        default: True
        type: bool
    memory_per_se:
        description:
            - Amount of memory for each of the Service Engine virtual machines.
        default: 2048
        type: integer
    mgmt_network_ref:
        description:
            - Management network to use for Avi Service Engines object ref Network.
        type: string
    mgmt_subnet:
        description:
            - Management subnet to use for Avi Service Engines
        type: IpAddrPrefix
    min_cpu_usage:
        description:
            - When CPU utilization falls below the minimum threshold, Virtual Services hosted on this Service Engine may be consolidated onto other underutilized Service Engines.  After consolidation, unused Service Engines may then be eligible for deletion. When CPU utilization exceeds the maximum threshold, Virtual Services hosted on this Service Engine may be migrated to other Service Engines to lighten the load. A new Service Engine may be created as part of this process.
        default: 30
        type: integer
    min_scaleout_per_vs:
        description:
            - Minimum number of active Service Engines for the Virtual Service.
        default: 1
        type: integer
    name:
        description:
            - Not present.
        required: true
        type: string
    num_flow_cores_sum_changes_to_ignore:
        description:
            - Number of changes in num flow cores sum to ignore.
        default: 8
        type: integer
    openstack_availability_zone:
        description:
            - Not present.
        type: string
    openstack_mgmt_network_name:
        description:
            - Avi Management network name
        type: string
    openstack_mgmt_network_uuid:
        description:
            - Management network UUID
        type: string
    os_reserved_memory:
        description:
            - Amount of extra memory to be reserved for use by the Operating System on a Service Engine.
        default: 0
        type: integer
    per_app:
        description:
            - Per-app SE mode is designed for deploying dedicated load balancers per app (VS). In this mode, each SE is limited to a max of 2 VSs. vCPUs in per-app SEs count towards licensing usage at 25% rate.
        default: False
        type: bool
    placement_mode:
        description:
            - If placement mode is 'Auto', Virtual Services are automatically placed on Service Engines.
        default: 1
        type: string
    realtime_se_metrics:
        description:
            - Enable or disable real time SE metrics
        type: MetricsRealTimeUpdate
    se_deprovision_delay:
        description:
            - Duration to preserve unused Service Engine virtual machines before deleting them. If traffic to a Virtual Service were to spike up abruptly, this Service Engine would still be available to be utilized again rather than creating a new Service Engine.
        default: 120
        type: integer
    se_dos_profile:
        description:
            - Not present.
        type: DosThresholdProfile
    se_name_prefix:
        description:
            - Prefix to use for virtual machine name of Service Engines.
        default: Avi
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
    uuid:
        description:
            - Not present.
        type: string
    vcenter_clusters:
        description:
            - Not present.
        type: VcenterClusters
    vcenter_datastore_mode:
        description:
            - Not present.
        default: 1
        type: string
    vcenter_datastores:
        description:
            - Not present.
        type: VcenterDatastore
    vcenter_datastores_include:
        description:
            - Not present.
        default: False
        type: bool
    vcenter_folder:
        description:
            - Folder to place all the Service Engine virtual machines in vCenter.
        default: AviSeFolder
        type: string
    vcenter_hosts:
        description:
            - Not present.
        type: VcenterHosts
    vcpus_per_se:
        description:
            - Number of vcpus for each of the Service Engine virtual machines.
        default: 2
        type: integer
    vs_host_redundancy:
        description:
            - Ensure primary and secondary Service Engines are deployed on different physical hosts.
        default: True
        type: bool
    vs_scalein_timeout:
        description:
            - Time to wait for the scaled in SE to drain existing flows before marking the scalein done
        default: 30
        type: integer
    vs_scalein_timeout_for_upgrade:
        description:
            - During SE upgrade, Time to wait for the scaled-in SE to drain existing flows before marking the scalein done
        default: 30
        type: integer
    vs_scaleout_timeout:
        description:
            - Time to wait for the scaled out SE to become ready before marking the scaleout done
        default: 30
        type: integer
'''

RETURN = '''
obj:
    description: ServiceEngineGroup (api/serviceenginegroup) object
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
                active_standby=dict(
                    type='bool',
                    ),
                advertise_backend_networks=dict(
                    type='bool',
                    ),
                aggressive_failure_detection=dict(
                    type='bool',
                    ),
                algo=dict(
                    type='str',
                    ),
                auto_rebalance=dict(
                    type='bool',
                    ),
                auto_rebalance_interval=dict(
                    type='int',
                    ),
                auto_redistribute_active_standby_load=dict(
                    type='bool',
                    ),
                buffer_se=dict(
                    type='int',
                    ),
                cloud_ref=dict(
                    type='str',
                    ),
                connection_memory_percentage=dict(
                    type='int',
                    ),
                cpu_reserve=dict(
                    type='bool',
                    ),
                cpu_socket_affinity=dict(
                    type='bool',
                    ),
                custom_tag=dict(
                    type='list',
                    ),
                dedicated_dispatcher_core=dict(
                    type='bool',
                    ),
                description=dict(
                    type='str',
                    ),
                disk_per_se=dict(
                    type='int',
                    ),
                distribute_load_active_standby=dict(
                    type='bool',
                    ),
                enable_routing=dict(
                    type='bool',
                    ),
                extra_config_multiplier=dict(
                    type='float',
                    ),
                floating_intf_ip=dict(
                    type='list',
                    ),
                floating_intf_ip_se_2=dict(
                    type='list',
                    ),
                ha_mode=dict(
                    type='str',
                    ),
                hardwaresecuritymodulegroup_ref=dict(
                    type='str',
                    ),
                hm_on_standby=dict(
                    type='bool',
                    ),
                host_attribute_key=dict(
                    type='str',
                    ),
                host_attribute_value=dict(
                    type='str',
                    ),
                hypervisor=dict(
                    type='str',
                    ),
                instance_flavor=dict(
                    type='str',
                    ),
                iptables=dict(
                    type='list',
                    ),
                least_load_core_selection=dict(
                    type='bool',
                    ),
                log_disksz=dict(
                    type='int',
                    ),
                max_cpu_usage=dict(
                    type='int',
                    ),
                max_scaleout_per_vs=dict(
                    type='int',
                    ),
                max_se=dict(
                    type='int',
                    ),
                max_vs_per_se=dict(
                    type='int',
                    ),
                mem_reserve=dict(
                    type='bool',
                    ),
                memory_per_se=dict(
                    type='int',
                    ),
                mgmt_network_ref=dict(
                    type='str',
                    ),
                mgmt_subnet=dict(
                    type='dict',
                    ),
                min_cpu_usage=dict(
                    type='int',
                    ),
                min_scaleout_per_vs=dict(
                    type='int',
                    ),
                name=dict(
                    type='str',
                    ),
                num_flow_cores_sum_changes_to_ignore=dict(
                    type='int',
                    ),
                openstack_availability_zone=dict(
                    type='str',
                    ),
                openstack_mgmt_network_name=dict(
                    type='str',
                    ),
                openstack_mgmt_network_uuid=dict(
                    type='str',
                    ),
                os_reserved_memory=dict(
                    type='int',
                    ),
                per_app=dict(
                    type='bool',
                    ),
                placement_mode=dict(
                    type='str',
                    ),
                realtime_se_metrics=dict(
                    type='dict',
                    ),
                se_deprovision_delay=dict(
                    type='int',
                    ),
                se_dos_profile=dict(
                    type='dict',
                    ),
                se_name_prefix=dict(
                    type='str',
                    ),
                tenant_ref=dict(
                    type='str',
                    ),
                url=dict(
                    type='str',
                    ),
                uuid=dict(
                    type='str',
                    ),
                vcenter_clusters=dict(
                    type='dict',
                    ),
                vcenter_datastore_mode=dict(
                    type='str',
                    ),
                vcenter_datastores=dict(
                    type='list',
                    ),
                vcenter_datastores_include=dict(
                    type='bool',
                    ),
                vcenter_folder=dict(
                    type='str',
                    ),
                vcenter_hosts=dict(
                    type='dict',
                    ),
                vcpus_per_se=dict(
                    type='int',
                    ),
                vs_host_redundancy=dict(
                    type='bool',
                    ),
                vs_scalein_timeout=dict(
                    type='int',
                    ),
                vs_scalein_timeout_for_upgrade=dict(
                    type='int',
                    ),
                vs_scaleout_timeout=dict(
                    type='int',
                    ),
                ),
        )
        return avi_ansible_api(module, 'serviceenginegroup',
                               set([]))
    except:
        raise


if __name__ == '__main__':
    main()