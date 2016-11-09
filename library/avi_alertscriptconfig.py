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
  - avi_alertscriptconfig:
      username: ''
      controller: ''
      password: ''
      action_script: "#!/usr/bin/python\nimport sys\nfrom avi.sdk.samples.autoscale.aws_samplescaleout\
        \ import scaleout\naws_setting = {\n        'ec2_region': 'us-west-2',\n \
        \       'tenant': 'Demo',\n        'aws_access_key_id': 'ASDAS123412341234',\n\
        \        'aws_secret_access_key': '523lk45j234lk5j234;5klj',\n\
        \        'image_id': 'ami-hs343234',\n        'security_group_ids': ['sg-1234567'],\n\
        \        'subnet_id': 'subnet-91dfek3',\n        'tag': 'AviDemo',\n    \
        \    'key_name': 'demo_oregon_key'\n}\nscaleout(aws_setting, *sys.argv)"
      name: AWS-Launch-Script
      tenant_ref: Demo
'''
DOCUMENTATION = '''
---
module: avi_alertscriptconfig
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: AlertScriptConfig Configuration
description:
    - This module is used to configure AlertScriptConfig object
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
    action_script:
        description:
            - User Defined Alert Action Script. Please refer to kb.avinetworks.com for more information.
        type: string
    name:
        description:
            - A user-friendly name of the Script
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
            - Not present.
        type: string
'''

RETURN = '''
obj:
    description: AlertScriptConfig (api/alertscriptconfig) object
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
                action_script=dict(
                    type='str',
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
        return avi_ansible_api(module, 'alertscriptconfig',
                               set([]))
    except:
        raise


if __name__ == '__main__':
    main()