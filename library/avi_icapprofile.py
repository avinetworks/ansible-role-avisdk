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
module: avi_icapprofile
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>

short_description: Module for setup of IcapProfile Avi RESTful Object
description:
    - This module is used to configure IcapProfile object
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
    buffer_size:
        description:
            - The maximum buffer size for the http request body.
            - If the request body exceeds this size, the request will not be checked by the icap server.
            - In this case, the configured action will be executed and a significant log entry will be generated.
            - Allowed values are 1-51200.
            - Field introduced in 20.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as 51200.
        type: int
    buffer_size_exceed_action:
        description:
            - Decide what should happen if the request body size exceeds the configured buffer size.
            - If this is set to fail open, the request will not be checked by the icap server.
            - If this is set to fail closed, the request will be rejected with 413 status code.
            - Enum options - ICAP_FAIL_OPEN, ICAP_FAIL_CLOSED.
            - Field introduced in 20.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as ICAP_FAIL_OPEN.
        type: str
    cloud_ref:
        description:
            - The cloud where this object belongs to.
            - This must match the cloud referenced in the pool group below.
            - It is a reference to an object of type cloud.
            - Field introduced in 20.1.1.
        type: str
    description:
        description:
            - A description for this icap profile.
            - Field introduced in 20.1.1.
        type: str
    enable_preview:
        description:
            - Use the icap preview feature as described in rfc 3507 section 4.5.
            - Field introduced in 20.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    fail_action:
        description:
            - Decide what should happen if there is a problem with the icap server like communication timeout, protocol error, pool error, etc.
            - If this is set to fail open, the request will continue, but will create a significant log entry.
            - If this is set to fail closed, the request will be rejected with a 503 status code.
            - Enum options - ICAP_FAIL_OPEN, ICAP_FAIL_CLOSED.
            - Field introduced in 20.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as ICAP_FAIL_OPEN.
        type: str
    name:
        description:
            - Name of the icap profile.
            - Field introduced in 20.1.1.
        required: true
        type: str
    pool_group_ref:
        description:
            - The pool group which is used to connect to icap servers.
            - It is a reference to an object of type poolgroup.
            - Field introduced in 20.1.1.
        required: true
        type: str
    preview_size:
        description:
            - The icap preview size as described in rfc 3507 section 4.5.
            - This should not exceed the size supported by the icap server.
            - If this is set to 0, only the http header will be sent to the icap server as a preview.
            - To disable preview completely, set the enable-preview option to false.
            - Allowed values are 0-5000.
            - Field introduced in 20.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as 5000.
        type: int
    response_timeout:
        description:
            - How long do we wait for a request to the icap server to finish.
            - If this timeout is exceeded, the request to the icap server will be aborted and the configured fail action is executed.
            - Allowed values are 50-3600000.
            - Field introduced in 20.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1000.
        type: int
    service_uri:
        description:
            - The path and query component of the icap url.
            - Host name and port will be taken from the pool.
            - Field introduced in 20.1.1.
        required: true
        type: str
    slow_response_warning_threshold:
        description:
            - If the icap request takes longer than this value, this request will generate a significant log entry.
            - Allowed values are 50-3600000.
            - Field introduced in 20.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as 500.
        type: int
    tenant_ref:
        description:
            - Tenant which this object belongs to.
            - It is a reference to an object of type tenant.
            - Field introduced in 20.1.1.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid of the icap profile.
            - Field introduced in 20.1.1.
        type: str
    vendor:
        description:
            - The vendor of the icap server.
            - Enum options - ICAP_VENDOR_GENERIC, ICAP_VENDOR_OPSWAT.
            - Field introduced in 20.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as ICAP_VENDOR_OPSWAT.
        type: str


extends_documentation_fragment:
    - avi
'''

EXAMPLES = """
- name: Example to create IcapProfile object
  avi_icapprofile:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_icapprofile
"""

RETURN = '''
obj:
    description: IcapProfile (api/icapprofile) object
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
        buffer_size=dict(type='int',),
        buffer_size_exceed_action=dict(type='str',),
        cloud_ref=dict(type='str',),
        description=dict(type='str',),
        enable_preview=dict(type='bool',),
        fail_action=dict(type='str',),
        name=dict(type='str', required=True),
        pool_group_ref=dict(type='str', required=True),
        preview_size=dict(type='int',),
        response_timeout=dict(type='int',),
        service_uri=dict(type='str', required=True),
        slow_response_warning_threshold=dict(type='int',),
        tenant_ref=dict(type='str',),
        url=dict(type='str',),
        uuid=dict(type='str',),
        vendor=dict(type='str',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk>=17.1) or requests is not installed. '
            'For more details visit https://github.com/avinetworks/sdk.'))
    return avi_ansible_api(module, 'icapprofile',
                           set())


if __name__ == '__main__':
    main()