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
- code: 'avi_systemconfiguration controller=10.10.25.42 username=admin '
            ' password=something'
            ' state=present name=sample_systemconfiguration'
description: "Adds/Deletes SystemConfiguration configuration from Avi Controller."
"""

DOCUMENTATION = '''
---
module: avi_systemconfiguration
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: SystemConfiguration Configuration
description:
    - This module is used to configure SystemConfiguration object
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
    admin_auth_configuration:
        description:
            - Not present.
        type: AdminAuthConfiguration
    dns_configuration:
        description:
            - Not present.
        type: DNSConfiguration
    docker_mode:
        description:
            - Not present.
        default: False
        type: bool
    email_configuration:
        description:
            - Not present.
        type: EmailConfiguration
    global_tenant_config:
        description:
            - Not present.
        type: TenantConfiguration
    linux_configuration:
        description:
            - Not present.
        type: LinuxConfiguration
    mgmt_ip_access_control:
        description:
            - Configure Ip Access control for controller to restrict open access.
        type: MgmtIpAccessControl
    ntp_configuration:
        description:
            - Not present.
        type: NTPConfiguration
    portal_configuration:
        description:
            - Not present.
        type: PortalConfiguration
    proxy_configuration:
        description:
            - Not present.
        type: ProxyConfiguration
    snmp_configuration:
        description:
            - Not present.
        type: SnmpConfiguration
    ssh_ciphers:
        description:
            - Allowed Ciphers list for SSH to the management interface on the Controller and Service Engines. If this is not specified, all the default ciphers are allowed. ssh -Q cipher provides the list of default ciphers supported.
        type: string
    ssh_hmacs:
        description:
            - Allowed HMAC list for SSH to the management interface on the Controller and Service Engines. If this is not specified, all the default HMACs are allowed. ssh -Q mac provides the list of default HMACs supported.
        type: string
    tech_support_uploader_configuration:
        description:
            - Not present.
        type: TechSupportUploaderConfiguration
    url:
        description:
            - url
        required: true
        type: string
    use_controller_dns_server:
        description:
            - Use Avi controller for providing DNS services for all domains configured in all of DNS profiles. If this option is not selected, then a DNS virtual service should be created, which will host and respond to DNS queries for all the domains configured across DNS profiles.
        default: True
        type: bool
    uuid:
        description:
            - Not present.
        type: string
'''

RETURN = '''
obj:
    description: SystemConfiguration (api/systemconfiguration) object
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
                admin_auth_configuration=dict(
                    type='dict',
                    ),
                dns_configuration=dict(
                    type='dict',
                    ),
                docker_mode=dict(
                    type='bool',
                    ),
                email_configuration=dict(
                    type='dict',
                    ),
                global_tenant_config=dict(
                    type='dict',
                    ),
                linux_configuration=dict(
                    type='dict',
                    ),
                mgmt_ip_access_control=dict(
                    type='dict',
                    ),
                ntp_configuration=dict(
                    type='dict',
                    ),
                portal_configuration=dict(
                    type='dict',
                    ),
                proxy_configuration=dict(
                    type='dict',
                    ),
                snmp_configuration=dict(
                    type='dict',
                    ),
                ssh_ciphers=dict(
                    type='list',
                    ),
                ssh_hmacs=dict(
                    type='list',
                    ),
                tech_support_uploader_configuration=dict(
                    type='dict',
                    ),
                url=dict(
                    type='str',
                    ),
                use_controller_dns_server=dict(
                    type='bool',
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
                    'systemconfiguration', name,
                    tenant=tenant, tenant_uuid=tenant_uuid)
            except ObjectNotFound:
                return module.exit_json(changed=False)
            if rsp.status_code == 204:
                return module.exit_json(changed=True)
            return module.fail_json(msg=rsp.text)
        existing_obj = api.get_object_by_name(
                'systemconfiguration', name,
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
                    'systemconfiguration/%s' % obj_uuid, data=obj,
                    tenant=tenant, tenant_uuid=tenant_uuid)
        else:
            changed = True
            rsp = api.post('systemconfiguration', data=obj,
                           tenant=tenant, tenant_uuid=tenant_uuid)
        if rsp is None:
            return module.exit_json(changed=changed, obj=existing_obj)
        else:
            return ansible_return(module, rsp, changed)
    except:
        raise


if __name__ == '__main__':
    main()