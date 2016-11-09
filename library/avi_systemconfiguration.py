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
    admin_auth_configuration:
        description:
            - Not present.
        type: AdminAuthConfiguration
    dns_configuration:
        description:
            - Not present.
        type: DNSConfiguration
    dns_virtualservice_refs:
        description:
            - DNS virtualservices hosting FQDN records for applications across Avi Vantage. If no virtualservices are provided, Avi Vantage will provide DNS services for configured applications. Switching back to Avi Vantage from DNS virtualservices is not allowed. object ref VirtualService.
        type: string
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
                controller=dict(default=os.environ.get('AVI_CONTROLLER', '')),
                username=dict(default=os.environ.get('AVI_USERNAME', '')),
                password=dict(default=os.environ.get('AVI_PASSWORD', '')),
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
                dns_virtualservice_refs=dict(
                    type='list',
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
                uuid=dict(
                    type='str',
                    ),
                ),
        )
        return avi_ansible_api(module, 'systemconfiguration',
                               set([]))
    except:
        raise


if __name__ == '__main__':
    main()