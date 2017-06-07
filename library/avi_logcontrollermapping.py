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
module: avi_logcontrollermapping
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: Module for setup of LogControllerMapping Avi RESTful Object
description:
    - This module is used to configure LogControllerMapping object
    - more examples at U(https://github.com/avinetworks/devops)
requirements: [ avisdk ]
version_added: "2.4"
options:
    state:
        description:
            - The state that should be applied on the entity.
        default: present
        choices: ["absent","present"]
    controller_ip:
        description:
            - Controller_ip of logcontrollermapping.
    metrics_mgr_port:
        description:
            - Enum options - metrics_mgr_port_0, metrics_mgr_port_1, metrics_mgr_port_2, metrics_mgr_port_3.
            - Default value when not specified in API or module is interpreted by Avi Controller as METRICS_MGR_PORT_0.
    node_uuid:
        description:
            - Unique object identifier of node.
    prev_controller_ip:
        description:
            - Prev_controller_ip of logcontrollermapping.
    prev_metrics_mgr_port:
        description:
            - Enum options - metrics_mgr_port_0, metrics_mgr_port_1, metrics_mgr_port_2, metrics_mgr_port_3.
            - Default value when not specified in API or module is interpreted by Avi Controller as METRICS_MGR_PORT_0.
    static_mapping:
        description:
            - Boolean flag to set static_mapping.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
    url:
        description:
            - Avi controller URL of the object.
    uuid:
        description:
            - Unique object identifier of the object.
    vs_uuid:
        description:
            - Unique object identifier of vs.
        required: true
extends_documentation_fragment:
    - avi
'''

EXAMPLES = """
- name: Example to create LogControllerMapping object
  avi_logcontrollermapping:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_logcontrollermapping
"""

RETURN = '''
obj:
    description: LogControllerMapping (api/logcontrollermapping) object
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
        controller_ip=dict(type='str',),
        metrics_mgr_port=dict(type='str',),
        node_uuid=dict(type='str',),
        prev_controller_ip=dict(type='str',),
        prev_metrics_mgr_port=dict(type='str',),
        static_mapping=dict(type='bool',),
        tenant_ref=dict(type='str',),
        url=dict(type='str',),
        uuid=dict(type='str',),
        vs_uuid=dict(type='str', required=True),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk>=17.1) is not installed. '
            'For more details visit https://github.com/avinetworks/sdk.'))
    return avi_ansible_api(module, 'logcontrollermapping',
                           set([]))

if __name__ == '__main__':
    main()
