#!/usr/bin/python
"""
# Created on July 24, 2017
#
# @author: Vilian Atmadzhov (vilian.atmadzhov@paddypowerbetfair.com) GitHub ID: vivobg
#
# module_check: not supported
#
# Copyright: (c) 2017 Gaurav Rastogi, <grastogi@avinetworks.com>
#                     Vilian Atmadzhov, <vilian.atmadzhov@paddypowerbetfair.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#
"""


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}


DOCUMENTATION = '''
---
module: avi_api_version
author: Vilian Atmadzhov (@vivobg) <vilian.atmadzhov@paddypowerbetfair.com>

short_description: Avi API Version Module
description:
    - This module can be used to obtain the version of the Avi REST API. U(https://avinetworks.com/)
version_added: 2.5
requirements: [ avisdk ]
options: {}
extends_documentation_fragment:
    - avi
'''

EXAMPLES = '''
  - name: Get AVI API version
    avi_api_version:
      controller: ""
      username: ""
      password: ""
      tenant: ""
    register: avi_controller_version
'''


RETURN = '''
obj:
    description: Avi REST resource
    returned: success, changed
    type: dict
'''

from ansible.module_utils.basic import AnsibleModule


try:
    from avi.sdk.avi_api import ApiSession, AviCredentials
    from avi.sdk.utils.ansible_utils import (
        avi_common_argument_spec, ansible_return)
    from pkg_resources import parse_version
    import avi.sdk
    sdk_version = getattr(avi.sdk, '__version__', None)
    if ((sdk_version is None) or
            (sdk_version and
             (parse_version(sdk_version) < parse_version('17.2.2b3')))):
        # It allows the __version__ to be '' as that value is used in d
        # evelopment builds
        raise ImportError
    HAS_AVI = True
except ImportError:
    try:
        from ansible.module_utils.network.avi.avi import (
            avi_common_argument_spec, ansible_return)
        from ansible.module_utils.network.avi.avi_api import (
            ApiSession, AviCredentials)
        HAS_AVI = True
    except ImportError:
        HAS_AVI = False


def main():
    module = AnsibleModule(argument_spec=avi_common_argument_spec())
    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk>=17.1) is not installed. '
            'For more details visit https://github.com/avinetworks/sdk.'))
    try:
        api_creds = AviCredentials()
        api_creds.update_from_ansible_module(module)
        api = ApiSession.get_session(
            api_creds.controller, api_creds.username,
            password=api_creds.password,
            timeout=api_creds.timeout, tenant=api_creds.tenant,
            tenant_uuid=api_creds.tenant_uuid, token=api_creds.token,
            port=api_creds.port)

        remote_api_version = api.remote_api_version
        remote = {}
        for key in remote_api_version.keys():
            remote[key.lower()] = remote_api_version[key]
        api.close()
        module.exit_json(changed=False, obj=remote)
    except Exception as e:
        module.fail_json(msg="Unable to get an AVI session. {}".format(e))


if __name__ == '__main__':
    main()
