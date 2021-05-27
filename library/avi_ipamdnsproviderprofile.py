#!/usr/bin/python3
# module_check: supported

# Copyright 2021 VMware, Inc.  All rights reserved. VMware Confidential
# SPDX-License-Identifier: Apache License 2.0


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_ipamdnsproviderprofile
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>

short_description: Module for setup of IpamDnsProviderProfile Avi RESTful Object
description:
    - This module is used to configure IpamDnsProviderProfile object
    - more examples at U(https://github.com/avinetworks/devops)
requirements: [ avisdk ]
version_added: "2.4"
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
    allocate_ip_in_vrf:
        description:
            - If this flag is set, only allocate ip from networks in the virtual service vrf.
            - Applicable for avi vantage ipam only.
            - Field introduced in 17.2.4.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        version_added: "2.5"
        type: bool
    aws_profile:
        description:
            - Provider details if type is aws.
        type: dict
    azure_profile:
        description:
            - Provider details if type is microsoft azure.
            - Field introduced in 17.2.1.
        version_added: "2.5"
        type: dict
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 21.1.1.
        type: dict
    custom_profile:
        description:
            - Provider details if type is custom.
            - Field introduced in 17.1.1.
        type: dict
    gcp_profile:
        description:
            - Provider details if type is google cloud.
        type: dict
    infoblox_profile:
        description:
            - Provider details if type is infoblox.
        type: dict
    internal_profile:
        description:
            - Provider details if type is avi.
        type: dict
    labels:
        description:
            - Key value pairs for granular object access control.
            - Also allows for classification and tagging of similar objects.
            - Field deprecated in 20.1.5.
            - Field introduced in 20.1.2.
            - Maximum of 4 items allowed.
        type: list
    markers:
        description:
            - List of labels to be used for granular rbac.
            - Field introduced in 20.1.5.
        type: list
    name:
        description:
            - Name for the ipam/dns provider profile.
        required: true
        type: str
    oci_profile:
        description:
            - Provider details for oracle cloud.
            - Field introduced in 18.2.1,18.1.3.
        version_added: "2.9"
        type: dict
    openstack_profile:
        description:
            - Provider details if type is openstack.
        type: dict
    proxy_configuration:
        description:
            - Field introduced in 17.1.1.
        type: dict
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
        type: str
    tencent_profile:
        description:
            - Provider details for tencent cloud.
            - Field introduced in 18.2.3.
        version_added: "2.9"
        type: dict
    type:
        description:
            - Provider type for the ipam/dns provider profile.
            - Enum options - IPAMDNS_TYPE_INFOBLOX, IPAMDNS_TYPE_AWS, IPAMDNS_TYPE_OPENSTACK, IPAMDNS_TYPE_GCP, IPAMDNS_TYPE_INFOBLOX_DNS, IPAMDNS_TYPE_CUSTOM,
            - IPAMDNS_TYPE_CUSTOM_DNS, IPAMDNS_TYPE_AZURE, IPAMDNS_TYPE_OCI, IPAMDNS_TYPE_TENCENT, IPAMDNS_TYPE_INTERNAL, IPAMDNS_TYPE_INTERNAL_DNS,
            - IPAMDNS_TYPE_AWS_DNS, IPAMDNS_TYPE_AZURE_DNS.
            - Allowed in basic(allowed values- ipamdns_type_internal) edition, essentials(allowed values- ipamdns_type_internal) edition, enterprise edition.
        required: true
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid of the ipam/dns provider profile.
        type: str


extends_documentation_fragment:
    - avi
'''

EXAMPLES = """
  - name: Create IPAM DNS provider setting
    avi_ipamdnsproviderprofile:
      controller: '{{ controller }}'
      username: '{{ username }}'
      password: '{{ password }}'
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
      tenant_ref: /api/tenant?name=Demo
      type: IPAMDNS_TYPE_INTERNAL
"""

RETURN = '''
obj:
    description: IpamDnsProviderProfile (api/ipamdnsproviderprofile) object
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
        allocate_ip_in_vrf=dict(type='bool',),
        aws_profile=dict(type='dict',),
        azure_profile=dict(type='dict',),
        configpb_attributes=dict(type='dict',),
        custom_profile=dict(type='dict',),
        gcp_profile=dict(type='dict',),
        infoblox_profile=dict(type='dict',),
        internal_profile=dict(type='dict',),
        labels=dict(type='list',),
        markers=dict(type='list',),
        name=dict(type='str', required=True),
        oci_profile=dict(type='dict',),
        openstack_profile=dict(type='dict',),
        proxy_configuration=dict(type='dict',),
        tenant_ref=dict(type='str',),
        tencent_profile=dict(type='dict',),
        type=dict(type='str', required=True),
        url=dict(type='str',),
        uuid=dict(type='str',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk>=17.1) or requests is not installed. '
            'For more details visit https://github.com/vmware/alb-sdk.'))
    return avi_ansible_api(module, 'ipamdnsproviderprofile',
                           set())


if __name__ == '__main__':
    main()
