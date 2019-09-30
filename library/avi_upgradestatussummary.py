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
module: avi_upgradestatussummary
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>

short_description: Module for setup of UpgradeStatusSummary Avi RESTful Object
description:
    - This module is used to configure UpgradeStatusSummary object
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
    enable_patch_rollback:
        description:
            - Check if the patch rollback is possible on this node.
            - Field introduced in 18.2.6.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    enable_rollback:
        description:
            - Check if the rollback is possible on this node.
            - Field introduced in 18.2.6.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    end_time:
        description:
            - End time of upgrade operations.
            - Field introduced in 18.2.6.
        type: str
    image_ref:
        description:
            - Image uuid for identifying the current base image.
            - It is a reference to an object of type image.
            - Field introduced in 18.2.6.
        type: str
    name:
        description:
            - Name of the system such as cluster name, se group name and se name.
            - Field introduced in 18.2.6.
        type: str
    node_type:
        description:
            - Type of the system such as controller_cluster, se_group or se.
            - Enum options - NODE_CONTROLLER_CLUSTER, NODE_SE_GROUP, NODE_SE_TYPE.
            - Field introduced in 18.2.6.
        type: str
    obj_cloud_ref:
        description:
            - Cloud that this object belongs to.
            - It is a reference to an object of type cloud.
            - Field introduced in 18.2.6.
        type: str
    obj_state:
        description:
            - Current status of the upgrade operations.
            - Field introduced in 18.2.6.
        type: dict
    patch_image_ref:
        description:
            - Image uuid for identifying the current patch.
            - It is a reference to an object of type image.
            - Field introduced in 18.2.6.
        type: str
    start_time:
        description:
            - Start time of upgrade operations.
            - Field introduced in 18.2.6.
        type: str
    tasks_completed:
        description:
            - Upgrade tasks completed.
            - Field introduced in 18.2.6.
        type: int
    tenant_ref:
        description:
            - Tenant that this object belongs to.
            - It is a reference to an object of type tenant.
            - Field introduced in 18.2.6.
        type: str
    total_tasks:
        description:
            - Total upgrade tasks.
            - Field introduced in 18.2.6.
        type: int
    upgrade_ops:
        description:
            - Upgrade operations requested.
            - Enum options - UPGRADE, PATCH, ROLLBACK, ROLLBACKPATCH, SEGROUP_RESUME.
            - Field introduced in 18.2.6.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid identifier for the system such as cluster, se group and se.
            - Field introduced in 18.2.6.
        type: str
    version:
        description:
            - Current base image applied to this node.
            - Field introduced in 18.2.6.
        type: str


extends_documentation_fragment:
    - avi
'''

EXAMPLES = """
- name: Example to create UpgradeStatusSummary object
  avi_upgradestatussummary:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_upgradestatussummary
"""

RETURN = '''
obj:
    description: UpgradeStatusSummary (api/upgradestatussummary) object
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
        enable_patch_rollback=dict(type='bool',),
        enable_rollback=dict(type='bool',),
        end_time=dict(type='str',),
        image_ref=dict(type='str',),
        name=dict(type='str',),
        node_type=dict(type='str',),
        obj_cloud_ref=dict(type='str',),
        obj_state=dict(type='dict',),
        patch_image_ref=dict(type='str',),
        start_time=dict(type='str',),
        tasks_completed=dict(type='int',),
        tenant_ref=dict(type='str',),
        total_tasks=dict(type='int',),
        upgrade_ops=dict(type='str',),
        url=dict(type='str',),
        uuid=dict(type='str',),
        version=dict(type='str',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk>=17.1) or requests is not installed. '
            'For more details visit https://github.com/avinetworks/sdk.'))
    return avi_ansible_api(module, 'upgradestatussummary',
                           set([]))


if __name__ == '__main__':
    main()
