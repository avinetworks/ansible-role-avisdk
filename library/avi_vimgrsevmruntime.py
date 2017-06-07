#!/usr/bin/python
#
# Created on Aug 25, 2016
# @author: Gaurav Rastogi (grastogi@avinetworks.com)
#          Eric Anderson (eanderson@avinetworks.com)
# module_check: supported
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

ANSIBLE_METADATA = {'metadata_version': '1.0',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_vimgrsevmruntime
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: Module for setup of VIMgrSEVMRuntime Avi RESTful Object
description:
    - This module is used to configure VIMgrSEVMRuntime object
    - more examples at U(https://github.com/avinetworks/devops)
requirements: [ avisdk ]
version_added: "2.4"
options:
    state:
        description:
            - The state that should be applied on the entity.
        default: present
        choices: ["absent","present"]
    availability_zone:
        description:
            - Availability_zone of vimgrsevmruntime.
    cloud_name:
        description:
            - Cloud_name of vimgrsevmruntime.
    cloud_ref:
        description:
            - It is a reference to an object of type cloud.
    connection_state:
        description:
            - Connection_state of vimgrsevmruntime.
    controller_cluster_uuid:
        description:
            - Unique object identifier of controller_cluster.
    controller_ip_addr:
        description:
            - Controller_ip_addr of vimgrsevmruntime.
    creation_in_progress:
        description:
            - Boolean flag to set creation_in_progress.
    deletion_in_progress:
        description:
            - Boolean flag to set deletion_in_progress.
    discovery_response:
        description:
            - Discovery_response of vimgrsevmruntime.
    discovery_status:
        description:
            - Number of discovery_status.
    flavor:
        description:
            - Flavor of vimgrsevmruntime.
    guest_nic:
        description:
            - List of vimgrguestnicruntime.
    host:
        description:
            - Host of vimgrsevmruntime.
    host_ref:
        description:
            - It is a reference to an object of type vimgrhostruntime.
    hostid:
        description:
            - Hostid of vimgrsevmruntime.
    hypervisor:
        description:
            - Enum options - default, vmware_esx, kvm, vmware_vsan, xen.
    init_vnics:
        description:
            - Number of init_vnics.
    last_discovery:
        description:
            - Number of last_discovery.
    managed_object_id:
        description:
            - Managed_object_id of vimgrsevmruntime.
        required: true
    name:
        description:
            - Name of the object.
        required: true
    powerstate:
        description:
            - Powerstate of vimgrsevmruntime.
    security_group_uuid:
        description:
            - Unique object identifier of security_group.
    segroup_ref:
        description:
            - It is a reference to an object of type serviceenginegroup.
    server_group_uuid:
        description:
            - Unique object identifier of server_group.
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
    type:
        description:
            - Enum options - cloud_none, cloud_vcenter, cloud_openstack, cloud_aws, cloud_vca, cloud_apic, cloud_mesos, cloud_linuxserver, cloud_docker_ucp,
            - cloud_rancher, cloud_oshift_k8s.
        required: true
    url:
        description:
            - Avi controller URL of the object.
    uuid:
        description:
            - Unique object identifier of the object.
    vcenter_datacenter_uuid:
        description:
            - Unique object identifier of vcenter_datacenter.
    vcenter_rm_cookie:
        description:
            - Vcenter_rm_cookie of vimgrsevmruntime.
    vcenter_se_type:
        description:
            - Enum options - vimgr_se_network_admin, vimgr_se_unified_admin.
    vcenter_template_vm:
        description:
            - Boolean flag to set vcenter_template_vm.
    vcenter_vAppName:
        description:
            - Vcenter_vappname of vimgrsevmruntime.
    vcenter_vAppVendor:
        description:
            - Vcenter_vappvendor of vimgrsevmruntime.
    vcenter_vm_type:
        description:
            - Enum options - vmtype_se_vm, vmtype_pool_srvr.
extends_documentation_fragment:
    - avi
'''

EXAMPLES = """
- name: Example to create VIMgrSEVMRuntime object
  avi_vimgrsevmruntime:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_vimgrsevmruntime
"""

RETURN = '''
obj:
    description: VIMgrSEVMRuntime (api/vimgrsevmruntime) object
    returned: success, changed
    type: dict
'''

from ansible.module_utils.basic import AnsibleModule
try:
    from avi.sdk.utils.ansible_utils import avi_common_argument_spec
    from pkg_resources import parse_version
    import avi.sdk
    sdk_version = getattr(avi.sdk, '__version__', None)
    if ((sdk_version is None) or (sdk_version and
            (parse_version(sdk_version) < parse_version('17.1')))):
        # It allows the __version__ to be '' as that value is used in development builds
        raise ImportError
    from avi.sdk.utils.ansible_utils import avi_ansible_api
    HAS_AVI = True
except ImportError:
    HAS_AVI = False


def main():
    argument_specs = dict(
        state=dict(default='present',
                   choices=['absent', 'present']),
        availability_zone=dict(type='str',),
        cloud_name=dict(type='str',),
        cloud_ref=dict(type='str',),
        connection_state=dict(type='str',),
        controller_cluster_uuid=dict(type='str',),
        controller_ip_addr=dict(type='str',),
        creation_in_progress=dict(type='bool',),
        deletion_in_progress=dict(type='bool',),
        discovery_response=dict(type='str',),
        discovery_status=dict(type='int',),
        flavor=dict(type='str',),
        guest_nic=dict(type='list',),
        host=dict(type='str',),
        host_ref=dict(type='str',),
        hostid=dict(type='str',),
        hypervisor=dict(type='str',),
        init_vnics=dict(type='int',),
        last_discovery=dict(type='int',),
        managed_object_id=dict(type='str', required=True),
        name=dict(type='str', required=True),
        powerstate=dict(type='str',),
        security_group_uuid=dict(type='str',),
        segroup_ref=dict(type='str',),
        server_group_uuid=dict(type='str',),
        tenant_ref=dict(type='str',),
        type=dict(type='str', required=True),
        url=dict(type='str',),
        uuid=dict(type='str',),
        vcenter_datacenter_uuid=dict(type='str',),
        vcenter_rm_cookie=dict(type='str',),
        vcenter_se_type=dict(type='str',),
        vcenter_template_vm=dict(type='bool',),
        vcenter_vAppName=dict(type='str',),
        vcenter_vAppVendor=dict(type='str',),
        vcenter_vm_type=dict(type='str',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk>=17.1) is not installed. '
            'For more details visit https://github.com/avinetworks/sdk.'))
    return avi_ansible_api(module, 'vimgrsevmruntime',
                           set([]))

if __name__ == '__main__':
    main()
