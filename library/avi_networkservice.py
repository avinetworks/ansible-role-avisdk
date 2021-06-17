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
module: avi_networkservice
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>

short_description: Module for setup of NetworkService Avi RESTful Object
description:
    - This module is used to configure NetworkService object
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
    cloud_ref:
        description:
            - It is a reference to an object of type cloud.
            - Field introduced in 18.2.5.
        type: str
    labels:
        description:
            - Key value pairs for granular object access control.
            - Also allows for classification and tagging of similar objects.
            - Field deprecated in 20.1.5.
            - Field introduced in 20.1.2.
            - Maximum of 4 items allowed.
        type: list
    markers:
        description:
            - List of labels to be used for granular rbac.
            - Field introduced in 20.1.5.
            - Allowed in basic edition, essentials edition, enterprise edition.
        type: list
    name:
        description:
            - Name of the networkservice.
            - Field introduced in 18.2.5.
        required: true
        type: str
    routing_service:
        description:
            - Routing information of the networkservice.
            - Field introduced in 18.2.5.
        type: dict
    se_group_ref:
        description:
            - Service engine group to which the service is applied.
            - It is a reference to an object of type serviceenginegroup.
            - Field introduced in 18.2.5.
        required: true
        type: str
    service_type:
        description:
            - Indicates the type of networkservice.
            - Enum options - ROUTING_SERVICE.
            - Field introduced in 18.2.5.
        required: true
        type: str
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
            - Field introduced in 18.2.5.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid of the networkservice.
            - Field introduced in 18.2.5.
        type: str
    vrf_ref:
        description:
            - Vrf context to which the service is scoped.
            - It is a reference to an object of type vrfcontext.
            - Field introduced in 18.2.5.
        required: true
        type: str


extends_documentation_fragment:
    - avi
'''

EXAMPLES = """
- name: Example to create NetworkService object
  avi_networkservice:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_networkservice
"""

RETURN = '''
obj:
    description: NetworkService (api/networkservice) object
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
        cloud_ref=dict(type='str',),
        labels=dict(type='list',),
        markers=dict(type='list',),
        name=dict(type='str', required=True),
        routing_service=dict(type='dict',),
        se_group_ref=dict(type='str', required=True),
        service_type=dict(type='str', required=True),
        tenant_ref=dict(type='str',),
        url=dict(type='str',),
        uuid=dict(type='str',),
        vrf_ref=dict(type='str', required=True),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk>=17.1) or requests is not installed. '
            'For more details visit https://github.com/vmware/alb-sdk.'))
    return avi_ansible_api(module, 'networkservice',
                           set())


if __name__ == '__main__':
    main()
