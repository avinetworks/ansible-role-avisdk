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
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_image
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>

short_description: Module for setup of Image Avi RESTful Object
description:
    - This module is used to configure Image object
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
    controller_info:
        description:
            - Controller package details.
            - Field introduced in 18.2.6.
        type: dict
    migrations:
        description:
            - This field describes the api migration related information.
            - Field introduced in 18.2.6.
        type: dict
    name:
        description:
            - Name of the image.
            - Field introduced in 18.2.6.
        required: true
        type: str
    se_info:
        description:
            - Se package details.
            - Field introduced in 18.2.6.
        type: dict
    status:
        description:
            - Status to check if the image is present.
            - Enum options - SYSERR_SUCCESS,  SYSERR_FAILURE,  SYSERR_OUT_OF_MEMORY...
            - Field introduced in 18.2.6.
        type: str
    tenant_ref:
        description:
            - Tenant that this object belongs to.
            - It is a reference to an object of type tenant.
            - Field introduced in 18.2.6.
        type: str
    type:
        description:
            - Type of the image patch/system.
            - Enum options - IMAGE_TYPE_PATCH, IMAGE_TYPE_SYSTEM.
            - Field introduced in 18.2.6.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid of the image.
            - Field introduced in 18.2.6.
        type: str


extends_documentation_fragment:
    - avi
'''

EXAMPLES = """
- name: Example to create Image object
  avi_image:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_image
"""

RETURN = '''
obj:
    description: Image (api/image) object
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
        controller_info=dict(type='dict',),
        migrations=dict(type='dict',),
        name=dict(type='str', required=True),
        se_info=dict(type='dict',),
        status=dict(type='str',),
        tenant_ref=dict(type='str',),
        type=dict(type='str',),
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
    return avi_ansible_api(module, 'image',
                           set([]))


if __name__ == '__main__':
    main()
