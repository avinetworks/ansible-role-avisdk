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

EXAMPLES = """
- code: 'avi_applicationpersistenceprofile controller=10.10.25.42 username=admin '
            ' password=something'
            ' state=present name=sample_applicationpersistenceprofile'
description: "Adds/Deletes ApplicationPersistenceProfile configuration from Avi Controller."
"""

DOCUMENTATION = '''
---
module: avi_applicationpersistenceprofile
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: ApplicationPersistenceProfile Configuration
description:
    - This module is used to configure ApplicationPersistenceProfile object
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
                controller=dict(required=True),
                username=dict(required=True),
                password=dict(required=True),
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
                    'applicationpersistenceprofile', name,
                    tenant=tenant, tenant_uuid=tenant_uuid)
            except ObjectNotFound:
                return module.exit_json(changed=False)
            if rsp.status_code == 204:
                return module.exit_json(changed=True)
            return module.fail_json(msg=rsp.text)
        existing_obj = api.get_object_by_name(
                'applicationpersistenceprofile', name,
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
                    'applicationpersistenceprofile/%s' % obj_uuid, data=obj,
                    tenant=tenant, tenant_uuid=tenant_uuid)
        else:
            changed = True
            rsp = api.post('applicationpersistenceprofile', data=obj,
                           tenant=tenant, tenant_uuid=tenant_uuid)
        if rsp is None:
            return module.exit_json(changed=changed, obj=existing_obj)
        else:
            return ansible_return(module, rsp, changed)
    except:
        raise


if __name__ == '__main__':
    main()