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
module: avi_ipreputationdb
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>

short_description: Module for setup of IPReputationDB Avi RESTful Object
description:
    - This module is used to configure IPReputationDB object
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
    base_file_refs:
        description:
            - Ip reputation db base file.
            - It is a reference to an object of type fileobject.
            - Field introduced in 20.1.1.
            - Maximum of 1 items allowed.
        type: list
    description:
        description:
            - Description.
            - Field introduced in 20.1.1.
        type: str
    incremental_file_refs:
        description:
            - Ip reputation db incremental update files.
            - It is a reference to an object of type fileobject.
            - Field introduced in 20.1.1.
        type: list
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
        type: list
    name:
        description:
            - Ip reputation db name.
            - Field introduced in 20.1.1.
        required: true
        type: str
    service_status:
        description:
            - If this object is managed by the ip reputation service, this field contain the status of this syncronization.
            - Field introduced in 20.1.1.
        type: dict
    tenant_ref:
        description:
            - Tenant that this object belongs to.
            - It is a reference to an object of type tenant.
            - Field introduced in 20.1.1.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid of this object.
            - Field introduced in 20.1.1.
        type: str
    vendor:
        description:
            - Organization providing ip reputation data.
            - Enum options - IP_REPUTATION_VENDOR_WEBROOT.
            - Field introduced in 20.1.1.
        required: true
        type: str
    version:
        description:
            - A version number for this database object.
            - This is informal for the consumer of this api only, a tool which manages this object can store version information here.
            - Field introduced in 20.1.1.
        type: str


extends_documentation_fragment:
    - avi
'''

EXAMPLES = """
- name: Example to create IPReputationDB object
  avi_ipreputationdb:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_ipreputationdb
"""

RETURN = '''
obj:
    description: IPReputationDB (api/ipreputationdb) object
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
        base_file_refs=dict(type='list',),
        description=dict(type='str',),
        incremental_file_refs=dict(type='list',),
        labels=dict(type='list',),
        markers=dict(type='list',),
        name=dict(type='str', required=True),
        service_status=dict(type='dict',),
        tenant_ref=dict(type='str',),
        url=dict(type='str',),
        uuid=dict(type='str',),
        vendor=dict(type='str', required=True),
        version=dict(type='str',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk>=17.1) or requests is not installed. '
            'For more details visit https://github.com/vmware/alb-sdk.'))
    return avi_ansible_api(module, 'ipreputationdb',
                           set())


if __name__ == '__main__':
    main()
