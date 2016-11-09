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


EXAMPLES = '''
  - avi_analyticsprofile:
      controller: ''
      username: ''
      password: ''
      apdex_response_threshold: 500
      apdex_response_tolerated_factor: 4.0
      apdex_rtt_threshold: 250
      apdex_rtt_tolerated_factor: 4.0
      apdex_rum_threshold: 5000
      apdex_rum_tolerated_factor: 4.0
      apdex_server_response_threshold: 400
      apdex_server_response_tolerated_factor: 4.0
      apdex_server_rtt_threshold: 125
      apdex_server_rtt_tolerated_factor: 4.0
      conn_lossy_ooo_threshold: 50
      conn_lossy_timeo_rexmt_threshold: 20
      conn_lossy_total_rexmt_threshold: 50
      conn_lossy_zero_win_size_event_threshold: 2
      conn_server_lossy_ooo_threshold: 50
      conn_server_lossy_timeo_rexmt_threshold: 20
      conn_server_lossy_total_rexmt_threshold: 50
      conn_server_lossy_zero_win_size_event_threshold: 2
      disable_se_analytics: false
      disable_server_analytics: false
      exclude_client_close_before_request_as_error: false
      exclude_persistence_change_as_error: false
      exclude_server_tcp_reset_as_error: false
      exclude_syn_retransmit_as_error: false
      exclude_tcp_reset_as_error: false
      hs_event_throttle_window: 1209600
      hs_max_anomaly_penalty: 10
      hs_max_resources_penalty: 25
      hs_max_security_penalty: 100
      hs_min_dos_rate: 1000
      hs_performance_boost: 20
      hs_pscore_traffic_threshold_l4_client: 10.0
      hs_pscore_traffic_threshold_l4_server: 10.0
      hs_security_certscore_expired: 0.0
      hs_security_certscore_gt30d: 5.0
      hs_security_certscore_le07d: 2.0
      hs_security_certscore_le30d: 4.0
      hs_security_chain_invalidity_penalty: 1.0
      hs_security_cipherscore_eq000b: 0.0
      hs_security_cipherscore_ge128b: 5.0
      hs_security_cipherscore_lt128b: 3.5
      hs_security_encalgo_score_none: 0.0
      hs_security_encalgo_score_rc4: 2.5
      hs_security_hsts_penalty: 0.0
      hs_security_nonpfs_penalty: 1.0
      hs_security_selfsignedcert_penalty: 1.0
      hs_security_ssl30_score: 3.5
      hs_security_tls10_score: 5.0
      hs_security_tls11_score: 5.0
      hs_security_tls12_score: 5.0
      hs_security_weak_signature_algo_penalty: 1.0
      name: jason-analytics-profile
      tenant_ref: Demo
'''
DOCUMENTATION = '''
---
module: avi_analyticsprofile
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: AnalyticsProfile Configuration
description:
    - This module is used to configure AnalyticsProfile object
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
    apdex_response_threshold:
        description:
            - If a client receives an HTTP response in less than the Satisfactory Latency Threshold, the request is considered Satisfied.  If the response time is greater than the Satisfactory Latency Threshold but less than the Tolerated Latency Factor multiplied by the Satisfactory Latency Threshold, it is considered Tolerated.  Greater than this number and the client's request is considered Frustrated.
        default: 500
        type: integer
    apdex_response_tolerated_factor:
        description:
            - Client tolerated response latency factor. Clientmust receive a response within this factor times the satisfactory threshold (apdex_response_threshold) to be considered tolerated
        default: 4.0
        type: float
    apdex_rtt_threshold:
        description:
            - Satisfactory client to Avi Round Trip Time(RTT).
        default: 250
        type: integer
    apdex_rtt_tolerated_factor:
        description:
            - Tolerated client to Avi Round Trip Time(RTT) factor.  It is a multiple of apdex_rtt_tolerated_factor.
        default: 4.0
        type: float
    apdex_rum_threshold:
        description:
            - If a client is able to load a page in less than the Satisfactory Latency Threshold, the PageLoad is considered Satisfied.  If the load time is greater than the Satisfied Latency but less than the Tolerated Latency multiplied by Satisifed Latency, it is considered Tolerated.  Greater than this number and the client's request is considered Frustrated.  A PageLoad includes the time for DNS lookup, download of all HTTP objects, and page render time.
        default: 5000
        type: integer
    apdex_rum_tolerated_factor:
        description:
            - Virtual service threshold factor for tolerated Page Load Time (PLT) as multiple of apdex_rum_threshold.
        default: 4.0
        type: float
    apdex_server_response_threshold:
        description:
            - If Avi receives an HTTP response from a server in less than the Satisfactory Latency Threshold, the server response is considered Satisfied.  If the response time is greater than the Satisfactory Latency Threshold but less than the Tolerated Latency Factor multiplied by the Satisfactory Latency Threshold, it is considered Tolerated.  Greater than this number and the server response is considered Frustrated.
        default: 400
        type: integer
    apdex_server_response_tolerated_factor:
        description:
            - Server tolerated response latency factor. Servermust response within this factor times the satisfactory threshold (apdex_server_response_threshold) to be considered tolerated
        default: 4.0
        type: float
    apdex_server_rtt_threshold:
        description:
            - Satisfactory client to Avi Round Trip Time(RTT).
        default: 125
        type: integer
    apdex_server_rtt_tolerated_factor:
        description:
            - Tolerated client to Avi Round Trip Time(RTT) factor.  It is a multiple of apdex_rtt_tolerated_factor.
        default: 4.0
        type: float
    client_log_config:
        description:
            - Not present.
        type: ClientLogConfiguration
    conn_lossy_ooo_threshold:
        description:
            - A connection between client and Avi is considered lossy when more than this percentage of out of order packets are received.
        default: 50
        type: integer
    conn_lossy_timeo_rexmt_threshold:
        description:
            - A connection between client and Avi is considered lossy when more than this percentage of packets are retransmitted due to timeout.
        default: 20
        type: integer
    conn_lossy_total_rexmt_threshold:
        description:
            - A connection between client and Avi is considered lossy when more than this percentage of packets are retransmitted.
        default: 50
        type: integer
    conn_lossy_zero_win_size_event_threshold:
        description:
            - A connection between client and Avi is considered lossy when more than this percentage of times a packet could not be trasmitted due to zero window.
        default: 2
        type: integer
    conn_server_lossy_ooo_threshold:
        description:
            - A connection between Avi and server is considered lossy when more than this percentage of out of order packets are received.
        default: 50
        type: integer
    conn_server_lossy_timeo_rexmt_threshold:
        description:
            - A connection between Avi and server is considered lossy when more than this percentage of packets are retransmitted due to timeout.
        default: 20
        type: integer
    conn_server_lossy_total_rexmt_threshold:
        description:
            - A connection between Avi and server is considered lossy when more than this percentage of packets are retransmitted.
        default: 50
        type: integer
    conn_server_lossy_zero_win_size_event_threshold:
        description:
            - A connection between Avi and server is considered lossy when more than this percentage of times a packet could not be trasmitted due to zero window.
        default: 2
        type: integer
    description:
        description:
            - Not present.
        type: string
    disable_se_analytics:
        description:
            - Disable node (service engine) level analytics forvs metrics
        default: False
        type: bool
    disable_server_analytics:
        description:
            - Disable analytics on backend servers. This may be desired in container environment when there are large number of  ephemeral servers
        default: False
        type: bool
    exclude_client_close_before_request_as_error:
        description:
            - Exclude client closed connection before an HTTP request could be completed from being classified as an error.
        default: False
        type: bool
    exclude_gs_down_as_error:
        description:
            - Exclude queries to GSLB services that are operationally down from the list of errors.
        default: False
        type: bool
    exclude_http_error_codes:
        description:
            - List of HTTP status codes to be excluded from being classified as an error.  Error connections or responses impacts health score, are included as significant logs, and may be classified as part of a DoS attack.
        type: integer
    exclude_invalid_dns_domain_as_error:
        description:
            - Exclude dns queries to domains outside the domains configured in the DNS application profile from the list of errors.
        default: False
        type: bool
    exclude_invalid_dns_query_as_error:
        description:
            - Exclude invalid dns queries from the list of errors.
        default: False
        type: bool
    exclude_no_dns_record_as_error:
        description:
            - Exclude queries to domains that did not have configured services/records from the list of errors.
        default: False
        type: bool
    exclude_no_valid_gs_member_as_error:
        description:
            - Exclude queries to GSLB services that have no available members from the list of errors.
        default: False
        type: bool
    exclude_persistence_change_as_error:
        description:
            - Exclude persistence server changed while load balancing' from the list of errors.
        default: False
        type: bool
    exclude_server_dns_error_as_error:
        description:
            - Exclude server dns error response from the list of errors.
        default: False
        type: bool
    exclude_server_tcp_reset_as_error:
        description:
            - Exclude server TCP reset from errors.  It is common for applications like MS Exchange.
        default: False
        type: bool
    exclude_syn_retransmit_as_error:
        description:
            - Exclude 'server unanswered syns' from the list of errors.
        default: False
        type: bool
    exclude_tcp_reset_as_error:
        description:
            - Exclude TCP resets by client from the list of potential errors.
        default: False
        type: bool
    exclude_unsupported_dns_query_as_error:
        description:
            - Exclude unsupported dns queries from the list of errors.
        default: False
        type: bool
    hs_event_throttle_window:
        description:
            - Time window (in secs) within which only unique health change events should occur
        default: 1209600
        type: integer
    hs_max_anomaly_penalty:
        description:
            - Maximum penalty that may be deducted from health score for anomalies.
        default: 10
        type: integer
    hs_max_resources_penalty:
        description:
            - Maximum penalty that may be deducted from health score for high resource utilization.
        default: 25
        type: integer
    hs_max_security_penalty:
        description:
            - Maximum penalty that may be deducted from health score based on security assessment.
        default: 100
        type: integer
    hs_min_dos_rate:
        description:
            - DoS connection rate below which the DoS security assessment will not kick in.
        default: 1000
        type: integer
    hs_performance_boost:
        description:
            - Adds free performance score credits to health score. It can be used for compensating health score for known slow applications.
        default: 0
        type: integer
    hs_pscore_traffic_threshold_l4_client:
        description:
            - Threshold number of connections in 5min, below which apdexr, apdexc, rum_apdex, and other network quality metrics are not computed.
        default: 10.0
        type: float
    hs_pscore_traffic_threshold_l4_server:
        description:
            - Threshold number of connections in 5min, below which apdexr, apdexc, rum_apdex, and other network quality metrics are not computed.
        default: 10.0
        type: float
    hs_security_certscore_expired:
        description:
            - Score assigned when the certificate has expired
        default: 0.0
        type: float
    hs_security_certscore_gt30d:
        description:
            - Score assigned when the certificate expires in more than 30 days
        default: 5.0
        type: float
    hs_security_certscore_le07d:
        description:
            - Score assigned when the certificate expires in less than or equal to 7 days
        default: 2.0
        type: float
    hs_security_certscore_le30d:
        description:
            - Score assigned when the certificate expires in less than or equal to 30 days
        default: 4.0
        type: float
    hs_security_chain_invalidity_penalty:
        description:
            - Penalty for allowing certificates with invalid chain.
        default: 1.0
        type: float
    hs_security_cipherscore_eq000b:
        description:
            - Score assigned when the minimum cipher strength is 0 bits
        default: 0.0
        type: float
    hs_security_cipherscore_ge128b:
        description:
            - Score assigned when the minimum cipher strength is greater than equal to 128 bits
        default: 5.0
        type: float
    hs_security_cipherscore_lt128b:
        description:
            - Score assigned when the minimum cipher strength is less than 128 bits
        default: 3.5
        type: float
    hs_security_encalgo_score_none:
        description:
            - Score assigned when no algorithm is used for encryption.
        default: 0.0
        type: float
    hs_security_encalgo_score_rc4:
        description:
            - Score assigned when RC4 algorithm is used for encryption.
        default: 2.5
        type: float
    hs_security_hsts_penalty:
        description:
            - Penalty for not enabling HSTS.
        default: 1.0
        type: float
    hs_security_nonpfs_penalty:
        description:
            - Penalty for allowing non-PFS handshakes.
        default: 1.0
        type: float
    hs_security_selfsignedcert_penalty:
        description:
            - Deprecated
        default: 1.0
        type: float
    hs_security_ssl30_score:
        description:
            - Score assigned when supporting SSL3.0 encryption protocol
        default: 3.5
        type: float
    hs_security_tls10_score:
        description:
            - Score assigned when supporting TLS1.0 encryption protocol
        default: 5.0
        type: float
    hs_security_tls11_score:
        description:
            - Score assigned when supporting TLS1.1 encryption protocol
        default: 5.0
        type: float
    hs_security_tls12_score:
        description:
            - Score assigned when supporting TLS1.2 encryption protocol
        default: 5.0
        type: float
    hs_security_weak_signature_algo_penalty:
        description:
            - Penalty for allowing weak signature algorithm(s).
        default: 1.0
        type: float
    name:
        description:
            - The name of the analytics profile.
        required: true
        type: string
    ranges:
        description:
            - List of HTTP status code ranges to be excluded from being classified as an error.
        type: HTTPStatusRange
    resp_code_block:
        description:
            - Block of HTTP response codes to be excluded from being classified as an error.
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
            - UUID of the analytics profile.
        type: string
'''

