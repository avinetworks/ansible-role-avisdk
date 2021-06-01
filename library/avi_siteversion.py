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
module: avi_siteversion
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>

short_description: Module for setup of SiteVersion Avi RESTful Object
description:
    - This module is used to configure SiteVersion object
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
    datetime:
        description:
            - This field represents the creation time of the federateddiff.
            - Field introduced in 20.1.1.
        type: str
    name:
        description:
            - Name of the site.
            - Field introduced in 20.1.1.
        required: true
        type: str
    prev_target_version:
        description:
            - Previous targer version for a site.
            - Field introduced in 20.1.1.
        type: int
    replication_state:
        description:
            - Replication state for a site.
            - Enum options - REPLICATION_STATE_FASTFORWARD, REPLICATION_STATE_FORCESYNC, REPLICATION_STATE_STREAMING, REPLICATION_STATE_SUSPENDED,
            - REPLICATION_STATE_INIT, REPLICATION_STATE_WAIT, REPLICATION_STATE_NOT_APPLICABLE.
            - Field introduced in 20.1.1.
        type: str
    site_id:
        description:
            - Cluster uuid of the site.
            - Field introduced in 20.1.1.
        type: str
    target_timeline:
        description:
            - Target timeline of the site.
            - Field introduced in 20.1.1.
        type: str
    target_version:
        description:
            - Target version of the site.
            - Field introduced in 20.1.1.
        type: int
    tenant_ref:
        description:
            - Tenant that this object belongs to.
            - It is a reference to an object of type tenant.
            - Field introduced in 20.1.1.
        type: str
    timeline:
        description:
            - Timeline of the site.
            - Field introduced in 20.1.1.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid of the siteversion object.
            - Field introduced in 20.1.1.
        type: str
    version:
        description:
            - Version of the site.
            - Field introduced in 20.1.1.
        type: int
    version_type:
        description:
            - Type of message for which version is maintained.
            - Enum options - CONFIG_VERSION, HEALTH_STATUS_VERSION.
            - Field introduced in 20.1.1.
        type: str


extends_documentation_fragment:
    - avi
'''

EXAMPLES = """
- name: Example to create SiteVersion object
  avi_siteversion:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_siteversion
"""

RETURN = '''
obj:
    description: SiteVersion (api/siteversion) object
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
        datetime=dict(type='str',),
        name=dict(type='str', required=True),
        prev_target_version=dict(type='int',),
        replication_state=dict(type='str',),
        site_id=dict(type='str',),
        target_timeline=dict(type='str',),
        target_version=dict(type='int',),
        tenant_ref=dict(type='str',),
        timeline=dict(type='str',),
        url=dict(type='str',),
        uuid=dict(type='str',),
        version=dict(type='int',),
        version_type=dict(type='str',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk>=17.1) or requests is not installed. '
            'For more details visit https://github.com/vmware/alb-sdk.'))
    return avi_ansible_api(module, 'siteversion',
                           set())


if __name__ == '__main__':
    main()
