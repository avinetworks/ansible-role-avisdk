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
                    'status': ['deprecated'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_securechannelmapping
author: Gaurav Rastogi (grastogi@avinetworks.com)

deprecated:
    removed_in: '2.11'
    why: Removed support for the module.
    alternative: Use M(avi_api_session) instead.

short_description: Module for setup of SecureChannelMapping Avi RESTful Object
description:
    - This module is used to configure SecureChannelMapping object
    - more examples at U(https://github.com/avinetworks/devops)
requirements: [ avisdk ]
version_added: "2.3"
options:
    state:
        description:
            - The state that should be applied on the entity.
        default: present
        choices: ["absent","present"]
    ip:
        description:
            - Ip of securechannelmapping.
    is_controller:
        description:
            - Boolean flag to set is_controller.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
    local_ip:
        description:
            - Local_ip of securechannelmapping.
    marked_for_delete:
        description:
            - Boolean flag to set marked_for_delete.
    name:
        description:
            - Name of the object.
        required: true
    pub_key:
        description:
            - Pub_key of securechannelmapping.
    pub_key_pem:
        description:
            - Pub_key_pem of securechannelmapping.
    status:
        description:
            - Enum options - secure_channel_none, secure_channel_connected, secure_channel_auth_ssh_success, secure_channel_auth_ssh_failed,
            - secure_channel_auth_token_success, secure_channel_auth_token_failed, secure_channel_auth_errors, secure_channel_auth_ignored.
            - Default value when not specified in API or module is interpreted by Avi Controller as SECURE_CHANNEL_NONE.
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
- name: Example to create SecureChannelMapping object
  avi_securechannelmapping:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_securechannelmapping
"""

RETURN = '''
obj:
    description: SecureChannelMapping (api/securechannelmapping) object
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
        ip=dict(type='str',),
        is_controller=dict(type='bool',),
        local_ip=dict(type='str',),
        marked_for_delete=dict(type='bool',),
        name=dict(type='str', required=True),
        pub_key=dict(type='str',),
        pub_key_pem=dict(type='str',),
        status=dict(type='str',),
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
    return avi_ansible_api(module, 'securechannelmapping',
                           set([]))

if __name__ == '__main__':
    main()
