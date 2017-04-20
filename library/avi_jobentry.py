#!/usr/bin/python
#
# Created on Aug 25, 2016
# @author: Gaurav Rastogi (grastogi@avinetworks.com)
#          Eric Anderson (eanderson@avinetworks.com)
# module_check: supported
# Avi Version: 17.1
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

ANSIBLE_METADATA = {'status': ['preview'], 'supported_by': 'community', 'version': '1.0'}

DOCUMENTATION = '''
---
module: avi_jobentry
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: Module for setup of JobEntry Avi RESTful Object
description:
    - This module is used to configure JobEntry object
    - more examples at U(https://github.com/avinetworks/devops)
requirements: [ avisdk ]
version_added: "2.3"
options:
    state:
        description:
            - The state that should be applied on the entity.
        default: present
        choices: ["absent","present"]
    cookie:
        description:
            - Cookie of jobentry.
    expires_at:
        description:
            - Expires_at of jobentry.
        required: true
    obj_key:
        description:
            - Obj_key of jobentry.
        required: true
    owner:
        description:
            - Enum options - job_owner_virtualservice, job_owner_ssl, job_owner_debug_virtualservice, job_owner_consistency_checker,
            - job_owner_techsupport_uploader, job_owner_pki_profile, job_owner_networksecuritypolicy, job_owner_segroup, job_owner_postgres_status.
        required: true
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
    type:
        description:
            - Enum options - job_type_vs_full_logs, job_type_vs_udf, job_type_vs_metrics_rt, job_type_ssl_cert, job_type_debugvs_pkt_capture,
            - job_type_consistency_check, job_type_techsupport, job_type_pki_profile, job_type_nsp_rule, job_type_segroup_metrics_rt, job_type_postgres_status.
        required: true
    url:
        description:
            - Avi controller URL of the object.
    uuid:
        description:
            - Unique object identifier of the object.
extends_documentation_fragment:
    - avi
'''

EXAMPLES = """
- name: Example to create JobEntry object
  avi_jobentry:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_jobentry
"""

RETURN = '''
obj:
    description: JobEntry (api/jobentry) object
    returned: success, changed
    type: dict
'''

from ansible.module_utils.basic import AnsibleModule
try:
    from avi.sdk.utils.ansible_utils import avi_common_argument_spec
    from pkg_resources import parse_version
    import avi.sdk
    sdk_version = getattr(avi.sdk, '__version__', None)
    if ((sdk_version is None) or (sdk_version and
            (parse_version(sdk_version) < parse_version('17.1')))):
        # It allows the __version__ to be '' as that value is used in development builds
        raise ImportError
    from avi.sdk.utils.ansible_utils import avi_ansible_api
    HAS_AVI = True
except ImportError:
    HAS_AVI = False


def main():
    argument_specs = dict(
        state=dict(default='present',
                   choices=['absent', 'present']),
        cookie=dict(type='str',),
        expires_at=dict(type='str', required=True),
        obj_key=dict(type='str', required=True),
        owner=dict(type='str', required=True),
        tenant_ref=dict(type='str',),
        type=dict(type='str', required=True),
        url=dict(type='str',),
        uuid=dict(type='str',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk>=17.1) is not installed. '
            'For more details visit https://github.com/avinetworks/sdk.'))
    # Added api version field in ansible api.
    return avi_ansible_api(module,
            'jobentry',set([]))

if __name__ == '__main__':
    main()
