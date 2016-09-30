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
from copy import deepcopy
from avi.sdk.avi_api import ApiSession, ObjectNotFound
from avi.sdk.utils.ansible_utils import (ansible_return, purge_optional_fields,
    avi_obj_cmp, cleanup_absent_fields)


EXAMPLES = '''
- avi_applicationprofile:
    http_profile:
      max_rps_uri: 0
      keepalive_header: false
      max_rps_cip_uri: 0
      x_forwarded_proto_enabled: false
      connection_multiplexing_enabled: true
      websockets_enabled: true
      hsts_enabled: false
      xff_enabled: true
      keepalive_timeout: 30000
      ssl_client_certificate_mode: SSL_CLIENT_CERTIFICATE_NONE
      http_to_https: false
      spdy_enabled: false
      client_body_timeout: 0
      httponly_enabled: false
      hsts_max_age: 365
      max_bad_rps_cip: 0
      server_side_redirect_to_https: false
      client_max_header_size: 12
      client_max_request_size: 48
      max_rps_unknown_uri: 0
      ssl_everywhere_enabled: false
      spdy_fwd_proxy_mode: false
      post_accept_timeout: 30000
      client_header_timeout: 10000
      secure_cookie_enabled: false
      xff_alternate_name: X-Forwarded-For
      max_rps_cip: 0
      client_max_body_size: 0
      max_rps_unknown_cip: 0
      max_bad_rps_cip_uri: 0
      max_bad_rps_uri: 0
    dos_rl_profile:
      rl_profile:
        client_ip_connections_rate_limit:
          count: 0
          explicit_tracking: false
          period: 1
          action:
            status_code: HTTP_LOCAL_RESPONSE_STATUS_CODE_429
            type: RL_ACTION_NONE
          burst_sz: 0
          fine_grain: false
    type: APPLICATION_PROFILE_TYPE_HTTP
    name: MyAppProfile
'''
DOCUMENTATION = '''
---
module: avi_applicationprofile
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: ApplicationProfile Configuration
description:
    - This module is used to configure ApplicationProfile object
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
    description:
        description:
            - Not present.
        type: string
    dns_service_profile:
        description:
            - Specifies various DNS service related controls for virtual service.
        type: DnsServiceApplicationProfile
    dos_rl_profile:
        description:
            - Specifies various security related controls for virtual service.
        type: DosRateLimitProfile
    http_profile:
        description:
            - Specifies the HTTP application proxy profile parameters.
        type: HTTPApplicationProfile
    name:
        description:
            - The name of the application profile.
        required: true
        type: string
    preserve_client_ip:
        description:
            - Specifies if client IP needs to be preserved for backend connection
        default: False
        type: bool
    tcp_app_profile:
        description:
            - Specifies the TCP application proxy profile parameters.
        type: TCPApplicationProfile
    tenant_ref:
        description:
            - Not present. object ref Tenant.
        type: string
    type:
        description:
            - Specifies which application layer proxy is enabled for the virtual service.
        required: true
        type: string
    url:
        description:
            - url
        required: true
        type: string
    uuid:
        description:
            - UUID of the application profile.
        type: string
'''

RETURN = '''
obj:
    description: ApplicationProfile (api/applicationprofile) object
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
                description=dict(
                    type='str',
                    ),
                dns_service_profile=dict(
                    type='dict',
                    ),
                dos_rl_profile=dict(
                    type='dict',
                    ),
                http_profile=dict(
                    type='dict',
                    ),
                name=dict(
                    type='str',
                    ),
                preserve_client_ip=dict(
                    type='bool',
                    ),
                tcp_app_profile=dict(
                    type='dict',
                    ),
                tenant_ref=dict(
                    type='str',
                    ),
                type=dict(
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
        api = ApiSession.get_session(
                module.params['controller'],
                module.params['username'],
                module.params['password'],
                tenant=module.params['tenant'])

        state = module.params['state']
        name = module.params['name']
        sensitive_fields = set([])

        obj = deepcopy(module.params)
        obj.pop('state', None)
        obj.pop('controller', None)
        obj.pop('username', None)
        obj.pop('password', None)
        tenant = obj.pop('tenant', '')
        tenant_uuid = obj.pop('tenant_uuid', '')
        obj.pop('cloud_ref', None)

        purge_optional_fields(obj, module)

        if state == 'absent':
            try:
                rsp = api.delete_by_name(
                    'applicationprofile', name,
                    tenant=tenant, tenant_uuid=tenant_uuid)
            except ObjectNotFound:
                return module.exit_json(changed=False)
            if rsp.status_code == 204:
                return module.exit_json(changed=True)
            return module.fail_json(msg=rsp.text)
        existing_obj = api.get_object_by_name(
                'applicationprofile', name,
                tenant=tenant, tenant_uuid=tenant_uuid,
                params={'include_refs': '', 'include_name': ''})
        changed = False
        rsp = None
        if existing_obj:
            # this is case of modify as object exists. should find out
            # if changed is true or not
            changed = not avi_obj_cmp(obj, existing_obj, sensitive_fields)
            cleanup_absent_fields(obj)
            if changed:
                obj_uuid = existing_obj['uuid']
                rsp = api.put(
                    'applicationprofile/%s' % obj_uuid, data=obj,
                    tenant=tenant, tenant_uuid=tenant_uuid)
        else:
            changed = True
            rsp = api.post('applicationprofile', data=obj,
                           tenant=tenant, tenant_uuid=tenant_uuid)
        if rsp is None:
            return module.exit_json(changed=changed, obj=existing_obj)
        else:
            return ansible_return(module, rsp, changed)
    except:
        raise


if __name__ == '__main__':
    main()