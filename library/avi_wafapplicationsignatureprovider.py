#!/usr/bin/python3
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
module: avi_wafapplicationsignatureprovider
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>

short_description: Module for setup of WafApplicationSignatureProvider Avi RESTful Object
description:
    - This module is used to configure WafApplicationSignatureProvider object
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
    available_applications:
        description:
            - Available application names and the ruleset version, when the rules for an application changed the last time.
            - Field introduced in 20.1.1.
        type: list
    last_check_for_updates_error:
        description:
            - The error message indicating why the last update check failed.
            - Field introduced in 20.1.1.
        type: str
    last_failed_check_for_updates:
        description:
            - The last time that we checked for updates but did not get a result because of an error.
            - Field introduced in 20.1.1.
        type: dict
    last_successful_check_for_updates:
        description:
            - The last time that we checked for updates sucessfully.
            - Field introduced in 20.1.1.
        type: dict
    name:
        description:
            - Name of application specific ruleset provider.
            - Field introduced in 20.1.1.
        type: str
    ruleset_version:
        description:
            - Version of signatures.
            - Field introduced in 20.1.1.
        type: str
    signatures:
        description:
            - The waf rules.
            - Not visible in the api.
            - Field introduced in 20.1.1.
        type: list
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
            - Field introduced in 20.1.1.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Field introduced in 20.1.1.
        type: str


extends_documentation_fragment:
    - avi
'''

EXAMPLES = """
- name: Example to create WafApplicationSignatureProvider object
  avi_wafapplicationsignatureprovider:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_wafapplicationsignatureprovider
"""

RETURN = '''
obj:
    description: WafApplicationSignatureProvider (api/wafapplicationsignatureprovider) object
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
        available_applications=dict(type='list',),
        last_check_for_updates_error=dict(type='str',),
        last_failed_check_for_updates=dict(type='dict',),
        last_successful_check_for_updates=dict(type='dict',),
        name=dict(type='str',),
        ruleset_version=dict(type='str',),
        signatures=dict(type='list',),
        tenant_ref=dict(type='str',),
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
    return avi_ansible_api(module, 'wafapplicationsignatureprovider',
                           set())


if __name__ == '__main__':
    main()
