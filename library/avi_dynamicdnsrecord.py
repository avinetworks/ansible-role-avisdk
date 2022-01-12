#!/usr/bin/python
# module_check: supported

# Copyright 2021 VMware, Inc.  All rights reserved. VMware Confidential
# SPDX-License-Identifier: Apache License 2.0


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_dynamicdnsrecord
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of DynamicDnsRecord Avi RESTful Object
description:
    - This module is used to configure DynamicDnsRecord object
    - more examples at U(https://github.com/avinetworks/devops)
requirements: [ avisdk ]
version_added: "2.7"
options:
    state:
        description:
            - The state that should be applied on the entity.
        default: present
        choices: ["absent", "present"]
        type: str
    avi_api_update_method:
        description:
            - Default method for object update is HTTP PUT.
            - Setting to patch will override that behavior to use HTTP PATCH.
        version_added: "2.5"
        default: put
        choices: ["put", "patch"]
        type: str
    avi_api_patch_op:
        description:
            - Patch operation to use when using avi_api_update_method as patch.
        version_added: "2.5"
        choices: ["add", "replace", "delete", "remove"]
        type: str
    avi_patch_path:
        description:
            - Patch path to use when using avi_api_update_method as patch.
        type: str
    avi_patch_value:
        description:
            - Patch value to use when using avi_api_update_method as patch.
        type: str
    algorithm:
        description:
            - Specifies the algorithm to pick the ip address(es) to be returned,when multiple entries are configured.
            - This does not apply if num_records_in_response is 0.
            - Default is round-robin.
            - Enum options - DNS_RECORD_RESPONSE_ROUND_ROBIN, DNS_RECORD_RESPONSE_CONSISTENT_HASH.
            - Field introduced in 20.1.3.
            - Default value when not specified in API or module is interpreted by Avi Controller as DNS_RECORD_RESPONSE_ROUND_ROBIN.
        type: str
    cname:
        description:
            - Canonical name in cname record.
            - Field introduced in 20.1.3.
        type: dict
    delegated:
        description:
            - Configured fqdns are delegated domains (i.e.
            - They represent a zone cut).
            - Field introduced in 20.1.3.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    description:
        description:
            - Details of dns record.
            - Field introduced in 20.1.3.
        type: str
    dns_vs_uuid:
        description:
            - Uuid of the dns vs.
            - Field introduced in 20.1.3.
        type: str
    fqdn:
        description:
            - Fully qualified domain name.
            - Field introduced in 20.1.3.
        type: str
    ip6_address:
        description:
            - Ipv6 address in aaaa record.
            - Field introduced in 20.1.3.
            - Maximum of 4 items allowed.
        type: list
    ip_address:
        description:
            - Ip address in a record.
            - Field introduced in 20.1.3.
            - Maximum of 4 items allowed.
        type: list
    metadata:
        description:
            - Internal metadata for the dns record.
            - Field introduced in 20.1.3.
        type: str
    mx_records:
        description:
            - Mx record.
            - Field introduced in 20.1.3.
            - Maximum of 4 items allowed.
        type: list
    name:
        description:
            - Dynamicdnsrecord name, needed for a top level uuid protobuf, for display in shell.
            - Field introduced in 20.1.3.
        type: str
    ns:
        description:
            - Name server information in ns record.
            - Field introduced in 20.1.3.
            - Maximum of 13 items allowed.
        type: list
    num_records_in_response:
        description:
            - Specifies the number of records returned by the dns service.enter 0 to return all records.
            - Default is 0.
            - Allowed values are 0-20.
            - Special values are 0- return all records.
            - Field introduced in 20.1.3.
        type: int
    service_locators:
        description:
            - Service locator info in srv record.
            - Field introduced in 20.1.3.
            - Maximum of 4 items allowed.
        type: list
    tenant_ref:
        description:
            - Tenant_uuid from dns vs's tenant_uuid.
            - It is a reference to an object of type tenant.
            - Field introduced in 20.1.3.
        type: str
    ttl:
        description:
            - Time to live for this dns record.
            - Field introduced in 20.1.3.
        type: int
    txt_records:
        description:
            - Text record.
            - Field introduced in 20.1.3.
            - Maximum of 4 items allowed.
        type: list
    type:
        description:
            - Dns record type.
            - Enum options - DNS_RECORD_OTHER, DNS_RECORD_A, DNS_RECORD_NS, DNS_RECORD_CNAME, DNS_RECORD_SOA, DNS_RECORD_PTR, DNS_RECORD_HINFO, DNS_RECORD_MX,
            - DNS_RECORD_TXT, DNS_RECORD_RP, DNS_RECORD_DNSKEY, DNS_RECORD_AAAA, DNS_RECORD_SRV, DNS_RECORD_OPT, DNS_RECORD_RRSIG, DNS_RECORD_AXFR,
            - DNS_RECORD_ANY.
            - Field introduced in 20.1.3.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid of the dns record.
            - Field introduced in 20.1.3.
        type: str
    wildcard_match:
        description:
            - Enable wild-card match of fqdn  if an exact match is not found in the dns table, the longest match is chosen by wild-carding the fqdn in the dns
            - request.
            - Default is false.
            - Field introduced in 20.1.3.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool


extends_documentation_fragment:
    - avi
'''

EXAMPLES = """
- hosts: all
  vars:
    avi_credentials:
      username: "admin"
      password: "something"
      controller: "192.168.15.18"
      api_version: "21.1.1"

- name: Example to create DynamicDnsRecord object
  avi_dynamicdnsrecord:
    avi_credentials: "{{ avi_credentials }}"
    state: present
    name: sample_dynamicdnsrecord
"""

RETURN = '''
obj:
    description: DynamicDnsRecord (api/dynamicdnsrecord) object
    returned: success, changed
    type: dict
'''

from ansible.module_utils.basic import AnsibleModule
try:
    from avi.sdk.utils.ansible_utils import avi_common_argument_spec
    from avi.sdk.utils.ansible_utils import (
        avi_ansible_api, avi_common_argument_spec)
    HAS_AVI = True
except ImportError:
    HAS_AVI = False


def main():
    argument_specs = dict(
        state=dict(default='present',
                   choices=['absent', 'present']),
        avi_api_update_method=dict(default='put',
                                   choices=['put', 'patch']),
        avi_api_patch_op=dict(choices=['add', 'replace', 'delete', 'remove']),
        avi_patch_path=dict(type='str',),
        avi_patch_value=dict(type='str',),
        algorithm=dict(type='str',),
        cname=dict(type='dict',),
        delegated=dict(type='bool',),
        description=dict(type='str',),
        dns_vs_uuid=dict(type='str',),
        fqdn=dict(type='str',),
        ip6_address=dict(type='list',),
        ip_address=dict(type='list',),
        metadata=dict(type='str',),
        mx_records=dict(type='list',),
        name=dict(type='str',),
        ns=dict(type='list',),
        num_records_in_response=dict(type='int',),
        service_locators=dict(type='list',),
        tenant_ref=dict(type='str',),
        ttl=dict(type='int',),
        txt_records=dict(type='list',),
        type=dict(type='str',),
        url=dict(type='str',),
        uuid=dict(type='str',),
        wildcard_match=dict(type='bool',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk>=17.1) or requests is not installed. '
            'For more details visit https://github.com/vmware/alb-sdk.'))
    return avi_ansible_api(module, 'dynamicdnsrecord',
                           set())


if __name__ == '__main__':
    main()