RETURN = '''
obj:
    description: AnalyticsProfile (api/analyticsprofile) object
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
                apdex_response_threshold=dict(
                    type='int',
                    ),
                apdex_response_tolerated_factor=dict(
                    type='float',
                    ),
                apdex_rtt_threshold=dict(
                    type='int',
                    ),
                apdex_rtt_tolerated_factor=dict(
                    type='float',
                    ),
                apdex_rum_threshold=dict(
                    type='int',
                    ),
                apdex_rum_tolerated_factor=dict(
                    type='float',
                    ),
                apdex_server_response_threshold=dict(
                    type='int',
                    ),
                apdex_server_response_tolerated_factor=dict(
                    type='float',
                    ),
                apdex_server_rtt_threshold=dict(
                    type='int',
                    ),
                apdex_server_rtt_tolerated_factor=dict(
                    type='float',
                    ),
                client_log_config=dict(
                    type='dict',
                    ),
                conn_lossy_ooo_threshold=dict(
                    type='int',
                    ),
                conn_lossy_timeo_rexmt_threshold=dict(
                    type='int',
                    ),
                conn_lossy_total_rexmt_threshold=dict(
                    type='int',
                    ),
                conn_lossy_zero_win_size_event_threshold=dict(
                    type='int',
                    ),
                conn_server_lossy_ooo_threshold=dict(
                    type='int',
                    ),
                conn_server_lossy_timeo_rexmt_threshold=dict(
                    type='int',
                    ),
                conn_server_lossy_total_rexmt_threshold=dict(
                    type='int',
                    ),
                conn_server_lossy_zero_win_size_event_threshold=dict(
                    type='int',
                    ),
                description=dict(
                    type='str',
                    ),
                disable_se_analytics=dict(
                    type='bool',
                    ),
                disable_server_analytics=dict(
                    type='bool',
                    ),
                exclude_client_close_before_request_as_error=dict(
                    type='bool',
                    ),
                exclude_gs_down_as_error=dict(
                    type='bool',
                    ),
                exclude_http_error_codes=dict(
                    type='list',
                    ),
                exclude_invalid_dns_domain_as_error=dict(
                    type='bool',
                    ),
                exclude_invalid_dns_query_as_error=dict(
                    type='bool',
                    ),
                exclude_no_dns_record_as_error=dict(
                    type='bool',
                    ),
                exclude_no_valid_gs_member_as_error=dict(
                    type='bool',
                    ),
                exclude_persistence_change_as_error=dict(
                    type='bool',
                    ),
                exclude_server_dns_error_as_error=dict(
                    type='bool',
                    ),
                exclude_server_tcp_reset_as_error=dict(
                    type='bool',
                    ),
                exclude_syn_retransmit_as_error=dict(
                    type='bool',
                    ),
                exclude_tcp_reset_as_error=dict(
                    type='bool',
                    ),
                exclude_unsupported_dns_query_as_error=dict(
                    type='bool',
                    ),
                hs_event_throttle_window=dict(
                    type='int',
                    ),
                hs_max_anomaly_penalty=dict(
                    type='int',
                    ),
                hs_max_resources_penalty=dict(
                    type='int',
                    ),
                hs_max_security_penalty=dict(
                    type='int',
                    ),
                hs_min_dos_rate=dict(
                    type='int',
                    ),
                hs_performance_boost=dict(
                    type='int',
                    ),
                hs_pscore_traffic_threshold_l4_client=dict(
                    type='float',
                    ),
                hs_pscore_traffic_threshold_l4_server=dict(
                    type='float',
                    ),
                hs_security_certscore_expired=dict(
                    type='float',
                    ),
                hs_security_certscore_gt30d=dict(
                    type='float',
                    ),
                hs_security_certscore_le07d=dict(
                    type='float',
                    ),
                hs_security_certscore_le30d=dict(
                    type='float',
                    ),
                hs_security_chain_invalidity_penalty=dict(
                    type='float',
                    ),
                hs_security_cipherscore_eq000b=dict(
                    type='float',
                    ),
                hs_security_cipherscore_ge128b=dict(
                    type='float',
                    ),
                hs_security_cipherscore_lt128b=dict(
                    type='float',
                    ),
                hs_security_encalgo_score_none=dict(
                    type='float',
                    ),
                hs_security_encalgo_score_rc4=dict(
                    type='float',
                    ),
                hs_security_hsts_penalty=dict(
                    type='float',
                    ),
                hs_security_nonpfs_penalty=dict(
                    type='float',
                    ),
                hs_security_selfsignedcert_penalty=dict(
                    type='float',
                    ),
                hs_security_ssl30_score=dict(
                    type='float',
                    ),
                hs_security_tls10_score=dict(
                    type='float',
                    ),
                hs_security_tls11_score=dict(
                    type='float',
                    ),
                hs_security_tls12_score=dict(
                    type='float',
                    ),
                hs_security_weak_signature_algo_penalty=dict(
                    type='float',
                    ),
                name=dict(
                    type='str',
                    ),
                ranges=dict(
                    type='list',
                    ),
                resp_code_block=dict(
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
                ),
        )
        return avi_ansible_api(module, 'analyticsprofile',
                               set([]))
    except:
        raise


if __name__ == '__main__':
    main()