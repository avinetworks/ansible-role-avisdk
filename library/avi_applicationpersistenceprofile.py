#!/usr/bin/python
#
# Created on Aug 25, 2016
# @author: Gaurav Rastogi (grastogi@avinetworks.com)
#          Eric Anderson (eanderson@avinetworks.com)
# module_check: not supported
# Avi Version: 16.3
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

import os
from ansible.module_utils.basic import AnsibleModule
from avi.sdk.utils.ansible_utils import (ansible_return, purge_optional_fields,
    avi_obj_cmp, cleanup_absent_fields, avi_ansible_api)


EXAMPLES = '''
  - avi_applicationpersistenceprofile:
      controller: ''
      username: ''
      password: ''
      http_cookie_persistence_profile:
        always_send_cookie: false
        cookie_name: My-HTTP
        key:
        - aes_key: ShYGZdMks8j6Bpvm2sCvaXWzvXms2Z9ob+TTjRy46lQ=
          name: c1276819-550c-4adf-912d-59efa5fd7269
        - aes_key: OGsyVk84VCtyMENFOW0rMnRXVnNrb0RzdG5mT29oamJRb0dlbHZVSjR1az0=
          name: a080de57-77c3-4580-a3ea-e7a6493c14fd
        - aes_key: UVN0cU9HWmFUM2xOUzBVcmVXaHFXbnBLVUUxMU1VSktSVU5HWjJOWmVFMTBUMUV4UmxsNk4xQmFZejA9
          name: 60478846-33c6-484d-868d-bbc324fce4a5
        timeout: 15
      name: My-HTTP-Cookie
      persistence_type: PERSISTENCE_TYPE_HTTP_COOKIE
      server_hm_down_recovery: HM_DOWN_PICK_NEW_SERVER
      tenant_ref: Demo
'''
DOCUMENTATION = '''
---
module: avi_applicationpersistenceprofile
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: ApplicationPersistenceProfile Configuration
description:
    - This module is used to configure ApplicationPersistenceProfile object
    - more examples at <https://github.com/avinetworks/avi-ansible-samples>
requirements: [ avisdk ]
version_added: 2.3
options:
    controller:
        description:
            - location of the controller. Environment variable AVI_CONTROLLER is default
    username:
        description:
            - username to access the Avi. Environment variable AVI_USERNAME is default
    password:
        description:
            - password of the Avi user. Environment variable AVI_PASSWORD is default
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
    app_cookie_persistence_profile:
        description:
            - Specifies the Application Cookie Persistence profile parameters.
        type: AppCookiePersistenceProfile
    description:
        description:
            - Not present.
        type: string
    hdr_persistence_profile:
        description:
            - Specifies the custom HTTP Header Persistence profile parameters.
        type: HdrPersistenceProfile
    http_cookie_persistence_profile:
        description:
            - Specifies the HTTP Cookie Persistence profile parameters.
        type: HttpCookiePersistenceProfile
    ip_persistence_profile:
        description:
            - Specifies the Client IP Persistence profile parameters.
        type: IPPersistenceProfile
    name:
        description:
            - A user-friendly name for the persistence profile.
        required: true
        type: string
    persistence_type:
        description:
            - Method used to persist clients to the same server for a duration of time or a session.
        required: true
        type: string
    server_hm_down_recovery:
        description:
            - Specifies behavior when a persistent server has been marked down by a health monitor.
        default: 1
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
            - UUID of the persistence profile.
        type: string
'''

RETURN = '''
obj:
    description: ApplicationPersistenceProfile (api/applicationpersistenceprofile) object
    returned: success, changed
    type: dict
'''

def main():
    try:
        module = AnsibleModule(
            argument_spec=dict(
                controller=dict(default=os.environ.get('AVI_CONTROLLER', '')),
                username=dict(default=os.environ.get('AVI_USERNAME', '')),
                password=dict(default=os.environ.get('AVI_PASSWORD', '')),
                tenant=dict(default='admin'),
                tenant_uuid=dict(default=''),
                state=dict(default='present',
                           choices=['absent', 'present']),
                app_cookie_persistence_profile=dict(
                    type='dict',
                    ),
                description=dict(
                    type='str',
                    ),
                hdr_persistence_profile=dict(
                    type='dict',
                    ),
                http_cookie_persistence_profile=dict(
                    type='dict',
                    ),
                ip_persistence_profile=dict(
                    type='dict',
                    ),
                name=dict(
                    type='str',
                    ),
                persistence_type=dict(
                    type='str',
                    ),
                server_hm_down_recovery=dict(
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
        return avi_ansible_api(module, 'applicationpersistenceprofile',
                               set([]))
    except:
        raise


if __name__ == '__main__':
    main()