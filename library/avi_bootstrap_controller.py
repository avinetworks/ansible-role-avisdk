#!/usr/bin/python
"""
# Created on 5 April, 2019
#
# @author: Shrikant Chaudhari (shrikant.chaudhari@avinetworks.com) GitHub ID: gitshrikant
#
# module_check: not supported
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
"""

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_bootstrap_controller
author: Shrikant Chaudhari (shrikant.chaudhari@avinetworks.com)
short_description: avi bootstrap controller module.
description:
    - This module can be used for initializing the password of a user.
    - This module is useful for setting up admin password for Controller bootstrap.
version_added: 2.6
requirements: [ avisdk ]
options:
    password:
        description:
            - New password to initialize controller password.
    ssh_key_pair:
        description:
            - AWS/Azure ssh key pair to login on the controller instance.

extends_documentation_fragment:
    - avi
'''

EXAMPLES = '''
  - name: Initialize user password
    avi_bootstrap_controller:
      controller: "controller_ip"
      ssh_key_pair: "/path/to/key-pair-file.pem"
      password: new_password
      api_version: "18.2.3"

'''

RETURN = '''
obj:
    description: Avi REST resource
    returned: success, changed
    type: dict
'''

import time
from ansible.module_utils.basic import AnsibleModule
import requests

try:
    from avi.sdk.avi_api import ApiSession, AviCredentials
    from avi.sdk.utils.ansible_utils import (
        avi_obj_cmp, cleanup_absent_fields, avi_common_argument_spec,
        ansible_return)
    from pkg_resources import parse_version
    import avi.sdk
    import subprocess

    sdk_version = getattr(avi.sdk, '__version__', None)
    if ((sdk_version is None) or
            (sdk_version and
             (parse_version(sdk_version) < parse_version('17.2.2b3')))):
        # It allows the __version__ to be '' as that value is used in development builds
        raise ImportError
    HAS_AVI = True
except ImportError:
    HAS_AVI = False


def controller_wait(controller_ip, round_wait=10, wait_time=3600):
    """
    It waits for controller to come up for a given wait_time (default 1 hour).
    :return: controller_up: Boolean value for controller up state.
    """
    count = 0
    max_count = wait_time / round_wait
    path = "http://" + str(controller_ip) + "/api/cluster/runtime"
    ctrl_status = False
    r = None
    while True:
        if count >= max_count:
            break
        try:
            r = requests.get(path, timeout=10, verify=False)
            # Check for controller response for login URI.
            if r.status_code in (500, 502, 503) and count < max_count:
                time.sleep(10)
                count += 1
            else:
                if r:
                    data = r.json()
                    cluster_state = data.get('cluster_state', '')
                    if cluster_state:
                        if cluster_state['state'] == 'CLUSTER_UP_NO_HA':
                            ctrl_status = True
                            break
        except (requests.Timeout, requests.exceptions.ConnectionError) as e:
            pass
    return ctrl_status


def main():
    argument_specs = dict(
        password=dict(type='str', required=True, no_log=True),
        ssh_key_pair=dict(type='str', required=True),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(argument_spec=argument_specs)

    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk) is not installed. '
            'For more details visit https://github.com/avinetworks/sdk.'))

    api_creds = AviCredentials()
    api_creds.update_from_ansible_module(module)
    new_password = module.params.get('password')
    key_pair = module.params.get('ssh_key_pair')
    # Wait for controller to come up for given con_wait_time
    controller_up = controller_wait(api_creds.controller)
    if not controller_up:
        return module.fail_json(
            msg='Something wrong with the controller. The Controller is not in the up state.')
    try:
        subprocess.check_output(
            "ssh -o \"StrictHostKeyChecking no\" -t -i " + key_pair + " admin@" +
            api_creds.controller + " \"echo -e '" + api_creds.controller + "\\n" +
            new_password + "' | sudo /opt/avi/scripts/initialize_admin_user.py\"",
            stderr=subprocess.STDOUT, shell=True)
        return module.exit_json(changed=True, msg="Successfully initialized controller with new password.")
    except Exception as e:
        return module.fail_json(msg='Fail to initialize password for controllers %s' % e)


if __name__ == '__main__':
    main()
