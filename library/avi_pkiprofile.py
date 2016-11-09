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
# Comment: import * is to make the modules work in ansible 2.0 environments
# from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.basic import *
from avi.sdk.utils.ansible_utils import (ansible_return, purge_optional_fields,
    avi_obj_cmp, cleanup_absent_fields, avi_ansible_api)

EXAMPLES = """
- code: 'avi_pkiprofile controller=10.10.25.42 username=admin '
            ' password=something'
            ' state=present name=sample_pkiprofile'
description: "Adds/Deletes PKIProfile configuration from Avi Controller."
"""

DOCUMENTATION = '''
---
module: avi_pkiprofile
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: PKIProfile Configuration
description:
    - This module is used to configure PKIProfile object
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
    ca_certs:
        description:
            - List of Certificate Authorities (Root and Intermediate) trusted that is used for certificate validation
        type: SSLCertificate
    created_by:
        description:
            - Creator name
        type: string
    crl_check:
        description:
            - When enabled, Avi will verify via CRL checks that certificates in the trust chain have not been revoked.
        default: True
        type: bool
    crls:
        description:
            - Certificate Revocation Lists
        type: CRL
    ignore_peer_chain:
        description:
            - When enabled, Avi will not trust Intermediate and Root certs presented by a client.  Instead, only the chain certs configured in the Certificate Authority section will be used to verify trust of the client's cert.
        default: False
        type: bool
    name:
        description:
            - Name of the PKI Profile
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
    validate_only_leaf_crl:
        description:
            - When enabled, Avi will only validate the revocation status of the leaf certificate using CRL. To enable validation for the entire chain, disable this option and provide all the relevant CRLs
        default: True
        type: bool
'''

RETURN = '''
obj:
    description: PKIProfile (api/pkiprofile) object
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
                ca_certs=dict(
                    type='list',
                    ),
                created_by=dict(
                    type='str',
                    ),
                crl_check=dict(
                    type='bool',
                    ),
                crls=dict(
                    type='list',
                    ),
                ignore_peer_chain=dict(
                    type='bool',
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
                validate_only_leaf_crl=dict(
                    type='bool',
                    ),
                ),
        )
        return avi_ansible_api(module, 'pkiprofile',
                               set([]))
    except:
        raise


if __name__ == '__main__':
    main()