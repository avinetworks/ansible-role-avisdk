#!/usr/bin/python
#
# Created on Aug 25, 2016
# @author: Gaurav Rastogi (grastogi@avinetworks.com)
#          Eric Anderson (eanderson@avinetworks.com)
# module_check: supported
# Avi Version: 17.1.1
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
module: avi_vimgrvcenterruntime
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: Module for setup of VIMgrVcenterRuntime Avi RESTful Object
description:
    - This module is used to configure VIMgrVcenterRuntime object
    - more examples at U(https://github.com/avinetworks/devops)
requirements: [ avisdk ]
version_added: "2.3"
options:
    state:
        description:
            - The state that should be applied on the entity.
        default: present
        choices: ["absent","present"]
    api_version:
        description:
            - Api_version of vimgrvcenterruntime.
    apic_mode:
        description:
            - Boolean flag to set apic_mode.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
    cloud_ref:
        description:
            - It is a reference to an object of type cloud.
    datacenter_refs:
        description:
            - It is a reference to an object of type vimgrdcruntime.
    disc_end_time:
        description:
            - Disc_end_time of vimgrvcenterruntime.
    disc_start_time:
        description:
            - Disc_start_time of vimgrvcenterruntime.
    discovered_datacenter:
        description:
            - Discovered_datacenter of vimgrvcenterruntime.
    inventory_progress:
        description:
            - Inventory_progress of vimgrvcenterruntime.
    inventory_state:
        description:
            - Enum options - vcenter_discovery_bad_credentials, vcenter_discovery_retrieving_dc, vcenter_discovery_waiting_dc, vcenter_discovery_retrieving_nw,
            - vcenter_discovery_ongoing, vcenter_discovery_resyncing, vcenter_discovery_complete, vcenter_discovery_deleting_vcenter, vcenter_discovery_failure,
            - vcenter_discovery_complete_no_mgmt_nw, vcenter_discovery_complete_per_tenant_ip_route, vcenter_discovery_making_se_ova.
    management_network:
        description:
            - Management_network of vimgrvcenterruntime.
    name:
        description:
            - Name of the object.
        required: true
    num_clusters:
        description:
            - Number of num_clusters.
    num_dcs:
        description:
            - Number of num_dcs.
    num_hosts:
        description:
            - Number of num_hosts.
    num_nws:
        description:
            - Number of num_nws.
    num_vcenter_req_pending:
        description:
            - Number of num_vcenter_req_pending.
    num_vms:
        description:
            - Number of num_vms.
    privilege:
        description:
            - Enum options - no_access, read_access, write_access.
    progress:
        description:
            - Number of progress.
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
    vcenter_connected:
        description:
            - Boolean flag to set vcenter_connected.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
    vcenter_fullname:
        description:
            - Vcenter_fullname of vimgrvcenterruntime.
    vcenter_template_se_location:
        description:
            - Vcenter_template_se_location of vimgrvcenterruntime.
    vcenter_url:
        description:
            - Vcenter_url of vimgrvcenterruntime.
        required: true
extends_documentation_fragment:
    - avi
'''

EXAMPLES = """
- name: Example to create VIMgrVcenterRuntime object
  avi_vimgrvcenterruntime:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_vimgrvcenterruntime
"""

RETURN = '''
obj:
    description: VIMgrVcenterRuntime (api/vimgrvcenterruntime) object
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
        api_version=dict(type='str',),
        apic_mode=dict(type='bool',),
        cloud_ref=dict(type='str',),
        datacenter_refs=dict(type='list',),
        disc_end_time=dict(type='str',),
        disc_start_time=dict(type='str',),
        discovered_datacenter=dict(type='str',),
        inventory_progress=dict(type='str',),
        inventory_state=dict(type='str',),
        management_network=dict(type='str',),
        name=dict(type='str', required=True),
        num_clusters=dict(type='int',),
        num_dcs=dict(type='int',),
        num_hosts=dict(type='int',),
        num_nws=dict(type='int',),
        num_vcenter_req_pending=dict(type='int',),
        num_vms=dict(type='int',),
        privilege=dict(type='str',),
        progress=dict(type='int',),
        tenant_ref=dict(type='str',),
        type=dict(type='str', required=True),
        url=dict(type='str',),
        uuid=dict(type='str',),
        vcenter_connected=dict(type='bool',),
        vcenter_fullname=dict(type='str',),
        vcenter_template_se_location=dict(type='str',),
        vcenter_url=dict(type='str', required=True),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk>=17.1) is not installed. '
            'For more details visit https://github.com/avinetworks/sdk.'))
    return avi_ansible_api(module, 'vimgrvcenterruntime',
                           set([]))

if __name__ == '__main__':
    main()
