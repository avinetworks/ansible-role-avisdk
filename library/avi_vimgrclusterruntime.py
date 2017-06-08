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
module: avi_vimgrclusterruntime
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: Module for setup of VIMgrClusterRuntime Avi RESTful Object
description:
    - This module is used to configure VIMgrClusterRuntime object
    - more examples at U(https://github.com/avinetworks/devops)
requirements: [ avisdk ]
version_added: "2.4"
options:
    state:
        description:
            - The state that should be applied on the entity.
        default: present
        choices: ["absent","present"]
    cloud_ref:
        description:
            - It is a reference to an object of type cloud.
    datacenter_managed_object_id:
        description:
            - Datacenter_managed_object_id of vimgrclusterruntime.
    datacenter_uuid:
        description:
            - Unique object identifier of datacenter.
    host_refs:
        description:
            - It is a reference to an object of type vimgrhostruntime.
    managed_object_id:
        description:
            - Managed_object_id of vimgrclusterruntime.
        required: true
    name:
        description:
            - Name of the object.
        required: true
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
extends_documentation_fragment:
    - avi
'''

EXAMPLES = """
- name: Example to create VIMgrClusterRuntime object
  avi_vimgrclusterruntime:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_vimgrclusterruntime
"""

RETURN = '''
obj:
    description: VIMgrClusterRuntime (api/vimgrclusterruntime) object
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
        datacenter_managed_object_id=dict(type='str',),
        datacenter_uuid=dict(type='str',),
        host_refs=dict(type='list',),
        managed_object_id=dict(type='str', required=True),
        name=dict(type='str', required=True),
        tenant_ref=dict(type='str',),
        type=dict(type='str', required=True),
        url=dict(type='str',),
        uuid=dict(type='str',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk>=17.1) is not installed. '
            'For more details visit https://github.com/avinetworks/sdk.'))
    return avi_ansible_api(module, 'vimgrclusterruntime',
                           set([]))

if __name__ == '__main__':
    main()
