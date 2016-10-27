#!/usr/bin/python
#
# Created on Aug 25, 2016
# @author: Gaurav Rastogi (grastogi@avinetworks.com)
#          Eric Anderson (eanderson@avinetworks.com)
# module_check: not supported
#
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#

from ansible.module_utils.basic import AnsibleModule
from avi.sdk.utils.ansible_utils import (ansible_return, purge_optional_fields,
    avi_obj_cmp, cleanup_absent_fields, avi_ansible_api)


EXAMPLES = '''
- avi_httppolicyset:
    controller: 10.10.27.90
    username: admin
    password: AviNetworks123!
    name: test-HTTP-Policy-Set
    tenant_ref: admin
    http_request_policy:
    rules:
      - index: 1
        enable: true
        name: test-test1
        match:
          path:
            match_case: INSENSITIVE
            match_str:
              - /test1
            match_criteria: EQUALS
        switching_action:
          action: HTTP_SWITCHING_SELECT_POOL
          status_code: HTTP_LOCAL_RESPONSE_STATUS_CODE_200
          pool_ref: "/api/pool?name=testpool1"
      - index: 2
        enable: true
        name: test-test2
        match:
          path:
            match_case: INSENSITIVE
            match_str:
              - /test2
            match_criteria: CONTAINS
        switching_action:
          action: HTTP_SWITCHING_SELECT_POOL
          status_code: HTTP_LOCAL_RESPONSE_STATUS_CODE_200
          pool_ref: "/api/pool?name=testpool2"
    is_internal_policy: false
'''
DOCUMENTATION = '''
---
module: avi_httppolicyset
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: HTTPPolicySet Configuration
description:
    - This module is used to configure HTTPPolicySet object
    - more examples at <https://github.com/avinetworks/avi-ansible-samples>
requirements: [ avisdk ]
version_added: 2.1.2
options:
    controller:
        description:
            - location of the controller
        required: true
    username:
        description:
            - username to access the Avi
        required: true
    password:
        description:
            - password of the Avi user
        required: true
    tenant:
        description:
            - tenant for the operations
        default: admin
    tenant_uuid:
        description:
            - tenant uuid for the operations
        default: ''
    state:
        description:
            - The state that should be applied on the entity.
        required: false
        default: present
        choices: ["absent","present"]
    cloud_config_cksum:
        description:
            - Checksum of cloud configuration for Pool. Internally set by cloud connector
        type: string
    created_by:
        description:
            - Creator name
        type: string
    description:
        description:
            - Not present.
        type: string
    http_request_policy:
        description:
            - HTTP request policy for the virtual service.
        type: HTTPRequestPolicy
    http_response_policy:
        description:
            - HTTP response policy for the virtual service.
        type: HTTPResponsePolicy
    http_security_policy:
        description:
            - HTTP security policy for the virtual service.
        type: HTTPSecurityPolicy
    is_internal_policy:
        description:
            - Not present.
        default: False
        type: bool
    name:
        description:
            - Name of the HTTP Policy Set
        required: true
        type: string
    tenant_ref:
        description:
            - Not present. object ref Tenant.
        type: string
    url:
        description:
            - url
        required: true
        type: string
    uuid:
        description:
            - UUID of the HTTP Policy Set
        type: string
'''

RETURN = '''
obj:
    description: HTTPPolicySet (api/httppolicyset) object
    returned: success, changed
    type: dict
'''


def main():
    try:
        module = AnsibleModule(
            argument_spec=dict(
                controller=dict(required=True),
                username=dict(required=True),
                password=dict(required=True),
                tenant=dict(default='admin'),
                tenant_uuid=dict(default=''),
                state=dict(default='present',
                           choices=['absent', 'present']),
                cloud_config_cksum=dict(
                    type='str',
                    ),
                created_by=dict(
                    type='str',
                    ),
                description=dict(
                    type='str',
                    ),
                http_request_policy=dict(
                    type='dict',
                    ),
                http_response_policy=dict(
                    type='dict',
                    ),
                http_security_policy=dict(
                    type='dict',
                    ),
                is_internal_policy=dict(
                    type='bool',
                    ),
                name=dict(
                    type='str',
                    ),
                tenant_ref=dict(
                    type='str',
                    ),
                url=dict(
                    type='str',
                    ),
                uuid=dict(
                    type='str',
                    ),
                ),
        )
        return avi_ansible_api(module, 'httppolicyset',
                               set([]))
    except:
        raise


if __name__ == '__main__':
    main()