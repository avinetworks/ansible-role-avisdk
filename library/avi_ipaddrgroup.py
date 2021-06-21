#!/usr/bin/python
# module_check: supported

# Avi Version: 17.1.1
# Copyright 2021 VMware, Inc.  All rights reserved. VMware Confidential
# SPDX-License-Identifier: Apache License 2.0


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_ipaddrgroup
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of IpAddrGroup Avi RESTful Object
description:
    - This module is used to configure IpAddrGroup object
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
    addrs:
        description:
            - Configure ip address(es).
        type: list
    apic_epg_name:
        description:
            - Populate ip addresses from members of this cisco apic epg.
            - Field deprecated in 21.1.1.
        type: str
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 21.1.1.
        type: dict
    country_codes:
        description:
            - Populate the ip address ranges from the geo database for this country.
        type: list
    description:
        description:
            - User defined description for the object.
        type: str
    ip_ports:
        description:
            - Configure (ip address, port) tuple(s).
        type: list
    labels:
        description:
            - Key value pairs for granular object access control.
            - Also allows for classification and tagging of similar objects.
            - Field deprecated in 20.1.5.
            - Field introduced in 20.1.2.
            - Maximum of 4 items allowed.
        type: list
    marathon_app_name:
        description:
            - Populate ip addresses from tasks of this marathon app.
        type: str
    marathon_service_port:
        description:
            - Task port associated with marathon service port.
            - If marathon app has multiple service ports, this is required.
            - Else, the first task port is used.
        type: int
    markers:
        description:
            - List of labels to be used for granular rbac.
            - Field introduced in 20.1.5.
            - Allowed in basic edition, essentials edition, enterprise edition.
        type: list
    name:
        description:
            - Name of the ip address group.
        required: true
        type: str
    prefixes:
        description:
            - Configure ip address prefix(es).
        type: list
    ranges:
        description:
            - Configure ip address range(s).
        type: list
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid of the ip address group.
        type: str


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

- name: Create an IP Address Group configuration
  avi_ipaddrgroup:
    avi_credentials: "{{ avi_credentials }}"
    name: Client-Source-Block
    prefixes:
    - ip_addr:
        addr: 192.168.138.18
        type: V4
      mask: 8
    - ip_addr:
        addr: 192.168.20.11
        type: V4
      mask: 12
    - ip_addr:
        addr: 192.168.20.12
        type: V4
      mask: 16
"""

RETURN = '''
obj:
    description: IpAddrGroup (api/ipaddrgroup) object
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
        addrs=dict(type='list',),
        apic_epg_name=dict(type='str',),
        configpb_attributes=dict(type='dict',),
        country_codes=dict(type='list',),
        description=dict(type='str',),
        ip_ports=dict(type='list',),
        labels=dict(type='list',),
        marathon_app_name=dict(type='str',),
        marathon_service_port=dict(type='int',),
        markers=dict(type='list',),
        name=dict(type='str', required=True),
        prefixes=dict(type='list',),
        ranges=dict(type='list',),
        tenant_ref=dict(type='str',),
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
    return avi_ansible_api(module, 'ipaddrgroup',
                           set())


if __name__ == '__main__':
    main()
