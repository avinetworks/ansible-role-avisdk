#!/usr/bin/python
#
# @author: Gaurav Rastogi (grastogi@avinetworks.com)
#          Eric Anderson (eanderson@avinetworks.com)
# module_check: supported
#
# Copyright: (c) 2017 Gaurav Rastogi, <grastogi@avinetworks.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['deprecated'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_customerportalinfo
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>

deprecated:
    removed_in: '2.11'
    why: Removed support for the module.
    alternative: Use M(avi_api_session) instead.

short_description: Module for setup of CustomerPortalInfo Avi RESTful Object
description:
    - This module is used to configure CustomerPortalInfo object
    - more examples at U(https://github.com/avinetworks/devops)
requirements: [ avisdk ]
version_added: "2.7"
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
    polling_interval:
        description:
            - Time interval in minutes.
            - Allowed values are 5-60.
            - Field introduced in 18.2.6.
            - Default value when not specified in API or module is interpreted by Avi Controller as 10.
        type: int
    portal_url:
        description:
            - The fqdn or ip address of the customer portal.
            - Field introduced in 18.2.6.
        required: true
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Field introduced in 18.2.6.
        type: str


extends_documentation_fragment:
    - avi
'''

EXAMPLES = """
- name: Example to create CustomerPortalInfo object
  avi_customerportalinfo:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_customerportalinfo
"""

RETURN = '''
obj:
    description: CustomerPortalInfo (api/customerportalinfo) object
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
        polling_interval=dict(type='int',),
        portal_url=dict(type='str', required=True),
        url=dict(type='str',),
        uuid=dict(type='str',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk>=17.1) or requests is not installed. '
            'For more details visit https://github.com/avinetworks/sdk.'))
    return avi_ansible_api(module, 'customerportalinfo',
                           set([]))


if __name__ == '__main__':
    main()
