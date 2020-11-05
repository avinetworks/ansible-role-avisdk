#!/usr/bin/python
#
# Created on Aug 25, 2016
# @author: Gaurav Rastogi (grastogi@avinetworks.com)
#          Eric Anderson (eanderson@avinetworks.com)
# module_check: supported
# Avi Version: 17.1.1
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

ANSIBLE_METADATA = {'metadata_version': '1.0',
                    'status': ['deprecated'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_alert
author: Gaurav Rastogi (grastogi@avinetworks.com)

deprecated:
    removed_in: '2.11'
    why: Removed support for this module.
    alternative: Use M(avi_api_session) instead.

short_description: Module for setup of Alert Avi RESTful Object
description:
    - This module is used to configure Alert object
    - more examples at U(https://github.com/avinetworks/devops)
requirements: [ avisdk ]
version_added: "2.3"
options:
    state:
        description:
            - The state that should be applied on the entity.
        default: present
        choices: ["absent","present"]
    action_script_output:
        description:
            - Output of the alert action script.
    alert_config_ref:
        description:
            - It is a reference to an object of type alertconfig.
        required: true
    app_events:
        description:
            - List of applicationlog.
    conn_events:
        description:
            - List of connectionlog.
    description:
        description:
            - Alert generation criteria.
    event_pages:
        description:
            - List of event pages this alert is associated with.
    events:
        description:
            - List of eventlog.
    last_throttle_timestamp:
        description:
            - Unix timestamp of the last throttling in seconds.
    level:
        description:
            - Resolved alert type.
            - Enum options - ALERT_LOW, ALERT_MEDIUM, ALERT_HIGH.
        required: true
    metric_info:
        description:
            - List of metriclog.
    name:
        description:
            - Name of the object.
        required: true
    obj_key:
        description:
            - Uuid of the resource.
        required: true
    obj_name:
        description:
            - Name of the resource.
    obj_uuid:
        description:
            - Uuid of the resource.
        required: true
    reason:
        description:
            - Reason of alert.
        required: true
    related_uuids:
        description:
            - Related uuids for the connection log.
            - Only log agent needs to fill this.
            - Server uuid should be in formatpool_uuid-ip-port.
            - In case of no port is set for server it shouldstill be operational port for the server.
    summary:
        description:
            - Summary of alert based on alert config.
        required: true
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
    threshold:
        description:
            - Number of threshold.
    throttle_count:
        description:
            - Number of times it was throttled.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
    timestamp:
        description:
            - Unix timestamp of the last throttling in seconds.
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
- name: Example to create Alert object
  avi_alert:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_alert
"""

RETURN = '''
obj:
    description: Alert (api/alert) object
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
        action_script_output=dict(type='str',),
        alert_config_ref=dict(type='str', required=True),
        app_events=dict(type='list',),
        conn_events=dict(type='list',),
        description=dict(type='str',),
        event_pages=dict(type='list',),
        events=dict(type='list',),
        last_throttle_timestamp=dict(type='float',),
        level=dict(type='str', required=True),
        metric_info=dict(type='list',),
        name=dict(type='str', required=True),
        obj_key=dict(type='str', required=True),
        obj_name=dict(type='str',),
        obj_uuid=dict(type='str', required=True),
        reason=dict(type='str', required=True),
        related_uuids=dict(type='list',),
        summary=dict(type='str', required=True),
        tenant_ref=dict(type='str',),
        threshold=dict(type='int',),
        throttle_count=dict(type='int',),
        timestamp=dict(type='float', required=True),
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
    return avi_ansible_api(module, 'alert',
                           set([]))

if __name__ == '__main__':
    main()
