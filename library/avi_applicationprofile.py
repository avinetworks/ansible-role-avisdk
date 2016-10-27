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
  - avi_applicationprofile:
      controller: ''
      username: ''
      password: ''
      http_profile:
        cache_config:
          age_header: true
          aggressive: false
          date_header: true
          default_expire: 600
          enabled: false
          heuristic_expire: false
          max_cache_size: 0
          max_object_size: 4194304
          mime_types_group_refs:
          - admin:System-Cacheable-Resource-Types
          min_object_size: 100
          query_cacheable: false
          xcache_header: true
        client_body_timeout: 0
        client_header_timeout: 10000
        client_max_body_size: 0
        client_max_header_size: 12
        client_max_request_size: 48
        compression_profile:
          compressible_content_ref: admin:System-Compressible-Content-Types
          compression: false
          remove_accept_encoding_header: true
          type: AUTO_COMPRESSION
        connection_multiplexing_enabled: true
        hsts_enabled: false
        hsts_max_age: 365
        http_to_https: false
        httponly_enabled: false
        keepalive_header: false
        keepalive_timeout: 30000
        max_bad_rps_cip: 0
        max_bad_rps_cip_uri: 0
        max_bad_rps_uri: 0
        max_rps_cip: 0
        max_rps_cip_uri: 0
        max_rps_unknown_cip: 0
        max_rps_unknown_uri: 0
        max_rps_uri: 0
        post_accept_timeout: 30000
        secure_cookie_enabled: false
        server_side_redirect_to_https: false
        spdy_enabled: false
        spdy_fwd_proxy_mode: false
        ssl_client_certificate_mode: SSL_CLIENT_CERTIFICATE_NONE
        ssl_everywhere_enabled: false
        websockets_enabled: true
        x_forwarded_proto_enabled: false
        xff_alternate_name: X-Forwarded-For
        xff_enabled: true
      name: System-HTTP
      tenant_ref: admin
      type: APPLICATION_PROFILE_TYPE_HTTP
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
        return avi_ansible_api(module, 'applicationprofile',
                               set([]))
    except:
        raise


if __name__ == '__main__':
    main()