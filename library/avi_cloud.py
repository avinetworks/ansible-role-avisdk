#!/usr/bin/python
#
# @author: Gaurav Rastogi (grastogi@avinetworks.com)
#          Eric Anderson (eanderson@avinetworks.com)
# module_check: supported
# Avi Version: 17.1.1
#
# Copyright: (c) 2017 Gaurav Rastogi, <grastogi@avinetworks.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_cloud
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>

short_description: Module for setup of Cloud Avi RESTful Object
description:
    - This module is used to configure Cloud object
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
        choices: ["add", "replace", "delete"]
        type: str
    apic_configuration:
        description:
            - Apicconfiguration settings for cloud.
        type: dict
    apic_mode:
        description:
            - Boolean flag to set apic_mode.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    autoscale_polling_interval:
        description:
            - Cloudconnector polling interval in seconds for external autoscale groups, minimum 60 seconds.
            - Allowed values are 60-3600.
            - Field introduced in 18.2.2.
            - Default value when not specified in API or module is interpreted by Avi Controller as 60.
        version_added: "2.9"
        type: int
    aws_configuration:
        description:
            - Awsconfiguration settings for cloud.
        type: dict
    azure_configuration:
        description:
            - Field introduced in 17.2.1.
        version_added: "2.5"
        type: dict
    cloudstack_configuration:
        description:
            - Cloudstackconfiguration settings for cloud.
        type: dict
    custom_tags:
        description:
            - Custom tags for all avi created resources in the cloud infrastructure.
            - Field introduced in 17.1.5.
        version_added: "2.5"
        type: list
    dhcp_enabled:
        description:
            - Select the ip address management scheme.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    dns_provider_ref:
        description:
            - Dns profile for the cloud.
            - It is a reference to an object of type ipamdnsproviderprofile.
        type: str
    dns_resolution_on_se:
        description:
            - By default, pool member fqdns are resolved on the controller.
            - When this is set, pool member fqdns are instead resolved on service engines in this cloud.
            - This is useful in scenarios where pool member fqdns can only be resolved from service engines and not from the controller.
            - Field introduced in 18.2.6.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    docker_configuration:
        description:
            - Dockerconfiguration settings for cloud.
        type: dict
    east_west_dns_provider_ref:
        description:
            - Dns profile for east-west services.
            - It is a reference to an object of type ipamdnsproviderprofile.
        type: str
    east_west_ipam_provider_ref:
        description:
            - Ipam profile for east-west services.
            - Warning - please use virtual subnets in this ipam profile that do not conflict with the underlay networks or any overlay networks in the cluster.
            - For example in aws and gcp, 169.254.0.0/16 is used for storing instance metadata.
            - Hence, it should not be used in this profile.
            - It is a reference to an object of type ipamdnsproviderprofile.
        type: str
    enable_vip_static_routes:
        description:
            - Use static routes for vip side network resolution during virtualservice placement.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    gcp_configuration:
        description:
            - Google cloud platform configuration.
            - Field introduced in 18.2.1.
        version_added: "2.9"
        type: dict
    ip6_autocfg_enabled:
        description:
            - Enable ipv6 auto configuration.
            - Field introduced in 18.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        version_added: "2.9"
        type: bool
    ipam_provider_ref:
        description:
            - Ipam profile for the cloud.
            - It is a reference to an object of type ipamdnsproviderprofile.
        type: str
    license_tier:
        description:
            - Specifies the default license tier which would be used by new se groups.
            - This field by default inherits the value from system configuration.
            - Enum options - ENTERPRISE_16, ENTERPRISE_18.
            - Field introduced in 17.2.5.
        version_added: "2.5"
        type: str
    license_type:
        description:
            - If no license type is specified then default license enforcement for the cloud type is chosen.
            - The default mappings are container cloud is max ses, openstack and vmware is cores and linux it is sockets.
            - Enum options - LIC_BACKEND_SERVERS, LIC_SOCKETS, LIC_CORES, LIC_HOSTS, LIC_SE_BANDWIDTH, LIC_METERED_SE_BANDWIDTH.
        type: str
    linuxserver_configuration:
        description:
            - Linuxserverconfiguration settings for cloud.
        type: dict
    mesos_configuration:
        description:
            - Field deprecated in 18.2.2.
        type: dict
    mtu:
        description:
            - Mtu setting for the cloud.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1500.
        type: int
    name:
        description:
            - Name of the object.
        required: true
        type: str
    nsx_configuration:
        description:
            - Configuration parameters for nsx manager.
            - Field introduced in 17.1.1.
        type: dict
    obj_name_prefix:
        description:
            - Default prefix for all automatically created objects in this cloud.
            - This prefix can be overridden by the se-group template.
        type: str
    openstack_configuration:
        description:
            - Openstackconfiguration settings for cloud.
        type: dict
    oshiftk8s_configuration:
        description:
            - Oshiftk8sconfiguration settings for cloud.
        type: dict
    prefer_static_routes:
        description:
            - Prefer static routes over interface routes during virtualservice placement.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    proxy_configuration:
        description:
            - Proxyconfiguration settings for cloud.
        type: dict
    rancher_configuration:
        description:
            - Rancherconfiguration settings for cloud.
        type: dict
    se_group_template_ref:
        description:
            - The service engine group to use as template.
            - It is a reference to an object of type serviceenginegroup.
            - Field introduced in 18.2.5.
        version_added: "2.9"
        type: str
    state_based_dns_registration:
        description:
            - Dns records for vips are added/deleted based on the operational state of the vips.
            - Field introduced in 17.1.12.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        version_added: "2.5"
        type: bool
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Unique object identifier of the object.
        type: str
    vca_configuration:
        description:
            - Vcloudairconfiguration settings for cloud.
        type: dict
    vcenter_configuration:
        description:
            - Vcenterconfiguration settings for cloud.
        type: dict
    vtype:
        description:
            - Cloud type.
            - Enum options - CLOUD_NONE, CLOUD_VCENTER, CLOUD_OPENSTACK, CLOUD_AWS, CLOUD_VCA, CLOUD_APIC, CLOUD_MESOS, CLOUD_LINUXSERVER, CLOUD_DOCKER_UCP,
            - CLOUD_RANCHER, CLOUD_OSHIFT_K8S, CLOUD_AZURE, CLOUD_GCP.
            - Default value when not specified in API or module is interpreted by Avi Controller as CLOUD_NONE.
        required: true
        type: str


