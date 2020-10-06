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
module: avi_controllerlicense
author: Gaurav Rastogi (grastogi@avinetworks.com)

deprecated:
  removed_in: '2.11'
  why: Removed support of this module.
  alternative: Use M(avi_api_session) instead.

short_description: Module for setup of ControllerLicense Avi RESTful Object
description:
    - This module is used to configure ControllerLicense object
    - more examples at U(https://github.com/avinetworks/devops)
requirements: [ avisdk ]
version_added: "2.3"
options:
    state:
        description:
            - The state that should be applied on the entity.
        default: present
        choices: ["absent","present"]
    backend_servers:
        description:
            - Number of backend_servers.
    cores:
        description:
            - Number of service engine cores in non-container clouds.
    customer_name:
        description:
            - Customer_name of controllerlicense.
        required: true
    license_tier:
        description:
            - License_tier of controllerlicense.
    licenses:
        description:
            - List of singlelicense.
    max_apps:
        description:
            - Number of max_apps.
    max_ses:
        description:
            - Number of service engines hosts in container clouds.
    max_vses:
        description:
            - Deprecated.
    name:
        description:
            - Name of the object.
    sockets:
        description:
            - Number of physical cpu sockets across service engines in no access and linux server clouds.
    start_on:
        description:
            - Start_on of controllerlicense.
    throughput:
        description:
            - Number of throughput.
    url:
        description:
            - Avi controller URL of the object.
    uuid:
        description:
            - Unique object identifier of the object.
    valid_until:
        description:
            - Valid_until of controllerlicense.
        required: true
extends_documentation_fragment:
    - avi
'''

EXAMPLES = """
- name: Example to create ControllerLicense object
  avi_controllerlicense:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_controllerlicense
"""

RETURN = '''
obj:
    description: ControllerLicense (api/controllerlicense) object
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
        backend_servers=dict(type='int',),
        cores=dict(type='int',),
        customer_name=dict(type='str', required=True),
        license_tier=dict(type='list',),
        licenses=dict(type='list',),
        max_apps=dict(type='int',),
        max_ses=dict(type='int',),
        max_vses=dict(type='int',),
        name=dict(type='str',),
        sockets=dict(type='int',),
        start_on=dict(type='str',),
        throughput=dict(type='int',),
        url=dict(type='str',),
        uuid=dict(type='str',),
        valid_until=dict(type='str', required=True),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk>=17.1) is not installed. '
            'For more details visit https://github.com/avinetworks/sdk.'))
    return avi_ansible_api(module, 'controllerlicense',
                           set([]))

if __name__ == '__main__':
    main()
