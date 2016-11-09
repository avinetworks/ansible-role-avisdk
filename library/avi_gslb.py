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
- code: 'avi_gslb controller=10.10.25.42 username=admin '
            ' password=something'
            ' state=present name=sample_gslb'
description: "Adds/Deletes Gslb configuration from Avi Controller."
"""

DOCUMENTATION = '''
---
module: avi_gslb
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: Gslb Configuration
description:
    - This module is used to configure Gslb object
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
    clear_on_max_retries:
        description:
            - Max retries after which the remote site is treatedas a fresh start. In fresh start all the configsare downloaded.
        default: 5
        type: integer
    description:
        description:
            - Not present.
        type: string
    dns_configs:
        description:
            - Sub domain configuration for this Gslb. GslbService FQDN must be a match one of these subdomains. 
        type: DNSConfig
    leader_cluster_uuid:
        description:
            - Mark this Site as leader of Gslb configuration.  This is the one among the sites.
        type: string
    name:
        description:
            - Name for the Gslb.
        required: true
        type: string
    send_interval:
        description:
            - Frequency with which group members communicate.
        default: 15
        type: integer
    sites:
        description:
            - Select Site belonging to this Gslb.
        type: GslbSite
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
            - UUID of the Gslb.
        type: string
    view_id:
        description:
            - The view-id is used in maintenance mode to differentiate partitioned groups while they havethe same gslb namespace. Each partitioned groupwill be able to operate independently by using theview-id.
        default: 0
        type: integer
'''

RETURN = '''
obj:
    description: Gslb (api/gslb) object
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
                clear_on_max_retries=dict(
                    type='int',
                    ),
                description=dict(
                    type='str',
                    ),
                dns_configs=dict(
                    type='list',
                    ),
                leader_cluster_uuid=dict(
                    type='str',
                    ),
                name=dict(
                    type='str',
                    ),
                send_interval=dict(
                    type='int',
                    ),
                sites=dict(
                    type='list',
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
                view_id=dict(
                    type='int',
                    ),
                ),
        )
        return avi_ansible_api(module, 'gslb',
                               set([]))
    except:
        raise


if __name__ == '__main__':
    main()