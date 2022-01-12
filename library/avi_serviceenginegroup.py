#!/usr/bin/python
# module_check: supported

# Avi Version: 17.1.1
# Copyright 2021 VMware, Inc.  All rights reserved. VMware Confidential
# SPDX-License-Identifier: Apache License 2.0


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_serviceenginegroup
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of ServiceEngineGroup Avi RESTful Object
description:
    - This module is used to configure ServiceEngineGroup object
    - more examples at U(https://github.com/avinetworks/devops)
requirements: [ avisdk ]
version_added: "2.4"
options:
    state:
        description:
            - The state that should be applied on the entity.
        default: present
        choices: ["absent", "present"]
        type: str
    avi_api_update_method:
        description:
            - Default method for object update is HTTP PUT.
            - Setting to patch will override that behavior to use HTTP PATCH.
        version_added: "2.5"
        default: put
        choices: ["put", "patch"]
        type: str
    avi_api_patch_op:
        description:
            - Patch operation to use when using avi_api_update_method as patch.
        version_added: "2.5"
        choices: ["add", "replace", "delete", "remove"]
        type: str
    avi_patch_path:
        description:
            - Patch path to use when using avi_api_update_method as patch.
        type: str
    avi_patch_value:
        description:
            - Patch value to use when using avi_api_update_method as patch.
        type: str
    accelerated_networking:
        description:
            - Enable accelerated networking option for azure se.
            - Accelerated networking enables single root i/o virtualization (sr-iov) to a se vm.
            - This improves networking performance.
            - Field introduced in 17.2.14,18.1.5,18.2.1.
        version_added: "2.9"
        type: bool
    active_standby:
        description:
            - Service engines in active/standby mode for ha failover.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    additional_config_memory:
        description:
            - Indicates the percent of config memory used for config updates.
            - Allowed values are 0-90.
            - Field deprecated in 18.1.2.
            - Field introduced in 18.1.1.
            - Unit is percent.
        version_added: "2.9"
        type: int
    advertise_backend_networks:
        description:
            - Advertise reach-ability of backend server networks via adc through bgp for default gateway feature.
            - Field deprecated in 18.2.5.
        type: bool
    aggressive_failure_detection:
        description:
            - Enable aggressive failover configuration for ha.
            - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    algo:
        description:
            - In compact placement, virtual services are placed on existing ses until max_vs_per_se limit is reached.
            - Enum options - PLACEMENT_ALGO_PACKED, PLACEMENT_ALGO_DISTRIBUTED.
            - Default value when not specified in API or module is interpreted by Avi Controller as PLACEMENT_ALGO_PACKED.
        type: str
    allow_burst:
        description:
            - Allow ses to be created using burst license.
            - Field introduced in 17.2.5.
        version_added: "2.5"
        type: bool
    app_cache_percent:
        description:
            - A percent value of total se memory reserved for applicationcaching.
            - This is an se bootup property and requires se restart.requires se reboot.
            - Allowed values are 0 - 100.
            - Special values are 0- disable.
            - Field introduced in 18.2.3.
            - Unit is percent.
            - Allowed in basic(allowed values- 0) edition, essentials(allowed values- 0) edition, enterprise edition.
            - Special default for basic edition is 0, essentials edition is 0, enterprise is 10.
            - Default value when not specified in API or module is interpreted by Avi Controller as 10.
        version_added: "2.9"
        type: int
    app_cache_threshold:
        description:
            - The max memory that can be allocated for the app cache.
            - This value will act as an upper bound on the cache size specified in app_cache_percent.
            - Special values are 0- disable.
            - Field introduced in 20.1.1.
            - Unit is gb.
            - Default value when not specified in API or module is interpreted by Avi Controller as 5.
        type: int
    app_learning_memory_percent:
        description:
            - A percent value of total se memory reserved for application learning.
            - This is an se bootup property and requires se restart.
            - Allowed values are 0 - 10.
            - Field introduced in 18.2.3.
            - Unit is percent.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        version_added: "2.9"
        type: int
    archive_shm_limit:
        description:
            - Amount of se memory in gb until which shared memory is collected in core archive.
            - Field introduced in 17.1.3.
            - Unit is gb.
            - Default value when not specified in API or module is interpreted by Avi Controller as 8.
        type: int
    async_ssl:
        description:
            - Ssl handshakes will be handled by dedicated ssl threads.requires se reboot.
            - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        version_added: "2.4"
        type: bool
    async_ssl_threads:
        description:
            - Number of async ssl threads per se_dp.requires se reboot.
            - Allowed values are 1-16.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
        version_added: "2.4"
        type: int
    auto_rebalance:
        description:
            - If set, virtual services will be automatically migrated when load on an se is less than minimum or more than maximum thresholds.
            - Only alerts are generated when the auto_rebalance is not set.
            - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    auto_rebalance_capacity_per_se:
        description:
            - Capacities of se for auto rebalance for each criteria.
            - Field introduced in 17.2.4.
        version_added: "2.5"
        type: list
    auto_rebalance_criteria:
        description:
            - Set of criteria for se auto rebalance.
            - Enum options - SE_AUTO_REBALANCE_CPU, SE_AUTO_REBALANCE_PPS, SE_AUTO_REBALANCE_MBPS, SE_AUTO_REBALANCE_OPEN_CONNS, SE_AUTO_REBALANCE_CPS.
            - Field introduced in 17.2.3.
        version_added: "2.5"
        type: list
    auto_rebalance_interval:
        description:
            - Frequency of rebalance, if 'auto rebalance' is enabled.
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 300.
        type: int
    auto_redistribute_active_standby_load:
        description:
            - Redistribution of virtual services from the takeover se to the replacement se can cause momentary traffic loss.
            - If the auto-redistribute load option is left in its default off state, any desired rebalancing requires calls to rest api.
            - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    availability_zone_refs:
        description:
            - Availability zones for virtual service high availability.
            - It is a reference to an object of type availabilityzone.
            - Field introduced in 20.1.1.
        type: list
    baremetal_dispatcher_handles_flows:
        description:
            - Control if dispatcher core also handles tcp flows in baremetal se.
            - Field introduced in 21.1.3.
            - Allowed in basic edition, essentials edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    bgp_peer_monitor_failover_enabled:
        description:
            - Enable bgp peer monitoring based failover.
            - Field introduced in 21.1.3.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    bgp_state_update_interval:
        description:
            - Bgp peer state update interval.
            - Allowed values are 5-100.
            - Field introduced in 17.2.14,18.1.5,18.2.1.
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 60.
        version_added: "2.9"
        type: int
    buffer_se:
        description:
            - Excess service engine capacity provisioned for ha failover.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
        type: int
    cloud_ref:
        description:
            - It is a reference to an object of type cloud.
        type: str
    compress_ip_rules_for_each_ns_subnet:
        description:
            - Compress ip rules into a single subnet based ip rule for each north-south ipam subnet configured in pcap mode in openshift/kubernetes node.
            - Field introduced in 18.2.9, 20.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    config_debugs_on_all_cores:
        description:
            - Enable config debugs on all cores of se.
            - Field introduced in 17.2.13,18.1.5,18.2.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        version_added: "2.9"
        type: bool
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 21.1.1.
        type: dict
    connection_memory_percentage:
        description:
            - Percentage of memory for connection state.
            - This will come at the expense of memory used for http in-memory cache.
            - Allowed values are 10-90.
            - Unit is percent.
            - Default value when not specified in API or module is interpreted by Avi Controller as 50.
        type: int
    core_shm_app_cache:
        description:
            - Include shared memory for app cache in core file.requires se reboot.
            - Field introduced in 18.2.8, 20.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    core_shm_app_learning:
        description:
            - Include shared memory for app learning in core file.requires se reboot.
            - Field introduced in 18.2.8, 20.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    cpu_reserve:
        description:
            - Boolean flag to set cpu_reserve.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    cpu_socket_affinity:
        description:
            - Allocate all the cpu cores for the service engine virtual machines  on the same cpu socket.
            - Applicable only for vcenter cloud.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    custom_securitygroups_data:
        description:
            - Custom security groups to be associated with data vnics for se instances in openstack and aws clouds.
            - Field introduced in 17.1.3.
        type: list
    custom_securitygroups_mgmt:
        description:
            - Custom security groups to be associated with management vnic for se instances in openstack and aws clouds.
            - Field introduced in 17.1.3.
        type: list
    custom_tag:
        description:
            - Custom tag will be used to create the tags for se instance in aws.
            - Note this is not the same as the prefix for se name.
        type: list
    data_network_id:
        description:
            - Subnet used to spin up the data nic for service engines, used only for azure cloud.
            - Overrides the cloud level setting for service engine subnet.
            - Field introduced in 18.2.3.
        version_added: "2.9"
        type: str
    datascript_timeout:
        description:
            - Number of instructions before datascript times out.
            - Allowed values are 0-100000000.
            - Field introduced in 18.2.3.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1000000.
        version_added: "2.9"
        type: int
    deactivate_ipv6_discovery:
        description:
            - If activated, ipv6 address and route discovery are deactivated.requires se reboot.
            - Field introduced in 21.1.1.
        type: bool
    deactivate_kni_filtering_at_dispatcher:
        description:
            - Deactivate filtering of packets to kni interface.
            - To be used under surveillance of avi support.
            - Field introduced in 21.1.3.
        type: bool
    dedicated_dispatcher_core:
        description:
            - Dedicate the core that handles packet receive/transmit from the network to just the dispatching function.
            - Don't use it for tcp/ip and ssl functions.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    description:
        description:
            - User defined description for the object.
        type: str
    disable_avi_securitygroups:
        description:
            - By default, avi creates and manages security groups along with custom sg provided by user.
            - Set this to true to disallow avi to create and manage new security groups.
            - Avi will only make use of custom security groups provided by user.
            - This option is supported for aws and openstack cloud types.
            - Field introduced in 17.2.13,18.1.4,18.2.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        version_added: "2.9"
        type: bool
    disable_csum_offloads:
        description:
            - Stop using tcp/udp and ip checksum offload features of nics.
            - Field introduced in 17.1.14, 17.2.5, 18.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        version_added: "2.5"
        type: bool
    disable_flow_probes:
        description:
            - Disable flow probes for scaled out vs'es.
            - Field introduced in 20.1.3.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    disable_gro:
        description:
            - Disable generic receive offload (gro) in dpdk poll-mode driver packet receive path.
            - Gro is on by default on nics that do not support lro (large receive offload) or do not gain performance boost from lro.
            - Field introduced in 17.2.5, 18.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        version_added: "2.5"
        type: bool
    disable_se_memory_check:
        description:
            - If set, disable the config memory check done in service engine.
            - Field introduced in 18.1.2.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        version_added: "2.9"
        type: bool
    disable_tso:
        description:
            - Disable tcp segmentation offload (tso) in dpdk poll-mode driver packet transmit path.
            - Tso is on by default on nics that support it.
            - Field introduced in 17.2.5, 18.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        version_added: "2.5"
        type: bool
    disk_per_se:
        description:
            - Amount of disk space for each of the service engine virtual machines.
            - Unit is gb.
            - Default value when not specified in API or module is interpreted by Avi Controller as 15.
        type: int
    distribute_load_active_standby:
        description:
            - Use both the active and standby service engines for virtual service placement in the legacy active standby ha mode.
            - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    distribute_queues:
        description:
            - Distributes queue ownership among cores so multiple cores handle dispatcher duties.
            - Requires se reboot.
            - Deprecated from 18.2.8, instead use max_queues_per_vnic.
            - Field introduced in 17.2.8.
            - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        version_added: "2.9"
        type: bool
    distribute_vnics:
        description:
            - Distributes vnic ownership among cores so multiple cores handle dispatcher duties.requires se reboot.
            - Field introduced in 18.2.5.
            - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        version_added: "2.9"
        type: bool
    downstream_send_timeout:
        description:
            - Timeout for downstream to become writable.
            - Field introduced in 21.1.1.
            - Unit is milliseconds.
            - Default value when not specified in API or module is interpreted by Avi Controller as 3600000.
        type: int
    dp_aggressive_deq_interval_msec:
        description:
            - Dequeue interval for receive queue from se_dp in aggressive mode.
            - Allowed values are 1-1000.
            - Field introduced in 21.1.1.
            - Unit is milliseconds.
            - Allowed in basic edition, essentials edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
        type: int
    dp_aggressive_enq_interval_msec:
        description:
            - Enqueue interval for request queue to se_dp in aggressive mode.
            - Allowed values are 1-1000.
            - Field introduced in 21.1.1.
            - Unit is milliseconds.
            - Allowed in basic edition, essentials edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
        type: int
    dp_aggressive_hb_frequency:
        description:
            - Frequency of se - se hb messages when aggressive failure mode detection is enabled.
            - Field introduced in 20.1.3.
            - Unit is milliseconds.
            - Default value when not specified in API or module is interpreted by Avi Controller as 100.
        type: int
    dp_aggressive_hb_timeout_count:
        description:
            - Consecutive hb failures after which failure is reported to controller,when aggressive failure mode detection is enabled.
            - Field introduced in 20.1.3.
            - Default value when not specified in API or module is interpreted by Avi Controller as 10.
        type: int
    dp_deq_interval_msec:
        description:
            - Dequeue interval for receive queue from se_dp.
            - Allowed values are 1-1000.
            - Field introduced in 21.1.1.
            - Unit is milliseconds.
            - Allowed in basic edition, essentials edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 20.
        type: int
    dp_enq_interval_msec:
        description:
            - Enqueue interval for request queue to se_dp.
            - Allowed values are 1-1000.
            - Field introduced in 21.1.1.
            - Unit is milliseconds.
            - Allowed in basic edition, essentials edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 20.
        type: int
    dp_hb_frequency:
        description:
            - Frequency of se - se hb messages when aggressive failure mode detection is not enabled.
            - Field introduced in 20.1.3.
            - Unit is milliseconds.
            - Default value when not specified in API or module is interpreted by Avi Controller as 100.
        type: int
    dp_hb_timeout_count:
        description:
            - Consecutive hb failures after which failure is reported to controller, when aggressive failure mode detection is not enabled.
            - Field introduced in 20.1.3.
            - Default value when not specified in API or module is interpreted by Avi Controller as 10.
        type: int
    enable_gratarp_permanent:
        description:
            - Enable gratarp for vip_ip.
            - Field introduced in 18.2.3.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        version_added: "2.9"
        type: bool
    enable_hsm_log:
        description:
            - Enable hsm luna engine logs.
            - Field introduced in 21.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    enable_hsm_priming:
        description:
            - (this is a beta feature).
            - Enable hsm key priming.
            - If enabled, key handles on the hsm will be synced to se before processing client connections.
            - Field introduced in 17.2.7, 18.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        version_added: "2.6"
        type: bool
    enable_multi_lb:
        description:
            - Applicable only for azure cloud with basic sku lb.
            - If set, additional azure lbs will be automatically created if resources in existing lb are exhausted.
            - Field introduced in 17.2.10, 18.1.2.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        version_added: "2.9"
        type: bool
    enable_pcap_tx_ring:
        description:
            - Enable tx ring support in pcap mode of operation.
            - Tso feature is not supported with tx ring enabled.
            - Deprecated from 18.2.8, instead use pcap_tx_mode.
            - Requires se reboot.
            - Field introduced in 18.2.5.
        version_added: "2.9"
        type: bool
    enable_routing:
        description:
            - Enable routing for this serviceenginegroup.
            - Field deprecated in 18.2.5.
            - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
        type: bool
    enable_vip_on_all_interfaces:
        description:
            - Enable vip on all interfaces of se.
            - Field deprecated in 18.2.5.
            - Field introduced in 17.1.1.
        type: bool
    enable_vmac:
        description:
            - Use virtual mac address for interfaces on which floating interface ips are placed.
            - Field deprecated in 18.2.5.
        type: bool
    ephemeral_portrange_end:
        description:
            - End local ephemeral port number for outbound connections.
            - Field introduced in 17.2.13, 18.1.5, 18.2.1.
        version_added: "2.9"
        type: int
    ephemeral_portrange_start:
        description:
            - Start local ephemeral port number for outbound connections.
            - Field introduced in 17.2.13, 18.1.5, 18.2.1.
        version_added: "2.9"
        type: int
    extra_config_multiplier:
        description:
            - Multiplier for extra config to support large vs/pool config.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.0.
        type: float
    extra_shared_config_memory:
        description:
            - Extra config memory to support large geo db configuration.
            - Field introduced in 17.1.1.
            - Unit is mb.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    floating_intf_ip:
        description:
            - If serviceenginegroup is configured for legacy 1+1 active standby ha mode, floating ip's will be advertised only by the active se in the pair.
            - Virtual services in this group must be disabled/enabled for any changes to the floating ip's to take effect.
            - Only active se hosting vs tagged with active standby se 1 tag will advertise this floating ip when manual load distribution is enabled.
            - Field deprecated in 18.2.5.
            - Maximum of 32 items allowed.
        type: list
    floating_intf_ip_se_2:
        description:
            - If serviceenginegroup is configured for legacy 1+1 active standby ha mode, floating ip's will be advertised only by the active se in the pair.
            - Virtual services in this group must be disabled/enabled for any changes to the floating ip's to take effect.
            - Only active se hosting vs tagged with active standby se 2 tag will advertise this floating ip when manual load distribution is enabled.
            - Field deprecated in 18.2.5.
            - Maximum of 32 items allowed.
        type: list
    flow_table_new_syn_max_entries:
        description:
            - Maximum number of flow table entries that have not completed tcp three-way handshake yet.
            - Field introduced in 17.2.5.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        version_added: "2.5"
        type: int
    free_list_size:
        description:
            - Number of entries in the free list.
            - Field introduced in 17.2.10, 18.1.2.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1024.
        version_added: "2.9"
        type: int
    gcp_config:
        description:
            - Google cloud platform, service engine group configuration.
            - Field introduced in 20.1.3.
        type: dict
    gratarp_permanent_periodicity:
        description:
            - Gratarp periodicity for vip-ip.
            - Allowed values are 5-30.
            - Field introduced in 18.2.3.
            - Unit is min.
            - Default value when not specified in API or module is interpreted by Avi Controller as 10.
        version_added: "2.9"
        type: int
    ha_mode:
        description:
            - High availability mode for all the virtual services using this service engine group.
            - Enum options - HA_MODE_SHARED_PAIR, HA_MODE_SHARED, HA_MODE_LEGACY_ACTIVE_STANDBY.
            - Allowed in basic(allowed values- ha_mode_legacy_active_standby) edition, essentials(allowed values- ha_mode_legacy_active_standby) edition,
            - enterprise edition.
            - Special default for basic edition is ha_mode_legacy_active_standby, essentials edition is ha_mode_legacy_active_standby, enterprise is
            - ha_mode_shared.
            - Default value when not specified in API or module is interpreted by Avi Controller as HA_MODE_SHARED.
        type: str
    handle_per_pkt_attack:
        description:
            - Configuration to handle per packet attack handling.for example, dns reflection attack is a type of attack where a response packet is sent to the
            - dns vs.this configuration tells if such packets should be dropped without further processing.
            - Field introduced in 20.1.3.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    hardwaresecuritymodulegroup_ref:
        description:
            - It is a reference to an object of type hardwaresecuritymodulegroup.
        type: str
    heap_minimum_config_memory:
        description:
            - Minimum required heap memory to apply any configuration.
            - Allowed values are 0-100.
            - Field introduced in 18.1.2.
            - Unit is mb.
            - Default value when not specified in API or module is interpreted by Avi Controller as 8.
        version_added: "2.9"
        type: int
    hm_on_standby:
        description:
            - Enable active health monitoring from the standby se for all placed virtual services.
            - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
            - Special default for basic edition is false, essentials edition is false, enterprise is true.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    host_attribute_key:
        description:
            - Key of a (key, value) pair identifying a label for a set of nodes usually in container clouds.
            - Needs to be specified together with host_attribute_value.
            - Ses can be configured differently including ha modes across different se groups.
            - May also be used for isolation between different classes of virtualservices.
            - Virtualservices' se group may be specified via annotations/labels.
            - A openshift/kubernetes namespace maybe annotated with a matching se group label as openshift.io/node-selector  apptype=prod.
            - When multiple se groups are used in a cloud with host attributes specified,just a single se group can exist as a match-all se group without a
            - host_attribute_key.
        type: str
    host_attribute_value:
        description:
            - Value of a (key, value) pair identifying a label for a set of nodes usually in container clouds.
            - Needs to be specified together with host_attribute_key.
        type: str
    host_gateway_monitor:
        description:
            - Enable the host gateway monitor when service engine is deployed as docker container.
            - Disabled by default.
            - Field introduced in 17.2.4.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        version_added: "2.5"
        type: bool
    http_rum_console_log:
        description:
            - Enable javascript console logs on the client browser when collecting client insights.
            - Field introduced in 21.1.1.
            - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    http_rum_min_content_length:
        description:
            - Minimum response size content length to sample for client insights.
            - Field introduced in 21.1.1.
            - Allowed in basic(allowed values- 64) edition, essentials(allowed values- 64) edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 64.
        type: int
    hybrid_rss_mode:
        description:
            - Toggles se hybrid only mode of operation in dpdk mode with rss configured;where-in each se datapath instance operates as an independent
            - standalonehybrid instance performing both dispatcher and proxy function.
            - Requires reboot.
            - Field introduced in 21.1.3.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    hypervisor:
        description:
            - Override default hypervisor.
            - Enum options - DEFAULT, VMWARE_ESX, KVM, VMWARE_VSAN, XEN.
        type: str
    ignore_docker_mac_change:
        description:
            - Ignore docker mac change.
            - Field introduced in 21.1.3.
            - Allowed in basic edition, essentials edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    ignore_rtt_threshold:
        description:
            - Ignore rtt samples if it is above threshold.
            - Field introduced in 17.1.6,17.2.2.
            - Unit is milliseconds.
            - Default value when not specified in API or module is interpreted by Avi Controller as 5000.
        version_added: "2.5"
        type: int
    ingress_access_data:
        description:
            - Program se security group ingress rules to allow vip data access from remote cidr type.
            - Enum options - SG_INGRESS_ACCESS_NONE, SG_INGRESS_ACCESS_ALL, SG_INGRESS_ACCESS_VPC.
            - Field introduced in 17.1.5.
            - Default value when not specified in API or module is interpreted by Avi Controller as SG_INGRESS_ACCESS_ALL.
        version_added: "2.5"
        type: str
    ingress_access_mgmt:
        description:
            - Program se security group ingress rules to allow ssh/icmp management access from remote cidr type.
            - Enum options - SG_INGRESS_ACCESS_NONE, SG_INGRESS_ACCESS_ALL, SG_INGRESS_ACCESS_VPC.
            - Field introduced in 17.1.5.
            - Default value when not specified in API or module is interpreted by Avi Controller as SG_INGRESS_ACCESS_ALL.
        version_added: "2.5"
        type: str
    instance_flavor:
        description:
            - Instance/flavor name for se instance.
        type: str
    instance_flavor_info:
        description:
            - Additional information associated with instance_flavor.
            - Field introduced in 20.1.1.
        type: dict
    iptables:
        description:
            - Iptable rules.
            - Maximum of 128 items allowed.
        type: list
    kni_allowed_server_ports:
        description:
            - Port ranges for any servers running in inband linuxserver clouds.
            - Field introduced in 21.1.3.
        type: list
    l7_conns_per_core:
        description:
            - Number of l7 connections that can be cached per core.
            - Field introduced in 21.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as 16384.
        type: int
    l7_resvd_listen_conns_per_core:
        description:
            - Number of reserved l7 listener connections per core.
            - Field introduced in 21.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as 256.
        type: int
    labels:
        description:
            - Labels associated with this se group.
            - Field introduced in 20.1.1.
            - Maximum of 1 items allowed.
        type: list
    lbaction_num_requests_to_dispatch:
        description:
            - Number of requests to dispatch from the request.
            - Queue at a regular interval.
            - Field introduced in 21.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as 4.
        type: int
    lbaction_rq_per_request_max_retries:
        description:
            - Maximum retries per request in the request queue.
            - Field introduced in 21.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as 22.
        type: int
    least_load_core_selection:
        description:
            - Select core with least load for new flow.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    license_tier:
        description:
            - Specifies the license tier which would be used.
            - This field by default inherits the value from cloud.
            - Enum options - ENTERPRISE_16, ENTERPRISE, ENTERPRISE_18, BASIC, ESSENTIALS, ENTERPRISE_WITH_CLOUD_SERVICES.
            - Field introduced in 17.2.5.
        version_added: "2.5"
        type: str
    license_type:
        description:
            - If no license type is specified then default license enforcement for the cloud type is chosen.
            - Enum options - LIC_BACKEND_SERVERS, LIC_SOCKETS, LIC_CORES, LIC_HOSTS, LIC_SE_BANDWIDTH, LIC_METERED_SE_BANDWIDTH.
            - Field introduced in 17.2.5.
        version_added: "2.5"
        type: str
    log_agent_compress_logs:
        description:
            - Flag to indicate if log files are compressed upon full on the service engine.
            - Field introduced in 21.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    log_agent_debug_enabled:
        description:
            - Enable debug logs by default on service engine.
            - This includes all other debugging logs.
            - Debug logs can also be explcitly enabled from the cli shell.
            - Field introduced in 21.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    log_agent_file_sz_appl:
        description:
            - Maximum application log file size before rollover.
            - Field introduced in 21.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as 4.
        type: int
    log_agent_file_sz_conn:
        description:
            - Maximum connection log file size before rollover.
            - Field introduced in 21.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as 4.
        type: int
    log_agent_file_sz_debug:
        description:
            - Maximum debug log file size before rollover.
            - Field introduced in 21.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as 4.
        type: int
    log_agent_file_sz_event:
        description:
            - Maximum event log file size before rollover.
            - Field introduced in 21.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as 4.
        type: int
    log_agent_log_storage_min_sz:
        description:
            - Minimum storage allocated for logs irrespective of memory and cores.
            - Field introduced in 21.1.1.
            - Unit is mb.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1024.
        type: int
    log_agent_max_concurrent_rsync:
        description:
            - Maximum concurrent rsync requests initiated from log-agent to the controller.
            - Field introduced in 21.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1024.
        type: int
    log_agent_max_storage_excess_percent:
        description:
            - Excess percentage threshold of disk size to trigger cleanup of logs on the service engine.
            - Field introduced in 21.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as 110.
        type: int
    log_agent_max_storage_ignore_percent:
        description:
            - Maximum storage on the disk not allocated for logs on the service engine.
            - Field introduced in 21.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as 20.0.
        type: float
    log_agent_min_storage_per_vs:
        description:
            - Minimum storage allocated to any given virtualservice on the service engine.
            - Field introduced in 21.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as 10.
        type: int
    log_agent_sleep_interval:
        description:
            - Internal timer to stall log-agent and prevent it from hogging cpu cycles on the service engine.
            - Field introduced in 21.1.1.
            - Unit is milliseconds.
            - Default value when not specified in API or module is interpreted by Avi Controller as 10.
        type: int
    log_agent_trace_enabled:
        description:
            - Enable trace logs by default on service engine.
            - Configuration operations are logged along with other important logs by service engine.
            - Field introduced in 21.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    log_agent_unknown_vs_timer:
        description:
            - Timeout to purge unknown virtual service logs from the service engine.
            - Field introduced in 21.1.1.
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1800.
        type: int
    log_disksz:
        description:
            - Maximum disk capacity (in mb) to be allocated to an se.
            - This is exclusively used for debug and log data.
            - Unit is mb.
            - Default value when not specified in API or module is interpreted by Avi Controller as 10000.
        type: int
    log_malloc_failure:
        description:
            - Se will log memory allocation related failure to the se_trace file, wherever available.
            - Field introduced in 20.1.2.
            - Allowed in basic(allowed values- true) edition, essentials(allowed values- true) edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    log_message_max_file_list_size:
        description:
            - Maximum number of file names in a log message.
            - Field introduced in 21.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as 64.
        type: int
    markers:
        description:
            - List of labels to be used for granular rbac.
            - Field introduced in 20.1.7.
            - Allowed in basic edition, essentials edition, enterprise edition.
        type: list
    max_concurrent_external_hm:
        description:
            - Maximum number of external health monitors that can run concurrently in a service engine.
            - This helps control the cpu and memory use by external health monitors.
            - Special values are 0- value will be internally calculated based on cpu and memory.
            - Field introduced in 18.2.7.
        type: int
    max_cpu_usage:
        description:
            - When cpu usage on an se exceeds this threshold, virtual services hosted on this se may be rebalanced to other ses to reduce load.
            - A new se may be created as part of this process.
            - Allowed values are 40-90.
            - Unit is percent.
            - Default value when not specified in API or module is interpreted by Avi Controller as 80.
        type: int
    max_memory_per_mempool:
        description:
            - Max bytes that can be allocated in a single mempool.
            - Field introduced in 18.1.5.
            - Unit is mb.
            - Default value when not specified in API or module is interpreted by Avi Controller as 64.
        version_added: "2.9"
        type: int
    max_num_se_dps:
        description:
            - Configures the maximum number of se_dp processes that handles traffic.
            - If not configured, defaults to the number of cpus on the se.
            - If decreased, it will only take effect after se reboot.
            - Allowed values are 1-128.
            - Field introduced in 20.1.1.
            - Allowed in basic(allowed values- 0) edition, essentials(allowed values- 0) edition, enterprise edition.
        type: int
    max_public_ips_per_lb:
        description:
            - Applicable to azure platform only.
            - Maximum number of public ips per azure lb.
            - Field introduced in 17.2.12, 18.1.2.
            - Default value when not specified in API or module is interpreted by Avi Controller as 30.
        version_added: "2.9"
        type: int
    max_queues_per_vnic:
        description:
            - Maximum number of queues per vnic setting to '0' utilises all queues that are distributed across dispatcher cores.
            - Allowed values are 0,1,2,4,8,16.
            - Field introduced in 18.2.7, 20.1.1.
            - Allowed in basic(allowed values- 1) edition, essentials(allowed values- 1) edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
        type: int
    max_rules_per_lb:
        description:
            - Applicable to azure platform only.
            - Maximum number of rules per azure lb.
            - Field introduced in 17.2.12, 18.1.2.
            - Default value when not specified in API or module is interpreted by Avi Controller as 150.
        version_added: "2.9"
        type: int
    max_scaleout_per_vs:
        description:
            - Maximum number of active service engines for the virtual service.
            - Allowed values are 1-64.
            - Default value when not specified in API or module is interpreted by Avi Controller as 4.
        type: int
    max_se:
        description:
            - Maximum number of services engines in this group.
            - Allowed values are 0-1000.
            - Default value when not specified in API or module is interpreted by Avi Controller as 10.
        type: int
    max_skb_frags:
        description:
            - Maximum of number of 4 kb pages allocated to the linux kernel gro subsystem for packet coalescing.
            - This parameter is limited to supported kernels only.
            - Requires se reboot.
            - Allowed values are 1-17.
            - Field introduced in 21.1.3.
            - Default value when not specified in API or module is interpreted by Avi Controller as 17.
        type: int
    max_vs_per_se:
        description:
            - Maximum number of virtual services that can be placed on a single service engine.
            - Allowed values are 1-1000.
            - Default value when not specified in API or module is interpreted by Avi Controller as 10.
        type: int
    mem_reserve:
        description:
            - Boolean flag to set mem_reserve.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    memory_for_config_update:
        description:
            - Indicates the percent of memory reserved for config updates.
            - Allowed values are 0-100.
            - Field introduced in 18.1.2.
            - Unit is percent.
            - Default value when not specified in API or module is interpreted by Avi Controller as 15.
        version_added: "2.9"
        type: int
    memory_per_se:
        description:
            - Amount of memory for each of the service engine virtual machines.
            - Changes to this setting do not affect existing ses.
            - Default value when not specified in API or module is interpreted by Avi Controller as 2048.
        type: int
    mgmt_network_ref:
        description:
            - Management network to use for avi service engines.
            - It is a reference to an object of type network.
        type: str
    mgmt_subnet:
        description:
            - Management subnet to use for avi service engines.
        type: dict
    min_cpu_usage:
        description:
            - When cpu usage on an se falls below the minimum threshold, virtual services hosted on the se may be consolidated onto other underutilized ses.
            - After consolidation, unused service engines may then be eligible for deletion.
            - Allowed values are 20-60.
            - Unit is percent.
            - Default value when not specified in API or module is interpreted by Avi Controller as 30.
        type: int
    min_scaleout_per_vs:
        description:
            - Minimum number of active service engines for the virtual service.
            - Allowed values are 1-64.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
        type: int
    min_se:
        description:
            - Minimum number of services engines in this group (relevant for se autorebalance only).
            - Allowed values are 0-1000.
            - Field introduced in 17.2.13,18.1.3,18.2.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
        version_added: "2.9"
        type: int
    minimum_connection_memory:
        description:
            - Indicates the percent of memory reserved for connections.
            - Allowed values are 0-100.
            - Field introduced in 18.1.2.
            - Unit is percent.
            - Default value when not specified in API or module is interpreted by Avi Controller as 20.
        version_added: "2.9"
        type: int
    minimum_required_config_memory:
        description:
            - Required available config memory to apply any configuration.
            - Allowed values are 0-90.
            - Field deprecated in 18.1.2.
            - Field introduced in 18.1.1.
            - Unit is percent.
        version_added: "2.9"
        type: int
    n_log_streaming_threads:
        description:
            - Number of threads to use for log streaming.
            - Allowed values are 1-100.
            - Field introduced in 17.2.12, 18.1.2.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
        version_added: "2.9"
        type: int
    name:
        description:
            - Name of the object.
        required: true
        type: str
    nat_flow_tcp_closed_timeout:
        description:
            - Idle timeout in seconds for nat tcp flows in closed state.
            - Allowed values are 1-3600.
            - Field deprecated in 18.2.5.
            - Field introduced in 18.2.5.
            - Unit is seconds.
        version_added: "2.9"
        type: int
    nat_flow_tcp_established_timeout:
        description:
            - Idle timeout in seconds for nat tcp flows in established state.
            - Allowed values are 1-3600.
            - Field deprecated in 18.2.5.
            - Field introduced in 18.2.5.
            - Unit is seconds.
        version_added: "2.9"
        type: int
    nat_flow_tcp_half_closed_timeout:
        description:
            - Idle timeout in seconds for nat tcp flows in half closed state.
            - Allowed values are 1-3600.
            - Field deprecated in 18.2.5.
            - Field introduced in 18.2.5.
            - Unit is seconds.
        version_added: "2.9"
        type: int
    nat_flow_tcp_handshake_timeout:
        description:
            - Idle timeout in seconds for nat tcp flows in handshake state.
            - Allowed values are 1-3600.
            - Field deprecated in 18.2.5.
            - Field introduced in 18.2.5.
            - Unit is seconds.
        version_added: "2.9"
        type: int
    nat_flow_udp_noresponse_timeout:
        description:
            - Idle timeout in seconds for nat udp flows in noresponse state.
            - Allowed values are 1-3600.
            - Field deprecated in 18.2.5.
            - Field introduced in 18.2.5.
            - Unit is seconds.
        version_added: "2.9"
        type: int
    nat_flow_udp_response_timeout:
        description:
            - Idle timeout in seconds for nat udp flows in response state.
            - Allowed values are 1-3600.
            - Field deprecated in 18.2.5.
            - Field introduced in 18.2.5.
            - Unit is seconds.
        version_added: "2.9"
        type: int
    netlink_poller_threads:
        description:
            - Number of threads to poll for netlink messages excluding the thread for default namespace.
            - Requires se reboot.
            - Allowed values are 1-32.
            - Field introduced in 21.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as 2.
        type: int
    netlink_sock_buf_size:
        description:
            - Socket buffer size for the netlink sockets.
            - Requires se reboot.
            - Allowed values are 1-128.
            - Field introduced in 21.1.1.
            - Unit is mega_bytes.
            - Default value when not specified in API or module is interpreted by Avi Controller as 4.
        type: int
    ngx_free_connection_stack:
        description:
            - Free the connection stack.
            - Field introduced in 21.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    non_significant_log_throttle:
        description:
            - This setting limits the number of non-significant logs generated per second per core on this se.
            - Default is 100 logs per second.
            - Set it to zero (0) to deactivate throttling.
            - Field introduced in 17.1.3.
            - Unit is per_second.
            - Default value when not specified in API or module is interpreted by Avi Controller as 100.
        type: int
    ns_helper_deq_interval_msec:
        description:
            - Dequeue interval for receive queue from ns helper.
            - Allowed values are 1-1000.
            - Field introduced in 21.1.1.
            - Unit is milliseconds.
            - Allowed in basic edition, essentials edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 20.
        type: int
    num_dispatcher_cores:
        description:
            - Number of dispatcher cores (0,1,2,4,8 or 16).
            - If set to 0, then number of dispatcher cores is deduced automatically.requires se reboot.
            - Allowed values are 0,1,2,4,8,16.
            - Field introduced in 17.2.12, 18.1.3, 18.2.1.
            - Allowed in basic(allowed values- 0) edition, essentials(allowed values- 0) edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        version_added: "2.9"
        type: int
    num_dispatcher_queues:
        description:
            - Number of queues to each dispatcher.
            - Allowed values are 2-8.
            - Special values are 0 - auto-compute, 1 - single-queue.
            - Field introduced in 21.1.3.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
        type: int
    num_flow_cores_sum_changes_to_ignore:
        description:
            - Number of changes in num flow cores sum to ignore.
            - Default value when not specified in API or module is interpreted by Avi Controller as 8.
        type: int
    objsync_config:
        description:
            - Configuration knobs for interse object distribution.
            - Field introduced in 20.1.3.
        type: dict
    objsync_port:
        description:
            - Tcp port on se management interface for interse object distribution.
            - Supported only for externally managed security groups.
            - Not supported on full access deployments.
            - Requires se reboot.
            - Field introduced in 20.1.3.
            - Default value when not specified in API or module is interpreted by Avi Controller as 9001.
        type: int
    openstack_availability_zone:
        description:
            - Field deprecated in 17.1.1.
        type: str
    openstack_availability_zones:
        description:
            - Field introduced in 17.1.1.
            - Maximum of 5 items allowed.
        type: list
    openstack_mgmt_network_name:
        description:
            - Avi management network name.
        type: str
    openstack_mgmt_network_uuid:
        description:
            - Management network uuid.
        type: str
    os_reserved_memory:
        description:
            - Amount of extra memory to be reserved for use by the operating system on a service engine.
            - Unit is mb.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    pcap_tx_mode:
        description:
            - Determines the pcap transmit mode of operation.
            - Requires se reboot.
            - Enum options - PCAP_TX_AUTO, PCAP_TX_SOCKET, PCAP_TX_RING.
            - Field introduced in 18.2.8, 20.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as PCAP_TX_AUTO.
        type: str
    pcap_tx_ring_rd_balancing_factor:
        description:
            - In pcap mode, reserve a configured portion of tx ring resources for itself and the remaining portion for the rx ring to achieve better balance in
            - terms of queue depth.
            - Requires se reboot.
            - Allowed values are 10-100.
            - Field introduced in 20.1.3.
            - Unit is percent.
            - Default value when not specified in API or module is interpreted by Avi Controller as 10.
        type: int
    per_app:
        description:
            - Per-app se mode is designed for deploying dedicated load balancers per app (vs).
            - In this mode, each se is limited to a max of 2 vss.
            - Vcpus in per-app ses count towards licensing usage at 25% rate.
            - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    per_vs_admission_control:
        description:
            - Enable/disable per vs level admission control.enabling this feature will cause the connection and packet throttling on a particular vs that has
            - high packet buffer consumption.
            - Field introduced in 20.1.3.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    placement_mode:
        description:
            - If placement mode is 'auto', virtual services are automatically placed on service engines.
            - Enum options - PLACEMENT_MODE_AUTO.
            - Default value when not specified in API or module is interpreted by Avi Controller as PLACEMENT_MODE_AUTO.
        type: str
    realtime_se_metrics:
        description:
            - Enable or deactivate real time se metrics.
        type: dict
    reboot_on_panic:
        description:
            - Reboot the vm or host on kernel panic.
            - Field introduced in 18.2.5.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        version_added: "2.9"
        type: bool
    reboot_on_stop:
        description:
            - Reboot the system if the se is stopped.
            - Field deprecated in 18.2.5.
        version_added: "2.9"
        type: bool
    resync_time_interval:
        description:
            - Time interval to re-sync se's time with wall clock time.
            - Allowed values are 8-600000.
            - Field introduced in 20.1.1.
            - Unit is milliseconds.
            - Default value when not specified in API or module is interpreted by Avi Controller as 65536.
        type: int
    sdb_flush_interval:
        description:
            - Sdb pipeline flush interval.
            - Allowed values are 1-10000.
            - Field introduced in 21.1.1.
            - Unit is milliseconds.
            - Allowed in basic edition, essentials edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 100.
        type: int
    sdb_pipeline_size:
        description:
            - Sdb pipeline size.
            - Allowed values are 1-10000.
            - Field introduced in 21.1.1.
            - Allowed in basic edition, essentials edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 100.
        type: int
    sdb_scan_count:
        description:
            - Sdb scan count.
            - Allowed values are 1-1000.
            - Field introduced in 21.1.1.
            - Allowed in basic edition, essentials edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1000.
        type: int
    se_bandwidth_type:
        description:
            - Select the se bandwidth for the bandwidth license.
            - Enum options - SE_BANDWIDTH_UNLIMITED, SE_BANDWIDTH_25M, SE_BANDWIDTH_200M, SE_BANDWIDTH_1000M, SE_BANDWIDTH_10000M.
            - Field introduced in 17.2.5.
            - Allowed in basic(allowed values- se_bandwidth_unlimited) edition, essentials(allowed values- se_bandwidth_unlimited) edition, enterprise edition.
        version_added: "2.5"
        type: str
    se_delayed_flow_delete:
        description:
            - Delay the cleanup of flowtable entry.
            - To be used under surveillance of avi support.
            - Field introduced in 20.1.2.
            - Allowed in basic(allowed values- true) edition, essentials(allowed values- true) edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    se_deprovision_delay:
        description:
            - Duration to preserve unused service engine virtual machines before deleting them.
            - If traffic to a virtual service were to spike up abruptly, this se would still be available to be utilized again rather than creating a new se.
            - If this value is set to 0, controller will never delete any ses and administrator has to manually cleanup unused ses.
            - Allowed values are 0-525600.
            - Unit is min.
            - Default value when not specified in API or module is interpreted by Avi Controller as 120.
        type: int
    se_dos_profile:
        description:
            - Dosthresholdprofile settings for serviceenginegroup.
        type: dict
    se_dp_hm_drops:
        description:
            - Internal only.
            - Used to simulate se - se hb failure.
            - Field introduced in 20.1.3.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    se_dp_if_state_poll_interval:
        description:
            - Number of jiffies between polling interface state.
            - Field introduced in 21.1.3.
            - Allowed in basic edition, essentials edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 10.
        type: int
    se_dp_isolation:
        description:
            - Toggle support to run se datapath instances in isolation on exclusive cpus.
            - This improves latency and performance.
            - However, this could reduce the total number of se_dp instances created on that se instance.
            - Supported for >= 8 cpus.
            - Requires se reboot.
            - Field introduced in 20.1.4.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    se_dp_isolation_num_non_dp_cpus:
        description:
            - Number of cpus for non se-dp tasks in se datapath isolation mode.
            - Translates total cpus minus 'num_non_dp_cpus' for datapath use.
            - It is recommended to reserve an even number of cpus for hyper-threaded processors.
            - Requires se reboot.
            - Allowed values are 1-8.
            - Special values are 0- auto.
            - Field introduced in 20.1.4.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    se_dp_log_nf_enqueue_percent:
        description:
            - Internal buffer full indicator on the service engine beyond which the unfiltered logs are abandoned.
            - Field introduced in 21.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as 70.
        type: int
    se_dp_log_udf_enqueue_percent:
        description:
            - Internal buffer full indicator on the service engine beyond which the user filtered logs are abandoned.
            - Field introduced in 21.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as 90.
        type: int
    se_dp_max_hb_version:
        description:
            - The highest supported se-se heartbeat protocol version.
            - This version is reported by secondary se to primary se in heartbeat response messages.
            - Allowed values are 1-3.
            - Field introduced in 20.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as 3.
        type: int
    se_dp_vnic_queue_stall_event_sleep:
        description:
            - Time (in seconds) service engine waits for after generating a vnic transmit queue stall event before resetting thenic.
            - Field introduced in 18.2.5.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        version_added: "2.9"
        type: int
    se_dp_vnic_queue_stall_threshold:
        description:
            - Number of consecutive transmit failures to look for before generating a vnic transmit queue stall event.
            - Field introduced in 18.2.5.
            - Default value when not specified in API or module is interpreted by Avi Controller as 2000.
        version_added: "2.9"
        type: int
    se_dp_vnic_queue_stall_timeout:
        description:
            - Time (in milliseconds) to wait for network/nic recovery on detecting a transmit queue stall after which service engine resets the nic.
            - Field introduced in 18.2.5.
            - Default value when not specified in API or module is interpreted by Avi Controller as 10000.
        version_added: "2.9"
        type: int
    se_dp_vnic_restart_on_queue_stall_count:
        description:
            - Number of consecutive transmit queue stall events in se_dp_vnic_stall_se_restart_window to look for before restarting se.
            - Field introduced in 18.2.5.
            - Default value when not specified in API or module is interpreted by Avi Controller as 3.
        version_added: "2.9"
        type: int
    se_dp_vnic_stall_se_restart_window:
        description:
            - Window of time (in seconds) during which se_dp_vnic_restart_on_queue_stall_count number of consecutive stalls results in a se restart.
            - Field introduced in 18.2.5.
            - Default value when not specified in API or module is interpreted by Avi Controller as 3600.
        version_added: "2.9"
        type: int
    se_dpdk_pmd:
        description:
            - Determines if dpdk pool mode driver should be used or not   0  automatically determine based on hypervisor/nic type 1  unconditionally use dpdk
            - poll mode driver 2  don't use dpdk poll mode driver.requires se reboot.
            - Allowed values are 0-2.
            - Field introduced in 18.1.3.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        version_added: "2.9"
        type: int
    se_dump_core_on_assert:
        description:
            - Enable core dump on assert.
            - Field introduced in 21.1.3.
            - Allowed in basic edition, essentials edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    se_emulated_cores:
        description:
            - Use this to emulate more/less cpus than is actually available.
            - One datapath process is started for each core.
            - Field introduced in 21.1.3.
            - Allowed in basic(allowed values- 0) edition, essentials(allowed values- 0) edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    se_flow_probe_retries:
        description:
            - Flow probe retry count if no replies are received.requires se reboot.
            - Allowed values are 0-5.
            - Field introduced in 18.1.4, 18.2.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as 2.
        version_added: "2.9"
        type: int
    se_flow_probe_retry_timer:
        description:
            - Timeout in milliseconds for flow probe retries.requires se reboot.
            - Allowed values are 20-50.
            - Field introduced in 18.2.5.
            - Unit is milliseconds.
            - Default value when not specified in API or module is interpreted by Avi Controller as 40.
        version_added: "2.9"
        type: int
    se_flow_probe_timer:
        description:
            - Timeout in milliseconds for flow probe entries.
            - Allowed values are 10-200.
            - Field deprecated in 18.2.5.
            - Field introduced in 18.1.4, 18.2.1.
            - Unit is milliseconds.
        version_added: "2.9"
        type: int
    se_group_analytics_policy:
        description:
            - Analytics policy for serviceenginegroup.
            - Field introduced in 20.1.3.
        type: dict
    se_hyperthreaded_mode:
        description:
            - Controls the distribution of se data path processes on cpus which support hyper-threading.
            - Requires hyper-threading to be enabled at host level.
            - Requires se reboot.
            - For more details please refer to se placement kb.
            - Enum options - SE_CPU_HT_AUTO, SE_CPU_HT_SPARSE_DISPATCHER_PRIORITY, SE_CPU_HT_SPARSE_PROXY_PRIORITY, SE_CPU_HT_PACKED_CORES.
            - Field introduced in 20.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as SE_CPU_HT_AUTO.
        type: str
    se_ip_encap_ipc:
        description:
            - Determines if se-se ipc messages are encapsulated in an ip header       0        automatically determine based on hypervisor type    1        use
            - ip encap unconditionally    ~[0,1]   don't use ip encaprequires se reboot.
            - Field introduced in 20.1.3.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    se_ipc_udp_port:
        description:
            - Udp port for se_dp ipc in docker bridge mode.
            - Field deprecated in 20.1.1.
            - Field introduced in 17.1.2.
        version_added: "2.4"
        type: int
    se_kni_burst_factor:
        description:
            - This knob controls the resource availability and burst size used between se datapath and kni.
            - This helps in minimising packet drops when there is higher kni traffic (non-vip traffic from and to linux).
            - The factor takes the following values      0-default.
            - 1-doubles the burst size and kni resources.
            - 2-quadruples the burst size and kni resources.
            - Allowed values are 0-2.
            - Field introduced in 18.2.6.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    se_l3_encap_ipc:
        description:
            - Determines if se-se ipc messages use se interface ip instead of vip        0        automatically determine based on hypervisor type    1
            - use se interface ip unconditionally    ~[0,1]   don't use se interface iprequires se reboot.
            - Field introduced in 20.1.3.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    se_log_buffer_app_blocking_dequeue:
        description:
            - Internal flag that blocks dataplane until all application logs are flushed to log-agent process.
            - Field introduced in 21.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    se_log_buffer_conn_blocking_dequeue:
        description:
            - Internal flag that blocks dataplane until all connection logs are flushed to log-agent process.
            - Field introduced in 21.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    se_log_buffer_events_blocking_dequeue:
        description:
            - Internal flag that blocks dataplane until all outstanding events are flushed to log-agent process.
            - Field introduced in 21.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    se_lro:
        description:
            - Enable or disable large receive optimization for vnics.
            - Requires se reboot.
            - Field introduced in 18.2.5.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        version_added: "2.9"
        type: bool
    se_mp_ring_retry_count:
        description:
            - The retry count for the multi-producer enqueue before yielding the cpu.
            - To be used under surveillance of avi support.
            - Field introduced in 20.1.3.
            - Allowed in basic(allowed values- 500) edition, essentials(allowed values- 500) edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 500.
        type: int
    se_mtu:
        description:
            - Mtu for the vnics of ses in the se group.
            - Allowed values are 512-9000.
            - Field introduced in 18.2.8, 20.1.1.
        type: int
    se_name_prefix:
        description:
            - Prefix to use for virtual machine name of service engines.
            - Default value when not specified in API or module is interpreted by Avi Controller as Avi.
        type: str
    se_packet_buffer_max:
        description:
            - Internal use only.
            - Used to artificially reduce the available number of packet buffers.
            - Field introduced in 21.1.3.
            - Allowed in basic edition, essentials edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    se_pcap_lookahead:
        description:
            - Enables lookahead mode of packet receive in pcap mode.
            - Introduced to overcome an issue with hv_netvsc driver.
            - Lookahead mode attempts to ensure that application and kernel's view of the receive rings are consistent.
            - Field introduced in 18.2.3.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        version_added: "2.9"
        type: bool
    se_pcap_pkt_count:
        description:
            - Max number of packets the pcap interface can hold and if the value is 0 the optimum value will be chosen.
            - The optimum value will be chosen based on se-memory, cloud type and number of interfaces.requires se reboot.
            - Field introduced in 18.2.5.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        version_added: "2.9"
        type: int
    se_pcap_pkt_sz:
        description:
            - Max size of each packet in the pcap interface.
            - Requires se reboot.
            - Field introduced in 18.2.5.
            - Default value when not specified in API or module is interpreted by Avi Controller as 69632.
        version_added: "2.9"
        type: int
    se_pcap_qdisc_bypass:
        description:
            - Bypass the kernel's traffic control layer, to deliver packets directly to the driver.
            - Enabling this feature results in egress packets not being captured in host tcpdump.
            - Note   brief packet reordering or loss may occur upon toggle.
            - Field introduced in 18.2.6.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    se_pcap_reinit_frequency:
        description:
            - Frequency in seconds at which periodically a pcap reinit check is triggered.
            - May be used in conjunction with the configuration pcap_reinit_threshold.
            - (valid range   15 mins - 12 hours, 0 - disables).
            - Allowed values are 900-43200.
            - Special values are 0- disable.
            - Field introduced in 17.2.13, 18.1.3, 18.2.1.
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        version_added: "2.9"
        type: int
    se_pcap_reinit_threshold:
        description:
            - Threshold for input packet receive errors in pcap mode exceeding which a pcap reinit is triggered.
            - If not set, an unconditional reinit is performed.
            - This value is checked every pcap_reinit_frequency interval.
            - Field introduced in 17.2.13, 18.1.3, 18.2.1.
            - Unit is metric_count.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        version_added: "2.9"
        type: int
    se_probe_port:
        description:
            - Tcp port on se where echo service will be run.
            - Field introduced in 17.2.2.
            - Default value when not specified in API or module is interpreted by Avi Controller as 7.
        version_added: "2.5"
        type: int
    se_remote_punt_udp_port:
        description:
            - Udp port for punted packets in docker bridge mode.
            - Field deprecated in 20.1.1.
            - Field introduced in 17.1.2.
        version_added: "2.4"
        type: int
    se_rl_prop:
        description:
            - Rate limiter properties.
            - Field introduced in 20.1.1.
        type: dict
    se_routing:
        description:
            - Enable routing via service engine datapath.
            - When disabled, routing is done by the linux kernel.
            - Ip routing needs to be enabled in service engine group for se routing to be effective.
            - Field deprecated in 18.2.5.
            - Field introduced in 18.2.3.
        version_added: "2.9"
        type: bool
    se_rum_sampling_nav_interval:
        description:
            - Minimum time to wait on server between taking sampleswhen sampling the navigation timing data from the end user client.
            - Field introduced in 18.2.6.
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
        type: int
    se_rum_sampling_nav_percent:
        description:
            - Percentage of navigation timing data from the end user client, used for sampling to get client insights.
            - Field introduced in 18.2.6.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
        type: int
    se_rum_sampling_res_interval:
        description:
            - Minimum time to wait on server between taking sampleswhen sampling the resource timing data from the end user client.
            - Field introduced in 18.2.6.
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 2.
        type: int
    se_rum_sampling_res_percent:
        description:
            - Percentage of resource timing data from the end user client used for sampling to get client insight.
            - Field introduced in 18.2.6.
            - Default value when not specified in API or module is interpreted by Avi Controller as 100.
        type: int
    se_sb_dedicated_core:
        description:
            - Sideband traffic will be handled by a dedicated core.requires se reboot.
            - Field introduced in 16.5.2, 17.1.9, 17.2.3.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        version_added: "2.5"
        type: bool
    se_sb_threads:
        description:
            - Number of sideband threads per se.requires se reboot.
            - Allowed values are 1-128.
            - Field introduced in 16.5.2, 17.1.9, 17.2.3.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
        version_added: "2.5"
        type: int
    se_thread_multiplier:
        description:
            - Multiplier for se threads based on vcpu.
            - Allowed values are 1-10.
            - Allowed in basic(allowed values- 1) edition, essentials(allowed values- 1) edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
        type: int
    se_tracert_port_range:
        description:
            - Traceroute port range.
            - Field introduced in 17.2.8.
        version_added: "2.9"
        type: dict
    se_tunnel_mode:
        description:
            - Determines if direct secondary return (dsr) from secondary se is active or not  0  automatically determine based on hypervisor type.
            - 1  enable tunnel mode - dsr is unconditionally disabled.
            - 2  disable tunnel mode - dsr is unconditionally enabled.
            - Tunnel mode can be enabled or disabled at run-time.
            - Allowed values are 0-2.
            - Field introduced in 17.1.1.
            - Allowed in basic(allowed values- 0) edition, essentials(allowed values- 0) edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    se_tunnel_udp_port:
        description:
            - Udp port for tunneled packets from secondary to primary se in docker bridge mode.requires se reboot.
            - Field introduced in 17.1.3.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1550.
        type: int
    se_tx_batch_size:
        description:
            - Number of packets to batch for transmit to the nic.
            - Requires se reboot.
            - Field introduced in 18.2.5.
            - Default value when not specified in API or module is interpreted by Avi Controller as 64.
        version_added: "2.9"
        type: int
    se_txq_threshold:
        description:
            - Once the tx queue of the dispatcher reaches this threshold, hardware queues are not polled for further packets.
            - To be used under surveillance of avi support.
            - Allowed values are 512-32768.
            - Field introduced in 20.1.2.
            - Allowed in basic(allowed values- 2048) edition, essentials(allowed values- 2048) edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 2048.
        type: int
    se_udp_encap_ipc:
        description:
            - Determines if se-se ipc messages are encapsulated in a udp header  0  automatically determine based on hypervisor type.
            - 1  use udp encap unconditionally.requires se reboot.
            - Allowed values are 0-1.
            - Field introduced in 17.1.2.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        version_added: "2.4"
        type: int
    se_use_dpdk:
        description:
            - Determines if dpdk library should be used or not   0  automatically determine based on hypervisor type 1  use dpdk if pcap is not enabled 2
            - don't use dpdk.
            - Allowed values are 0-2.
            - Field introduced in 18.1.3.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        version_added: "2.9"
        type: int
    se_vnic_tx_sw_queue_flush_frequency:
        description:
            - Configure the frequency in milliseconds of software transmit spillover queue flush when enabled.
            - This is necessary to flush any packets in the spillover queue in the absence of a packet transmit in the normal course of operation.
            - Allowed values are 50-500.
            - Special values are 0- disable.
            - Field introduced in 20.1.1.
            - Unit is milliseconds.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    se_vnic_tx_sw_queue_size:
        description:
            - Configure the size of software transmit spillover queue when enabled.
            - Requires se reboot.
            - Allowed values are 128-2048.
            - Field introduced in 20.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as 256.
        type: int
    se_vs_hb_max_pkts_in_batch:
        description:
            - Maximum number of aggregated vs heartbeat packets to send in a batch.
            - Allowed values are 1-256.
            - Field introduced in 17.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as 64.
        type: int
    se_vs_hb_max_vs_in_pkt:
        description:
            - Maximum number of virtualservices for which heartbeat messages are aggregated in one packet.
            - Allowed values are 1-1024.
            - Field introduced in 17.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as 256.
        type: int
    self_se_election:
        description:
            - Enable ses to elect a primary amongst themselves in the absence of a connectivity to controller.
            - Field introduced in 18.1.2.
            - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        version_added: "2.9"
        type: bool
    send_se_ready_timeout:
        description:
            - Timeout for sending se_ready without ns helper registration completion.
            - Allowed values are 10-600.
            - Field introduced in 21.1.1.
            - Unit is seconds.
            - Allowed in basic edition, essentials edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 300.
        type: int
    service_ip6_subnets:
        description:
            - Ipv6 subnets assigned to the se group.
            - Required for vs group placement.
            - Field introduced in 18.1.1.
            - Maximum of 128 items allowed.
        version_added: "2.9"
        type: list
    service_ip_subnets:
        description:
            - Subnets assigned to the se group.
            - Required for vs group placement.
            - Field introduced in 17.1.1.
            - Maximum of 128 items allowed.
        type: list
    shm_minimum_config_memory:
        description:
            - Minimum required shared memory to apply any configuration.
            - Allowed values are 0-100.
            - Field introduced in 18.1.2.
            - Unit is mb.
            - Default value when not specified in API or module is interpreted by Avi Controller as 4.
        version_added: "2.9"
        type: int
    significant_log_throttle:
        description:
            - This setting limits the number of significant logs generated per second per core on this se.
            - Default is 100 logs per second.
            - Set it to zero (0) to deactivate throttling.
            - Field introduced in 17.1.3.
            - Unit is per_second.
            - Default value when not specified in API or module is interpreted by Avi Controller as 100.
        type: int
    ssl_preprocess_sni_hostname:
        description:
            - (beta) preprocess ssl client hello for sni hostname extension.if set to true, this will apply sni child's ssl protocol(s), if they are different
            - from sni parent's allowed ssl protocol(s).
            - Field introduced in 17.2.12, 18.1.3.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        version_added: "2.9"
        type: bool
    ssl_sess_cache_per_vs:
        description:
            - Number of ssl sessions that can be cached per vs.
            - Field introduced in 21.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as 4096.
        type: int
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
        type: str
    transient_shared_memory_max:
        description:
            - The threshold for the transient shared config memory in the se.
            - Allowed values are 0-100.
            - Field introduced in 20.1.1.
            - Unit is percent.
            - Default value when not specified in API or module is interpreted by Avi Controller as 30.
        type: int
    udf_log_throttle:
        description:
            - This setting limits the number of udf logs generated per second per core on this se.
            - Udf logs are generated due to the configured client log filters or the rules with logging enabled.
            - Default is 100 logs per second.
            - Set it to zero (0) to deactivate throttling.
            - Field introduced in 17.1.3.
            - Unit is per_second.
            - Default value when not specified in API or module is interpreted by Avi Controller as 100.
        type: int
    upstream_connect_timeout:
        description:
            - Timeout for backend connection.
            - Field introduced in 21.1.1.
            - Unit is milliseconds.
            - Default value when not specified in API or module is interpreted by Avi Controller as 3600000.
        type: int
    upstream_connpool_enable:
        description:
            - Enable upstream connection pool,.
            - Field introduced in 21.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    upstream_read_timeout:
        description:
            - Timeout for data to be received from backend.
            - Field introduced in 21.1.1.
            - Unit is milliseconds.
            - Default value when not specified in API or module is interpreted by Avi Controller as 3600000.
        type: int
    upstream_send_timeout:
        description:
            - Timeout for upstream to become writable.
            - Field introduced in 21.1.1.
            - Unit is milliseconds.
            - Allowed in basic(allowed values- 3600000) edition, essentials(allowed values- 3600000) edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 3600000.
        type: int
    url:
        description:
            - Avi controller URL of the object.
        type: str
    use_hyperthreaded_cores:
        description:
            - Enables the use of hyper-threaded cores on se.
            - Requires se reboot.
            - Field introduced in 20.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    use_legacy_netlink:
        description:
            - Enable legacy model of netlink notifications.
            - Field introduced in 21.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    use_objsync:
        description:
            - Enable interse objsyc distribution framework.
            - Field introduced in 20.1.3.
            - Allowed in basic edition, essentials edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    use_standard_alb:
        description:
            - Use standard sku azure load balancer.
            - By default cloud level flag is set.
            - If not set, it inherits/uses the use_standard_alb flag from the cloud.
            - Field introduced in 18.2.3.
        version_added: "2.9"
        type: bool
    user_agent_cache_config:
        description:
            - Configuration for user-agent cache used in bot management.
            - Field introduced in 21.1.1.
        type: dict
    user_defined_metric_age:
        description:
            - Defines in seconds how long before an unused user-defined-metric is garbage collected.
            - Field introduced in 21.1.1.
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 60.
        type: int
    uuid:
        description:
            - Unique object identifier of the object.
        type: str
    vcenter_clusters:
        description:
            - Vcenterclusters settings for serviceenginegroup.
        type: dict
    vcenter_datastore_mode:
        description:
            - Enum options - VCENTER_DATASTORE_ANY, VCENTER_DATASTORE_LOCAL, VCENTER_DATASTORE_SHARED.
            - Default value when not specified in API or module is interpreted by Avi Controller as VCENTER_DATASTORE_ANY.
        type: str
    vcenter_datastores:
        description:
            - List of vcenterdatastore.
        type: list
    vcenter_datastores_include:
        description:
            - Boolean flag to set vcenter_datastores_include.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    vcenter_folder:
        description:
            - Folder to place all the service engine virtual machines in vcenter.
            - Default value when not specified in API or module is interpreted by Avi Controller as AviSeFolder.
        type: str
    vcenter_hosts:
        description:
            - Vcenterhosts settings for serviceenginegroup.
        type: dict
    vcenters:
        description:
            - Vcenter information for scoping at host/cluster level.
            - Field introduced in 20.1.1.
        type: list
    vcpus_per_se:
        description:
            - Number of vcpus for each of the service engine virtual machines.
            - Changes to this setting do not affect existing ses.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
        type: int
    vip_asg:
        description:
            - When vip_asg is set, vip configuration will be managed by avi.user will be able to configure vip_asg or vips individually at the time of create.
            - Field introduced in 17.2.12, 18.1.2.
        version_added: "2.9"
        type: dict
    vnic_dhcp_ip_check_interval:
        description:
            - Dhcp ip check interval.
            - Allowed values are 1-1000.
            - Field introduced in 21.1.1.
            - Unit is sec.
            - Allowed in basic edition, essentials edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 6.
        type: int
    vnic_dhcp_ip_max_retries:
        description:
            - Dhcp ip max retries.
            - Field introduced in 21.1.1.
            - Allowed in basic edition, essentials edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 10.
        type: int
    vnic_ip_delete_interval:
        description:
            - Wait interval before deleting ip.
            - Field introduced in 21.1.1.
            - Unit is sec.
            - Allowed in basic edition, essentials edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 5.
        type: int
    vnic_probe_interval:
        description:
            - Probe vnic interval.
            - Field introduced in 21.1.1.
            - Unit is sec.
            - Allowed in basic edition, essentials edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 5.
        type: int
    vnic_rpc_retry_interval:
        description:
            - Time interval for retrying the failed vnic rpc requests.
            - Field introduced in 21.1.1.
            - Unit is sec.
            - Allowed in basic edition, essentials edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 5.
        type: int
    vnicdb_cmd_history_size:
        description:
            - Size of vnicdb command history.
            - Allowed values are 0-65535.
            - Field introduced in 21.1.1.
            - Allowed in basic edition, essentials edition, enterprise edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 256.
        type: int
    vs_host_redundancy:
        description:
            - Ensure primary and secondary service engines are deployed on different physical hosts.
            - Allowed in basic(allowed values- true) edition, essentials(allowed values- true) edition, enterprise edition.
            - Special default for basic edition is true, essentials edition is true, enterprise is true.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    vs_scalein_timeout:
        description:
            - Time to wait for the scaled in se to drain existing flows before marking the scalein done.
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 30.
        type: int
    vs_scalein_timeout_for_upgrade:
        description:
            - During se upgrade, time to wait for the scaled-in se to drain existing flows before marking the scalein done.
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 30.
        type: int
    vs_scaleout_timeout:
        description:
            - Time to wait for the scaled out se to become ready before marking the scaleout done.
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 600.
        type: int
    vs_se_scaleout_additional_wait_time:
        description:
            - Wait time for sending scaleout ready notification after virtual service is marked up.
            - In certain deployments, there may be an additional delay to accept traffic.
            - For example, for bgp, some time is needed for route advertisement.
            - Allowed values are 0-20.
            - Field introduced in 18.1.5,18.2.1.
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        version_added: "2.9"
        type: int
    vs_se_scaleout_ready_timeout:
        description:
            - Timeout in seconds for service engine to sendscaleout ready notification of a virtual service.
            - Allowed values are 0-90.
            - Field introduced in 18.1.5,18.2.1.
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 60.
        version_added: "2.9"
        type: int
    vs_switchover_timeout:
        description:
            - During se upgrade in a legacy active/standby segroup, time to wait for the new primary se to accept flows before marking the switchover done.
            - Field introduced in 17.2.13,18.1.4,18.2.1.
            - Unit is sec.
            - Default value when not specified in API or module is interpreted by Avi Controller as 300.
        version_added: "2.9"
        type: int
    vss_placement:
        description:
            - Parameters to place virtual services on only a subset of the cores of an se.
            - Field introduced in 17.2.5.
        version_added: "2.5"
        type: dict
    vss_placement_enabled:
        description:
            - If set, virtual services will be placed on only a subset of the cores of an se.
            - Field introduced in 18.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        version_added: "2.9"
        type: bool
    waf_learning_interval:
        description:
            - Frequency with which se publishes waf learning.
            - Allowed values are 1-43200.
            - Field deprecated in 18.2.3.
            - Field introduced in 18.1.2.
            - Unit is min.
        version_added: "2.9"
        type: int
    waf_learning_memory:
        description:
            - Amount of memory reserved on se for waf learning.
            - This can be atmost 5% of se memory.
            - Field deprecated in 18.2.3.
            - Field introduced in 18.1.2.
            - Unit is mb.
        version_added: "2.9"
        type: int
    waf_mempool:
        description:
            - Enable memory pool for waf.requires se reboot.
            - Field introduced in 17.2.3.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        version_added: "2.5"
        type: bool
    waf_mempool_size:
        description:
            - Memory pool size used for waf.requires se reboot.
            - Field introduced in 17.2.3.
            - Unit is kb.
            - Default value when not specified in API or module is interpreted by Avi Controller as 64.
        version_added: "2.5"
        type: int


extends_documentation_fragment:
    - avi
'''

EXAMPLES = """
- hosts: all
  vars:
    avi_credentials:
      username: "admin"
      password: "something"
      controller: "192.168.15.18"
      api_version: "21.1.1"

- name: Example to create ServiceEngineGroup object
  avi_serviceenginegroup:
    avi_credentials: "{{ avi_credentials }}"
    state: present
    name: sample_serviceenginegroup
"""

RETURN = '''
obj:
    description: ServiceEngineGroup (api/serviceenginegroup) object
    returned: success, changed
    type: dict
'''

from ansible.module_utils.basic import AnsibleModule
try:
    from avi.sdk.utils.ansible_utils import avi_common_argument_spec
    from avi.sdk.utils.ansible_utils import (
        avi_ansible_api, avi_common_argument_spec)
    HAS_AVI = True
except ImportError:
    HAS_AVI = False


def main():
    argument_specs = dict(
        state=dict(default='present',
                   choices=['absent', 'present']),
        avi_api_update_method=dict(default='put',
                                   choices=['put', 'patch']),
        avi_api_patch_op=dict(choices=['add', 'replace', 'delete', 'remove']),
        avi_patch_path=dict(type='str',),
        avi_patch_value=dict(type='str',),
        accelerated_networking=dict(type='bool',),
        active_standby=dict(type='bool',),
        additional_config_memory=dict(type='int',),
        advertise_backend_networks=dict(type='bool',),
        aggressive_failure_detection=dict(type='bool',),
        algo=dict(type='str',),
        allow_burst=dict(type='bool',),
        app_cache_percent=dict(type='int',),
        app_cache_threshold=dict(type='int',),
        app_learning_memory_percent=dict(type='int',),
        archive_shm_limit=dict(type='int',),
        async_ssl=dict(type='bool',),
        async_ssl_threads=dict(type='int',),
        auto_rebalance=dict(type='bool',),
        auto_rebalance_capacity_per_se=dict(type='list',),
        auto_rebalance_criteria=dict(type='list',),
        auto_rebalance_interval=dict(type='int',),
        auto_redistribute_active_standby_load=dict(type='bool',),
        availability_zone_refs=dict(type='list',),
        baremetal_dispatcher_handles_flows=dict(type='bool',),
        bgp_peer_monitor_failover_enabled=dict(type='bool',),
        bgp_state_update_interval=dict(type='int',),
        buffer_se=dict(type='int',),
        cloud_ref=dict(type='str',),
        compress_ip_rules_for_each_ns_subnet=dict(type='bool',),
        config_debugs_on_all_cores=dict(type='bool',),
        configpb_attributes=dict(type='dict',),
        connection_memory_percentage=dict(type='int',),
        core_shm_app_cache=dict(type='bool',),
        core_shm_app_learning=dict(type='bool',),
        cpu_reserve=dict(type='bool',),
        cpu_socket_affinity=dict(type='bool',),
        custom_securitygroups_data=dict(type='list',),
        custom_securitygroups_mgmt=dict(type='list',),
        custom_tag=dict(type='list',),
        data_network_id=dict(type='str',),
        datascript_timeout=dict(type='int',),
        deactivate_ipv6_discovery=dict(type='bool',),
        deactivate_kni_filtering_at_dispatcher=dict(type='bool',),
        dedicated_dispatcher_core=dict(type='bool',),
        description=dict(type='str',),
        disable_avi_securitygroups=dict(type='bool',),
        disable_csum_offloads=dict(type='bool',),
        disable_flow_probes=dict(type='bool',),
        disable_gro=dict(type='bool',),
        disable_se_memory_check=dict(type='bool',),
        disable_tso=dict(type='bool',),
        disk_per_se=dict(type='int',),
        distribute_load_active_standby=dict(type='bool',),
        distribute_queues=dict(type='bool',),
        distribute_vnics=dict(type='bool',),
        downstream_send_timeout=dict(type='int',),
        dp_aggressive_deq_interval_msec=dict(type='int',),
        dp_aggressive_enq_interval_msec=dict(type='int',),
        dp_aggressive_hb_frequency=dict(type='int',),
        dp_aggressive_hb_timeout_count=dict(type='int',),
        dp_deq_interval_msec=dict(type='int',),
        dp_enq_interval_msec=dict(type='int',),
        dp_hb_frequency=dict(type='int',),
        dp_hb_timeout_count=dict(type='int',),
        enable_gratarp_permanent=dict(type='bool',),
        enable_hsm_log=dict(type='bool',),
        enable_hsm_priming=dict(type='bool',),
        enable_multi_lb=dict(type='bool',),
        enable_pcap_tx_ring=dict(type='bool',),
        enable_routing=dict(type='bool',),
        enable_vip_on_all_interfaces=dict(type='bool',),
        enable_vmac=dict(type='bool',),
        ephemeral_portrange_end=dict(type='int',),
        ephemeral_portrange_start=dict(type='int',),
        extra_config_multiplier=dict(type='float',),
        extra_shared_config_memory=dict(type='int',),
        floating_intf_ip=dict(type='list',),
        floating_intf_ip_se_2=dict(type='list',),
        flow_table_new_syn_max_entries=dict(type='int',),
        free_list_size=dict(type='int',),
        gcp_config=dict(type='dict',),
        gratarp_permanent_periodicity=dict(type='int',),
        ha_mode=dict(type='str',),
        handle_per_pkt_attack=dict(type='bool',),
        hardwaresecuritymodulegroup_ref=dict(type='str',),
        heap_minimum_config_memory=dict(type='int',),
        hm_on_standby=dict(type='bool',),
        host_attribute_key=dict(type='str',),
        host_attribute_value=dict(type='str',),
        host_gateway_monitor=dict(type='bool',),
        http_rum_console_log=dict(type='bool',),
        http_rum_min_content_length=dict(type='int',),
        hybrid_rss_mode=dict(type='bool',),
        hypervisor=dict(type='str',),
        ignore_docker_mac_change=dict(type='bool',),
        ignore_rtt_threshold=dict(type='int',),
        ingress_access_data=dict(type='str',),
        ingress_access_mgmt=dict(type='str',),
        instance_flavor=dict(type='str',),
        instance_flavor_info=dict(type='dict',),
        iptables=dict(type='list',),
        kni_allowed_server_ports=dict(type='list',),
        l7_conns_per_core=dict(type='int',),
        l7_resvd_listen_conns_per_core=dict(type='int',),
        labels=dict(type='list',),
        lbaction_num_requests_to_dispatch=dict(type='int',),
        lbaction_rq_per_request_max_retries=dict(type='int',),
        least_load_core_selection=dict(type='bool',),
        license_tier=dict(type='str',),
        license_type=dict(type='str',),
        log_agent_compress_logs=dict(type='bool',),
        log_agent_debug_enabled=dict(type='bool',),
        log_agent_file_sz_appl=dict(type='int',),
        log_agent_file_sz_conn=dict(type='int',),
        log_agent_file_sz_debug=dict(type='int',),
        log_agent_file_sz_event=dict(type='int',),
        log_agent_log_storage_min_sz=dict(type='int',),
        log_agent_max_concurrent_rsync=dict(type='int',),
        log_agent_max_storage_excess_percent=dict(type='int',),
        log_agent_max_storage_ignore_percent=dict(type='float',),
        log_agent_min_storage_per_vs=dict(type='int',),
        log_agent_sleep_interval=dict(type='int',),
        log_agent_trace_enabled=dict(type='bool',),
        log_agent_unknown_vs_timer=dict(type='int',),
        log_disksz=dict(type='int',),
        log_malloc_failure=dict(type='bool',),
        log_message_max_file_list_size=dict(type='int',),
        markers=dict(type='list',),
        max_concurrent_external_hm=dict(type='int',),
        max_cpu_usage=dict(type='int',),
        max_memory_per_mempool=dict(type='int',),
        max_num_se_dps=dict(type='int',),
        max_public_ips_per_lb=dict(type='int',),
        max_queues_per_vnic=dict(type='int',),
        max_rules_per_lb=dict(type='int',),
        max_scaleout_per_vs=dict(type='int',),
        max_se=dict(type='int',),
        max_skb_frags=dict(type='int',),
        max_vs_per_se=dict(type='int',),
        mem_reserve=dict(type='bool',),
        memory_for_config_update=dict(type='int',),
        memory_per_se=dict(type='int',),
        mgmt_network_ref=dict(type='str',),
        mgmt_subnet=dict(type='dict',),
        min_cpu_usage=dict(type='int',),
        min_scaleout_per_vs=dict(type='int',),
        min_se=dict(type='int',),
        minimum_connection_memory=dict(type='int',),
        minimum_required_config_memory=dict(type='int',),
        n_log_streaming_threads=dict(type='int',),
        name=dict(type='str', required=True),
        nat_flow_tcp_closed_timeout=dict(type='int',),
        nat_flow_tcp_established_timeout=dict(type='int',),
        nat_flow_tcp_half_closed_timeout=dict(type='int',),
        nat_flow_tcp_handshake_timeout=dict(type='int',),
        nat_flow_udp_noresponse_timeout=dict(type='int',),
        nat_flow_udp_response_timeout=dict(type='int',),
        netlink_poller_threads=dict(type='int',),
        netlink_sock_buf_size=dict(type='int',),
        ngx_free_connection_stack=dict(type='bool',),
        non_significant_log_throttle=dict(type='int',),
        ns_helper_deq_interval_msec=dict(type='int',),
        num_dispatcher_cores=dict(type='int',),
        num_dispatcher_queues=dict(type='int',),
        num_flow_cores_sum_changes_to_ignore=dict(type='int',),
        objsync_config=dict(type='dict',),
        objsync_port=dict(type='int',),
        openstack_availability_zone=dict(type='str',),
        openstack_availability_zones=dict(type='list',),
        openstack_mgmt_network_name=dict(type='str',),
        openstack_mgmt_network_uuid=dict(type='str',),
        os_reserved_memory=dict(type='int',),
        pcap_tx_mode=dict(type='str',),
        pcap_tx_ring_rd_balancing_factor=dict(type='int',),
        per_app=dict(type='bool',),
        per_vs_admission_control=dict(type='bool',),
        placement_mode=dict(type='str',),
        realtime_se_metrics=dict(type='dict',),
        reboot_on_panic=dict(type='bool',),
        reboot_on_stop=dict(type='bool',),
        resync_time_interval=dict(type='int',),
        sdb_flush_interval=dict(type='int',),
        sdb_pipeline_size=dict(type='int',),
        sdb_scan_count=dict(type='int',),
        se_bandwidth_type=dict(type='str',),
        se_delayed_flow_delete=dict(type='bool',),
        se_deprovision_delay=dict(type='int',),
        se_dos_profile=dict(type='dict',),
        se_dp_hm_drops=dict(type='int',),
        se_dp_if_state_poll_interval=dict(type='int',),
        se_dp_isolation=dict(type='bool',),
        se_dp_isolation_num_non_dp_cpus=dict(type='int',),
        se_dp_log_nf_enqueue_percent=dict(type='int',),
        se_dp_log_udf_enqueue_percent=dict(type='int',),
        se_dp_max_hb_version=dict(type='int',),
        se_dp_vnic_queue_stall_event_sleep=dict(type='int',),
        se_dp_vnic_queue_stall_threshold=dict(type='int',),
        se_dp_vnic_queue_stall_timeout=dict(type='int',),
        se_dp_vnic_restart_on_queue_stall_count=dict(type='int',),
        se_dp_vnic_stall_se_restart_window=dict(type='int',),
        se_dpdk_pmd=dict(type='int',),
        se_dump_core_on_assert=dict(type='bool',),
        se_emulated_cores=dict(type='int',),
        se_flow_probe_retries=dict(type='int',),
        se_flow_probe_retry_timer=dict(type='int',),
        se_flow_probe_timer=dict(type='int',),
        se_group_analytics_policy=dict(type='dict',),
        se_hyperthreaded_mode=dict(type='str',),
        se_ip_encap_ipc=dict(type='int',),
        se_ipc_udp_port=dict(type='int',),
        se_kni_burst_factor=dict(type='int',),
        se_l3_encap_ipc=dict(type='int',),
        se_log_buffer_app_blocking_dequeue=dict(type='bool',),
        se_log_buffer_conn_blocking_dequeue=dict(type='bool',),
        se_log_buffer_events_blocking_dequeue=dict(type='bool',),
        se_lro=dict(type='bool',),
        se_mp_ring_retry_count=dict(type='int',),
        se_mtu=dict(type='int',),
        se_name_prefix=dict(type='str',),
        se_packet_buffer_max=dict(type='int',),
        se_pcap_lookahead=dict(type='bool',),
        se_pcap_pkt_count=dict(type='int',),
        se_pcap_pkt_sz=dict(type='int',),
        se_pcap_qdisc_bypass=dict(type='bool',),
        se_pcap_reinit_frequency=dict(type='int',),
        se_pcap_reinit_threshold=dict(type='int',),
        se_probe_port=dict(type='int',),
        se_remote_punt_udp_port=dict(type='int',),
        se_rl_prop=dict(type='dict',),
        se_routing=dict(type='bool',),
        se_rum_sampling_nav_interval=dict(type='int',),
        se_rum_sampling_nav_percent=dict(type='int',),
        se_rum_sampling_res_interval=dict(type='int',),
        se_rum_sampling_res_percent=dict(type='int',),
        se_sb_dedicated_core=dict(type='bool',),
        se_sb_threads=dict(type='int',),
        se_thread_multiplier=dict(type='int',),
        se_tracert_port_range=dict(type='dict',),
        se_tunnel_mode=dict(type='int',),
        se_tunnel_udp_port=dict(type='int',),
        se_tx_batch_size=dict(type='int',),
        se_txq_threshold=dict(type='int',),
        se_udp_encap_ipc=dict(type='int',),
        se_use_dpdk=dict(type='int',),
        se_vnic_tx_sw_queue_flush_frequency=dict(type='int',),
        se_vnic_tx_sw_queue_size=dict(type='int',),
        se_vs_hb_max_pkts_in_batch=dict(type='int',),
        se_vs_hb_max_vs_in_pkt=dict(type='int',),
        self_se_election=dict(type='bool',),
        send_se_ready_timeout=dict(type='int',),
        service_ip6_subnets=dict(type='list',),
        service_ip_subnets=dict(type='list',),
        shm_minimum_config_memory=dict(type='int',),
        significant_log_throttle=dict(type='int',),
        ssl_preprocess_sni_hostname=dict(type='bool',),
        ssl_sess_cache_per_vs=dict(type='int',),
        tenant_ref=dict(type='str',),
        transient_shared_memory_max=dict(type='int',),
        udf_log_throttle=dict(type='int',),
        upstream_connect_timeout=dict(type='int',),
        upstream_connpool_enable=dict(type='bool',),
        upstream_read_timeout=dict(type='int',),
        upstream_send_timeout=dict(type='int',),
        url=dict(type='str',),
        use_hyperthreaded_cores=dict(type='bool',),
        use_legacy_netlink=dict(type='bool',),
        use_objsync=dict(type='bool',),
        use_standard_alb=dict(type='bool',),
        user_agent_cache_config=dict(type='dict',),
        user_defined_metric_age=dict(type='int',),
        uuid=dict(type='str',),
        vcenter_clusters=dict(type='dict',),
        vcenter_datastore_mode=dict(type='str',),
        vcenter_datastores=dict(type='list',),
        vcenter_datastores_include=dict(type='bool',),
        vcenter_folder=dict(type='str',),
        vcenter_hosts=dict(type='dict',),
        vcenters=dict(type='list',),
        vcpus_per_se=dict(type='int',),
        vip_asg=dict(type='dict',),
        vnic_dhcp_ip_check_interval=dict(type='int',),
        vnic_dhcp_ip_max_retries=dict(type='int',),
        vnic_ip_delete_interval=dict(type='int',),
        vnic_probe_interval=dict(type='int',),
        vnic_rpc_retry_interval=dict(type='int',),
        vnicdb_cmd_history_size=dict(type='int',),
        vs_host_redundancy=dict(type='bool',),
        vs_scalein_timeout=dict(type='int',),
        vs_scalein_timeout_for_upgrade=dict(type='int',),
        vs_scaleout_timeout=dict(type='int',),
        vs_se_scaleout_additional_wait_time=dict(type='int',),
        vs_se_scaleout_ready_timeout=dict(type='int',),
        vs_switchover_timeout=dict(type='int',),
        vss_placement=dict(type='dict',),
        vss_placement_enabled=dict(type='bool',),
        waf_learning_interval=dict(type='int',),
        waf_learning_memory=dict(type='int',),
        waf_mempool=dict(type='bool',),
        waf_mempool_size=dict(type='int',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk>=17.1) or requests is not installed. '
            'For more details visit https://github.com/vmware/alb-sdk.'))
    return avi_ansible_api(module, 'serviceenginegroup',
                           set())


if __name__ == '__main__':
    main()
