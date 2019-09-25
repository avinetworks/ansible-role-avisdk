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
module: avi_serverautoscalepolicy
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>

short_description: Module for setup of ServerAutoScalePolicy Avi RESTful Object
description:
    - This module is used to configure ServerAutoScalePolicy object
    - more examples at U(https://github.com/avinetworks/devops)
requirements: [ avisdk ]
version_added: "2.4"
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
            - User defined description for the object.
        type: str
    intelligent_autoscale:
        description:
            - Use avi intelligent autoscale algorithm where autoscale is performed by comparing load on the pool against estimated capacity of all the servers.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    intelligent_scalein_margin:
        description:
            - Maximum extra capacity as percentage of load used by the intelligent scheme.
            - Scalein is triggered when available capacity is more than this margin.
            - Allowed values are 1-99.
            - Default value when not specified in API or module is interpreted by Avi Controller as 40.
        type: int
    intelligent_scaleout_margin:
        description:
            - Minimum extra capacity as percentage of load used by the intelligent scheme.
            - Scaleout is triggered when available capacity is less than this margin.
            - Allowed values are 1-99.
            - Default value when not specified in API or module is interpreted by Avi Controller as 20.
        type: int
    max_scalein_adjustment_step:
        description:
            - Maximum number of servers to scalein simultaneously.
            - The actual number of servers to scalein is chosen such that target number of servers is always more than or equal to the min_size.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
        type: int
    max_scaleout_adjustment_step:
        description:
            - Maximum number of servers to scaleout simultaneously.
            - The actual number of servers to scaleout is chosen such that target number of servers is always less than or equal to the max_size.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
        type: int
    max_size:
        description:
            - Maximum number of servers after scaleout.
            - Allowed values are 0-400.
        type: int
    min_size:
        description:
            - No scale-in happens once number of operationally up servers reach min_servers.
            - Allowed values are 0-400.
        type: int
    name:
        description:
            - Name of the object.
        required: true
        type: str
    scalein_alertconfig_refs:
        description:
            - Trigger scalein when alerts due to any of these alert configurations are raised.
            - It is a reference to an object of type alertconfig.
        type: list
    scalein_cooldown:
        description:
            - Cooldown period during which no new scalein is triggered to allow previous scalein to successfully complete.
            - Default value when not specified in API or module is interpreted by Avi Controller as 300.
        type: int
    scaleout_alertconfig_refs:
        description:
            - Trigger scaleout when alerts due to any of these alert configurations are raised.
            - It is a reference to an object of type alertconfig.
        type: list
    scaleout_cooldown:
        description:
            - Cooldown period during which no new scaleout is triggered to allow previous scaleout to successfully complete.
            - Default value when not specified in API or module is interpreted by Avi Controller as 300.
        type: int
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    use_predicted_load:
        description:
            - Use predicted load rather than current load.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    uuid:
        description:
            - Unique object identifier of the object.
        type: str


extends_documentation_fragment:
    - avi
'''

EXAMPLES = """
- name: Example to create ServerAutoScalePolicy object
  avi_serverautoscalepolicy:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_serverautoscalepolicy
"""

RETURN = '''
obj:
    description: ServerAutoScalePolicy (api/serverautoscalepolicy) object
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
        intelligent_autoscale=dict(type='bool',),
        intelligent_scalein_margin=dict(type='int',),
        intelligent_scaleout_margin=dict(type='int',),
        max_scalein_adjustment_step=dict(type='int',),
        max_scaleout_adjustment_step=dict(type='int',),
        max_size=dict(type='int',),
        min_size=dict(type='int',),
        name=dict(type='str', required=True),
        scalein_alertconfig_refs=dict(type='list',),
        scalein_cooldown=dict(type='int',),
        scaleout_alertconfig_refs=dict(type='list',),
        scaleout_cooldown=dict(type='int',),
        tenant_ref=dict(type='str',),
        url=dict(type='str',),
        use_predicted_load=dict(type='bool',),
        uuid=dict(type='str',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk>=17.1) or requests is not installed. '
            'For more details visit https://github.com/avinetworks/sdk.'))
    return avi_ansible_api(module, 'serverautoscalepolicy',
                           set([]))


if __name__ == '__main__':
    main()