extends_documentation_fragment:
    - avi
'''

EXAMPLES = """
  - name: Create a VMWare cloud with write access mode
    avi_cloud:
      username: '{{ username }}'
      controller: '{{ controller }}'
      password: '{{ password }}'
      apic_mode: false
      dhcp_enabled: true
      enable_vip_static_routes: false
      license_type: LIC_CORES
      mtu: 1500
      name: VCenter Cloud
      prefer_static_routes: false
      tenant_ref: admin
      vcenter_configuration:
        datacenter_ref: /api/vimgrdcruntime/datacenter-2-10.10.20.100
        management_network: /api/vimgrnwruntime/dvportgroup-103-10.10.20.100
        password: password
        privilege: WRITE_ACCESS
        username: user
        vcenter_url: 10.10.20.100
      vtype: CLOUD_VCENTER
"""

RETURN = '''
obj:
    description: Cloud (api/cloud) object
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
        avi_api_patch_op=dict(choices=['add', 'replace', 'delete']),
        apic_configuration=dict(type='dict',),
        apic_mode=dict(type='bool',),
        autoscale_polling_interval=dict(type='int',),
        aws_configuration=dict(type='dict',),
        azure_configuration=dict(type='dict',),
        cloudstack_configuration=dict(type='dict',),
        custom_tags=dict(type='list',),
        dhcp_enabled=dict(type='bool',),
        dns_provider_ref=dict(type='str',),
        dns_resolution_on_se=dict(type='bool',),
        docker_configuration=dict(type='dict',),
        east_west_dns_provider_ref=dict(type='str',),
        east_west_ipam_provider_ref=dict(type='str',),
        enable_vip_static_routes=dict(type='bool',),
        gcp_configuration=dict(type='dict',),
        ip6_autocfg_enabled=dict(type='bool',),
        ipam_provider_ref=dict(type='str',),
        license_tier=dict(type='str',),
        license_type=dict(type='str',),
        linuxserver_configuration=dict(type='dict',),
        mesos_configuration=dict(type='dict',),
        mtu=dict(type='int',),
        name=dict(type='str', required=True),
        nsx_configuration=dict(type='dict',),
        obj_name_prefix=dict(type='str',),
        openstack_configuration=dict(type='dict',),
        oshiftk8s_configuration=dict(type='dict',),
        prefer_static_routes=dict(type='bool',),
        proxy_configuration=dict(type='dict',),
        rancher_configuration=dict(type='dict',),
        se_group_template_ref=dict(type='str',),
        state_based_dns_registration=dict(type='bool',),
        tenant_ref=dict(type='str',),
        url=dict(type='str',),
        uuid=dict(type='str',),
        vca_configuration=dict(type='dict',),
        vcenter_configuration=dict(type='dict',),
        vtype=dict(type='str', required=True),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk>=17.1) or requests is not installed. '
            'For more details visit https://github.com/avinetworks/sdk.'))
    return avi_ansible_api(module, 'cloud',
                           set([]))


if __name__ == '__main__':
    main()
