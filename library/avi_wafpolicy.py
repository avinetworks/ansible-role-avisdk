#!/usr/bin/python
#
# @author: Gaurav Rastogi (grastogi@avinetworks.com)
#          Eric Anderson (eanderson@avinetworks.com)
# module_check: supported
#
# Copyright: (c) 2017 Gaurav Rastogi, <grastogi@avinetworks.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from ansible.module_utils.basic import AnsibleModule
try:
    from avi.sdk.utils.ansible_utils import avi_common_argument_spec
    from pkg_resources import parse_version
    import avi.sdk
    sdk_version = getattr(avi.sdk, '__version__', None)
    if ((sdk_version is None) or
            (sdk_version and
             (parse_version(sdk_version) < parse_version('17.1')))):
        # It allows the __version__ to be '' as that value is used in development builds
        raise ImportError
    from avi.sdk.utils.ansible_utils import avi_ansible_api
    HAS_AVI = True
except ImportError:
    HAS_AVI = False


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_wafpolicy
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: Module for setup of WafPolicy Avi RESTful Object
description:
    - This module is used to configure WafPolicy object
    - more examples at U(https://github.com/avinetworks/devops)
requirements: [ avisdk ]
version_added: "2.5"
options:
    state:
        description:
            - The state that should be applied on the entity.
        default: present
        choices: ["absent", "present"]
    avi_api_update_method:
        description:
            - Default method for object update is HTTP PUT.
            - Setting to patch will override that behavior to use HTTP PATCH.
        version_added: "2.5"
        default: put
        choices: ["put", "patch"]
    avi_api_patch_op:
        description:
            - Patch operation to use when using avi_api_update_method as patch.
        version_added: "2.5"
        choices: ["add", "replace", "delete"]
    allow_mode_delegation:
        description:
            - Allow rules to overwrite the policy mode.
            - This must be set if the policy mode is set to enforcement.
            - Field introduced in 18.1.5, 18.2.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    created_by:
        description:
            - Creator name.
            - Field introduced in 17.2.4.
    crs_groups:
        description:
            - Waf rules are categorized in to groups based on their characterization.
            - These groups are system created with crs groups.
            - Field introduced in 17.2.1.
    description:
        description:
            - Field introduced in 17.2.1.
    failure_mode:
        description:
            - Waf policy failure mode.
            - This can be 'open' or 'closed'.
            - Enum options - WAF_FAILURE_MODE_OPEN, WAF_FAILURE_MODE_CLOSED.
            - Field introduced in 18.1.2.
            - Default value when not specified in API or module is interpreted by Avi Controller as WAF_FAILURE_MODE_OPEN.
        version_added: "2.7"
    learning:
        description:
            - Configure parameters for waf learning.
            - Field introduced in 18.1.2.
        version_added: "2.7"
    mode:
        description:
            - Waf policy mode.
            - This can be detection or enforcement.
            - It can be overwritten by rules if allow_mode_delegation is set.
            - Enum options - WAF_MODE_DETECTION_ONLY, WAF_MODE_ENFORCEMENT.
            - Field introduced in 17.2.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as WAF_MODE_DETECTION_ONLY.
        required: true
    name:
        description:
            - Field introduced in 17.2.1.
        required: true
    paranoia_level:
        description:
            - Waf ruleset paranoia  mode.
            - This is used to select rules based on the paranoia-level tag.
            - Enum options - WAF_PARANOIA_LEVEL_LOW, WAF_PARANOIA_LEVEL_MEDIUM, WAF_PARANOIA_LEVEL_HIGH, WAF_PARANOIA_LEVEL_EXTREME.
            - Field introduced in 17.2.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as WAF_PARANOIA_LEVEL_LOW.
    post_crs_groups:
        description:
            - Waf rules are categorized in to groups based on their characterization.
            - These groups are created by the user and will be enforced after the crs groups.
            - Field introduced in 17.2.1.
    pre_crs_groups:
        description:
            - Waf rules are categorized in to groups based on their characterization.
            - These groups are created by the user and will be  enforced before the crs groups.
            - Field introduced in 17.2.1.
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
            - Field introduced in 17.2.1.
    url:
        description:
            - Avi controller URL of the object.
    uuid:
        description:
            - Field introduced in 17.2.1.
    waf_crs_ref:
        description:
            - Waf core ruleset used for the crs part of this policy.
            - It is a reference to an object of type wafcrs.
            - Field introduced in 18.1.1.
        version_added: "2.7"
    waf_profile_ref:
        description:
            - Waf profile for waf policy.
            - It is a reference to an object of type wafprofile.
            - Field introduced in 17.2.1.
        required: true
extends_documentation_fragment:
    - avi
'''

EXAMPLES = """
- name: Example to create WafPolicy object
  avi_wafpolicy:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_wafpolicy
"""

RETURN = '''
obj:
    description: WafPolicy (api/wafpolicy) object
    returned: success, changed
    type: dict
'''


def main():
    argument_specs = dict(
        state=dict(default='present',
                   choices=['absent', 'present']),
        avi_api_update_method=dict(default='put',
                                   choices=['put', 'patch']),
        avi_api_patch_op=dict(choices=['add', 'replace', 'delete']),
        allow_mode_delegation=dict(type='bool',),
        created_by=dict(type='str',),
        crs_groups=dict(type='list',),
        description=dict(type='str',),
        failure_mode=dict(type='str',),
        learning=dict(type='dict',),
        mode=dict(type='str', required=True),
        name=dict(type='str', required=True),
        paranoia_level=dict(type='str',),
        post_crs_groups=dict(type='list',),
        pre_crs_groups=dict(type='list',),
        tenant_ref=dict(type='str',),
        url=dict(type='str',),
        uuid=dict(type='str',),
        waf_crs_ref=dict(type='str',),
        waf_profile_ref=dict(type='str', required=True),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk>=17.1) is not installed. '
            'For more details visit https://github.com/avinetworks/sdk.'))
    return avi_ansible_api(module, 'wafpolicy',
                           set([]))


if __name__ == '__main__':
    main()
