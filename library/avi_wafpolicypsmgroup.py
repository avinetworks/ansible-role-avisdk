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
module: avi_wafpolicypsmgroup
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>

short_description: Module for setup of WafPolicyPSMGroup Avi RESTful Object
description:
    - This module is used to configure WafPolicyPSMGroup object
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
    description:
        description:
            - Free-text comment about this group.
            - Field introduced in 18.2.3.
        type: str
    enable:
        description:
            - Enable or disable this waf rule group.
            - Field introduced in 18.2.3.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    hit_action:
        description:
            - If a rule in this group matches the match_value pattern, this action will be executed.
            - Allowed actions are waf_action_no_op and waf_action_allow_parameter.
            - Enum options - WAF_ACTION_NO_OP, WAF_ACTION_BLOCK, WAF_ACTION_ALLOW_PARAMETER.
            - Field introduced in 18.2.3.
            - Default value when not specified in API or module is interpreted by Avi Controller as WAF_ACTION_ALLOW_PARAMETER.
        type: str
    is_learning_group:
        description:
            - This field indicates that this group is used for learning.
            - Field introduced in 18.2.3.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    locations:
        description:
            - Positive security model locations.
            - These are used to partition the application name space.
            - Field introduced in 18.2.3.
        type: list
    miss_action:
        description:
            - If a rule in this group does not match the match_value pattern, this action will be executed.
            - Allowed actions are waf_action_no_op and waf_action_block.
            - Enum options - WAF_ACTION_NO_OP, WAF_ACTION_BLOCK, WAF_ACTION_ALLOW_PARAMETER.
            - Field introduced in 18.2.3.
            - Default value when not specified in API or module is interpreted by Avi Controller as WAF_ACTION_NO_OP.
        type: str
    name:
        description:
            - User defined name of the group.
            - Field introduced in 18.2.3.
        required: true
        type: str
    tenant_ref:
        description:
            - Tenant that this object belongs to.
            - It is a reference to an object of type tenant.
            - Field introduced in 18.2.3.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid of this object.
            - Field introduced in 18.2.3.
        type: str


extends_documentation_fragment:
    - avi
'''

EXAMPLES = """
- name: Example to create WafPolicyPSMGroup object
  avi_wafpolicypsmgroup:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_wafpolicypsmgroup
"""

RETURN = '''
obj:
    description: WafPolicyPSMGroup (api/wafpolicypsmgroup) object
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
        description=dict(type='str',),
        enable=dict(type='bool',),
        hit_action=dict(type='str',),
        is_learning_group=dict(type='bool',),
        locations=dict(type='list',),
        miss_action=dict(type='str',),
        name=dict(type='str', required=True),
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
    return avi_ansible_api(module, 'wafpolicypsmgroup',
                           set([]))


if __name__ == '__main__':
    main()
