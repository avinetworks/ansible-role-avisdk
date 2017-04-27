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
module: avi_debugvirtualservice
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: Module for setup of DebugVirtualService Avi RESTful Object
description:
    - This module is used to configure DebugVirtualService object
    - more examples at U(https://github.com/avinetworks/devops)
requirements: [ avisdk ]
version_added: "2.3"
options:
    state:
        description:
            - The state that should be applied on the entity.
        default: present
        choices: ["absent","present"]
    capture:
        description:
            - Boolean flag to set capture.
    capture_params:
        description:
            - Debugvirtualservicecapture settings for debugvirtualservice.
    cloud_ref:
        description:
            - It is a reference to an object of type cloud.
    debug_hm:
        description:
            - This option controls the capture of health monitor flows.
            - Enum options - DEBUG_VS_HM_NONE, DEBUG_VS_HM_ONLY, DEBUG_VS_HM_INCLUDE.
            - Default value when not specified in API or module is interpreted by Avi Controller as DEBUG_VS_HM_NONE.
    debug_ip:
        description:
            - Debugipaddr settings for debugvirtualservice.
    flags:
        description:
            - List of debugvsdataplane.
    name:
        description:
            - Name of the object.
        required: true
    se_params:
        description:
            - Debugvirtualserviceseparams settings for debugvirtualservice.
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
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
- name: Example to create DebugVirtualService object
  avi_debugvirtualservice:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_debugvirtualservice
"""

RETURN = '''
obj:
    description: DebugVirtualService (api/debugvirtualservice) object
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
        capture=dict(type='bool',),
        capture_params=dict(type='dict',),
        cloud_ref=dict(type='str',),
        debug_hm=dict(type='str',),
        debug_ip=dict(type='dict',),
        flags=dict(type='list',),
        name=dict(type='str', required=True),
        se_params=dict(type='dict',),
        tenant_ref=dict(type='str',),
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
    return avi_ansible_api(module, 'debugvirtualservice',
                           set([]))

if __name__ == '__main__':
    main()
