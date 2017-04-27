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
module: avi_vimgrhostruntime
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: Module for setup of VIMgrHostRuntime Avi RESTful Object
description:
    - This module is used to configure VIMgrHostRuntime object
    - more examples at U(https://github.com/avinetworks/devops)
requirements: [ avisdk ]
version_added: "2.3"
options:
    state:
        description:
            - The state that should be applied on the entity.
        default: present
        choices: ["absent","present"]
    cloud_ref:
        description:
            - It is a reference to an object of type cloud.
    cluster_name:
        description:
            - Cluster_name of vimgrhostruntime.
    cluster_uuid:
        description:
            - Unique object identifier of cluster.
    cntlr_accessible:
        description:
            - Boolean flag to set cntlr_accessible.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
    connection_state:
        description:
            - Connection_state of vimgrhostruntime.
            - Default value when not specified in API or module is interpreted by Avi Controller as connected.
    cpu_hz:
        description:
            - Number of cpu_hz.
    maintenance_mode:
        description:
            - Boolean flag to set maintenance_mode.
    managed_object_id:
        description:
            - Managed_object_id of vimgrhostruntime.
        required: true
    mem:
        description:
            - Number of mem.
    mgmt_portgroup:
        description:
            - Mgmt_portgroup of vimgrhostruntime.
            - Default value when not specified in API or module is interpreted by Avi Controller as .
    name:
        description:
            - Name of the object.
        required: true
    network_uuids:
        description:
            - Unique object identifiers of networks.
    num_cpu_cores:
        description:
            - Number of num_cpu_cores.
    num_cpu_packages:
        description:
            - Number of num_cpu_packages.
    num_cpu_threads:
        description:
            - Number of num_cpu_threads.
    pnics:
        description:
            - List of cdplldpinfo.
    powerstate:
        description:
            - Powerstate of vimgrhostruntime.
    quarantine_start_ts:
        description:
            - Quarantine_start_ts of vimgrhostruntime.
    quarantined:
        description:
            - Boolean flag to set quarantined.
    quarantined_periods:
        description:
            - Number of quarantined_periods.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
    se_fail_cnt:
        description:
            - Number of se_fail_cnt.
    se_success_cnt:
        description:
            - Number of se_success_cnt.
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
    vm_refs:
        description:
            - It is a reference to an object of type vimgrvmruntime.
extends_documentation_fragment:
    - avi
'''

EXAMPLES = """
- name: Example to create VIMgrHostRuntime object
  avi_vimgrhostruntime:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_vimgrhostruntime
"""

RETURN = '''
obj:
    description: VIMgrHostRuntime (api/vimgrhostruntime) object
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
        cloud_ref=dict(type='str',),
        cluster_name=dict(type='str',),
        cluster_uuid=dict(type='str',),
        cntlr_accessible=dict(type='bool',),
        connection_state=dict(type='str',),
        cpu_hz=dict(type='int',),
        maintenance_mode=dict(type='bool',),
        managed_object_id=dict(type='str', required=True),
        mem=dict(type='int',),
        mgmt_portgroup=dict(type='str',),
        name=dict(type='str', required=True),
        network_uuids=dict(type='list',),
        num_cpu_cores=dict(type='int',),
        num_cpu_packages=dict(type='int',),
        num_cpu_threads=dict(type='int',),
        pnics=dict(type='list',),
        powerstate=dict(type='str',),
        quarantine_start_ts=dict(type='str',),
        quarantined=dict(type='bool',),
        quarantined_periods=dict(type='int',),
        se_fail_cnt=dict(type='int',),
        se_success_cnt=dict(type='int',),
        tenant_ref=dict(type='str',),
        type=dict(type='str', required=True),
        url=dict(type='str',),
        uuid=dict(type='str',),
        vm_refs=dict(type='list',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk>=17.1) is not installed. '
            'For more details visit https://github.com/avinetworks/sdk.'))
    return avi_ansible_api(module, 'vimgrhostruntime',
                           set([]))

if __name__ == '__main__':
    main()
