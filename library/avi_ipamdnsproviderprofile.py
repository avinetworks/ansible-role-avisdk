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
  - avi_ipamdnsproviderprofile:
      controller: ''
      username: ''
      password: ''
      internal_profile:
        dns_service_domain:
        - domain_name: ashish.local
          num_dns_ip: 1
          pass_through: true
          record_ttl: 100
        - domain_name: guru.local
          num_dns_ip: 1
          pass_through: true
          record_ttl: 200
        ttl: 300
      name: Ashish-DNS
      tenant_ref: Demo
      type: IPAMDNS_TYPE_INTERNAL
'''
DOCUMENTATION = '''
---
module: avi_ipamdnsproviderprofile
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: IpamDnsProviderProfile Configuration
description:
    - This module is used to configure IpamDnsProviderProfile object
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
    aws_profile:
        description:
            - Provider details if type is AWS
        type: IpamDnsAwsProfile
    gcp_profile:
        description:
            - Provider details if type is Google Cloud
        type: IpamDnsGCPProfile
    infoblox_profile:
        description:
            - Provider details if type is Infoblox
        type: IpamDnsInfobloxProfile
    internal_profile:
        description:
            - Provider details if type is Avi
        type: IpamDnsInternalProfile
    name:
        description:
            - Name for the IPAM/DNS Provider profile
        required: true
        type: string
    openstack_profile:
        description:
            - Provider details if type is OpenStack
        type: IpamDnsOpenstackProfile
    tenant_ref:
        description:
            - Not present. object ref Tenant.
        type: string
    type:
        description:
            - Provider Type for the IPAM/DNS Provider profile
        required: true
        type: string
    url:
        description:
            - url
        required: true
        type: string
    uuid:
        description:
            - UUID of the IPAM/DNS Provider profile
        type: string
'''

RETURN = '''
obj:
    description: IpamDnsProviderProfile (api/ipamdnsproviderprofile) object
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
                aws_profile=dict(
                    type='dict',
                    ),
                gcp_profile=dict(
                    type='dict',
                    ),
                infoblox_profile=dict(
                    type='dict',
                    ),
                internal_profile=dict(
                    type='dict',
                    ),
                name=dict(
                    type='str',
                    ),
                openstack_profile=dict(
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
        return avi_ansible_api(module, 'ipamdnsproviderprofile',
                               set([]))
    except:
        raise


if __name__ == '__main__':
    main()