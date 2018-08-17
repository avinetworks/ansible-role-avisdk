
HealthMonitor = {
        "https_monitor":
            {
              "http_request": "HEAD / HTTP/1.0",
              "http_response_code" :["HTTP_2XX", "HTTP_3XX"]
            },
        "receive_timeout": 4,
        "failed_checks": 3,
        "send_interval": 10,
        "successful_checks": 3,
        "type": "HEALTH_MONITOR_HTTPS",
        "name": "MyWebsite-HTTPS"
    }

VirtualService = {
        "name": "rtb-facebook_outside_p80",
        "enabled": "False",
        "vip": [
            {
                "ip_address": {
                    "type": "V4",
                    "addr": "172.82.206.52"
                },
                "vip_id": 0
            }
        ],
        "services": [
            {
                "enable_ssl": "False",
                "port": "80"
            }
        ],
        "type": "VS_TYPE_NORMAL",
    }

Tenant = {
        "name": "admin",
}


Pool = {
            "lb_algorithm": "LB_ALGORITHM_LEAST_CONNECTIONS",
            "name": "storage1ed1svc1.cs.qai-8080-pool",
            "tenant_ref": "/api/tenant/?name=admin",
            "servers": [
                {
                    "ip": {
                        "type": "V4",
                        "addr": "10.229.68.71"
                    },
                    "hostname": "storage1ed1svc1.cs.qai",
                    "enabled": "True",
                    "port": "8080"
                }
            ],
            "health_monitor_refs": []
        }

VsVip = {
            "east_west_placement": "False",
            "tenant_ref": "/api/tenant/?name=admin",
            "vip": [
                {
                    "vip_id": "1",
                    "avi_allocated_fip": "False",
                    "auto_allocate_ip": "False",
                    "enabled": "True",
                    "auto_allocate_floating_ip": "False",
                    "avi_allocated_vip": "False",
                    "auto_allocate_ip_type": "V4_ONLY",
                    "ip_address": {
                        "type": "V4",
                        "addr": "10.10.2.13"
                    }
                }
            ],
            "name": "vsvip-Test-vs-Default-Cloud"
    }

UserAccountProfile = {
            "max_concurrent_sessions": 0,
            "uuid": "useraccountprofile-bc7cfe8e-a74c-4a9e-978b-8c5a9f2e54e3",
            "name": "Default-User-Account-Profile",
            "url": "/api/useraccountprofile/useraccountprofile-bc7cfe8e-a74c-4a9e-978b-8c5a9f2e54e3",
            "account_lock_timeout": 30,
            "max_login_failure_count": 20,
            "max_password_history_count": 0,
            "credentials_timeout_threshold": 0
    }

WafPolicy = {
            "waf_profile_ref": "/api/wafprofile/?name=System-WAF-Profile",
            "tenant_ref": "/api/tenant/?name=admin",
            "mode": "WAF_MODE_DETECTION_ONLY",
            "paranoia_level": "WAF_PARANOIA_LEVEL_LOW",
            "name": "System-WAF-Policy"
        }

Applicationpersisteceprofile = {
            "name": "Test-persistance-profile",
            "persistence_type": "PERSISTENCE_TYPE_CLIENT_IP_ADDRESS",
            "ip_persistence_profile": {
                "ip_persistent_timeout": 24
			},
			"tenant_ref": "/api/tenant/?name=admin",
			"server_hm_down_recovery": "HM_DOWN_PICK_NEW_SERVER"
		}

ApplicationProfile = {
			"name": "test-applicationprofile",
			"http_profile": {
				"websockets_enabled": True,
				"x_forwarded_proto_enabled": False,
				"xff_alternate_name": "X-Forwarded-For",
				"xff_enabled": True
			},
			"type": "APPLICATION_PROFILE_TYPE_HTTP"
    }

Networkprofile = {
			"name": "NDS-TCP-PROFILE",
			"profile": {
				"tcp_proxy_profile": {
					"max_segment_size": 0,
					"receive_window": 3662,
					"nagles_algorithm": False,
					"use_interface_mtu": False,
					"automatic": False
				},
				"type": "PROTOCOL_TYPE_TCP_PROXY"
			},
			"tenant_ref": "/api/tenant/?name=admin"
    }



SslProfile = {
			"name": "Test-ssl_profile-cEE",
			"accepted_ciphers": "DHE-DSS-AES256-SHA:AES256-SHA:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA:AES128-SHA:DHE-RSA-AES256-SHA",
			"tenant_ref": "/api/tenant/?name=admin",
			"accepted_versions": [
				{
					"type": "SSL_VERSION_TLS1"
				},
				{
					"type": "SSL_VERSION_TLS1_1"
				},
				{
					"type": "SSL_VERSION_TLS1_2"
				}
			],
			"enable_ssl_session_reuse": False
    }


HttpPolicySet = {
			"http_request_policy": {
				"rules": [
					{
						"index": 0,
						"match": {
							"path": {
								"match_case": "INSENSITIVE",
								"match_criteria": "EQUALS",
								"match_str": [
									"/"
								]
							}
						},
						"name": "mysitestg-43000-redirect-policy-rule-0",
						"redirect_action": {
							"host": {
								"tokens": [
									{
										"end_index": "65535",
										"start_index": "0",
										"str_value": "mysitestg.qualcomm.com",
										"type": "URI_TOKEN_TYPE_STRING"
									}
								],
								"type": "URI_PARAM_TYPE_TOKENIZED"
							},
							"protocol": "HTTP"
						}
					}
				]
			},
			"name": "mysitestg-43000-redirect-policy",
			"tenant_ref": "/api/tenant/?name=admin"
    }

BackupConfiguration = {
			"name": "Backup-Configuration",
			"tenant_ref": "/api/tenant?name=admin",
			"save_local": True,
			"maximum_backups_stored": 3
    }


Role = {
			"name": "Test-role",
			"tenant_ref": "/api/tenant?name=admin",
			"privileges": [
				{
					"type": "READ_ACCESS",
					"resource": "PERMISSION_VIRTUALSERVICE"
				},
				{
					"type": "READ_ACCESS",
					"resource": "PERMISSION_POOL"
				},
				{
					"type": "READ_ACCESS",
					"resource": "PERMISSION_POOLGROUP"
				},
				{
					"type": "READ_ACCESS",
					"resource": "PERMISSION_HTTPPOLICYSET"
				}
			]
    }


Scheduler = {
			"name": "Default-Scheduler",
			"frequency_unit": "SCHEDULER_FREQUENCY_UNIT_MONTH",
			"run_mode": "RUN_MODE_PERIODIC",
			"backup_config_ref": "/api/backupconfiguration?name=Backup-Configuration",
			"frequency": 3,
			"scheduler_action": "SCHEDULER_ACTION_BACKUP"
    }


Prioritylabels = {
			"name": "test-proritylabel",
			"tenant_ref": "/api/tenant?name=admin",
			"description": "desc"
    }


Prioritylabels = {
			"name": "test-proritylabel",
			"tenant_ref": "/api/tenant?name=admin",
			"description": "desc"
    }

Cloud = {
			"name": "Test-Vcenter-Cloud",
			"tenant_ref": "/api/tenant?name=admin",
			"dhcp_enabled": True,
			"enable_vip_static_routes": False,
			"license_type": "LIC_CORES",
			"mtu": 1500,
			"prefer_static_routes": False,
			"vcenter_configuration": {
				"datacenter": "Demo-DC",
				"management_network": "api/vimgrnwruntime/dvportgroup-102-10.128.2.190",
				"password": "vmware",
				"privilege": "WRITE_ACCESS",
				"username": "root",
				"vcenter_url": "10.128.2.190"
			},
			"vtype": "CLOUD_VCENTER"
    }


Vrfcontext = {
			"name": "test-vrf-context",
			"url": "/api/vrfcontext/vrfcontext-f54f6d8a-d2c9-4bc9-a0b8-cfaed295aff6",
			"tenant_ref": "/api/tenant?name=admin",
			"system_default": False
    }

Gslbservice = {
	"controller_health_status_enabled": True,
	"wildcard_match": False,
	"down_response": {
		"type": "GSLB_SERVICE_DOWN_RESPONSE_NONE"
	},
	"enabled": True,
	"domain_names": [
		"test-application.com"
	],
	"is_federated": True,
	"use_edns_client_subnet": True,
	"groups": [{
		"priority": 10,
		"members": [{
			"public_ip": {
				"ip": {
					"type": "V4",
					"addr": "10.10.2.4"
				}
			},
			"ip": {
				"type": "V4",
				"addr": "10.10.0.3"
			},
			"ratio": 1,
			"location": {
				"source": "GSLB_LOCATION_SRC_FROM_GEODB"
			},
			"enabled": True
		}],
		"name": "gslb-pool",
		"algorithm": "GSLB_ALGORITHM_ROUND_ROBIN"
	}],
	"site_persistence_enabled": False,
	"min_members": 0,
	"health_monitor_scope": "GSLB_SERVICE_HEALTH_MONITOR_ALL_MEMBERS",
	"pool_algorithm": "GSLB_SERVICE_ALGORITHM_PRIORITY",
	"name": "Test-gslb"
}

Useraccountprofile = {
			"name": "Test-Default-User-Account-Profile",
			"max_concurrent_sessions": 0,
			"account_lock_timeout": 60,
			"max_login_failure_count": 20,
			"max_password_history_count": 0,
			"credentials_timeout_threshold": 0
    }

VsDataScriptSet = {
			"name": "Test-datascript",
			"description": "Desc"
    }


StringGroup = {
			"name": "Test-System-Compressible-Content-Types",
			"kv": [
				{
					"key": "text/html"
				},
				{
					"key": "text/xml"
				},
				{
					"key": "text/plain"
				},
				{
					"key": "text/css"
				},
				{
					"key": "text/javascript"
				},
				{
					"key": "application/javascript"
				},
				{
					"key": "application/x-javascript"
				},
				{
					"key": "application/xml"
				},
				{
					"key": "application/pdf"
				}
			],
			"tenant_ref": "/api/tenant?name=admin",
			"type": "SG_TYPE_STRING"
    }


HardwareSecurityModuleGroup = {
			"hsm": {
				"nethsm": [
					{
						"esn": "123",
						"keyhash": "abc",
						"module_id": 0,
						"priority": 100,
						"remote_ip": {
							"addr": "1.2.3.4",
							"type": "V4"
						},
						"remote_port": 9004
					}
				],
				"rfs": {
					"ip": {
						"addr": "1.2.3.4",
						"type": "V4"
					},
					"port": 9004
				},
				"type": "HSM_TYPE_THALES_NETHSM"
			},
			"name": "test",
			"tenant_ref": "/api/tenant?name=admin"
    }


Wafprofile = {
			"name": "Test-WAF-Profile",
			"tenant_ref": "/api/tenant/?name=admin",
			"config": {
				"client_nonfile_upload_max_body_size": 128,
				"regex_match_limit": 1500,
				"allowed_request_content_types": [
					"application/x-www-form-urlencoded",
					"multipart/form-data",
					"text/xml",
					"application/xml",
					"application/x-amf",
					"application/json"
				],
				"allowed_methods": [
					"HTTP_METHOD_GET",
					"HTTP_METHOD_HEAD",
					"HTTP_METHOD_POST",
					"HTTP_METHOD_OPTIONS"
				],
				"response_hdr_default_action": "phase:3,deny,status:403,log,auditlog",
				"allowed_http_versions": [
					"ONE_ZERO",
					"ONE_ONE"
				],
				"request_body_default_action": "phase:2,deny,status:403,log,auditlog",
				"response_body_default_action": "phase:4,deny,status:403,log,auditlog",
				"request_hdr_default_action": "phase:1,deny,status:403,log,auditlog",
				"static_extensions": [
					".gif",
					".jpg",
					".jpeg",
					".png",
					".js",
					".css",
					".ico",
					".svg",
					".webp"
				],
				"buffer_response_body_for_inspection": False,
				"restricted_extensions": [
					".asa",
					".asax",
					".ascx"
				],
				"client_file_upload_max_body_size": 1024,
				"cookie_format_version": 0,
				"restricted_headers": [
					"Proxy-Connection",
					"Lock-Token",
					"Content-Range",
					"Translate",
					"via",
					"if"
				],
				"server_response_max_body_size": 128,
				"argument_separator": "&"
			}
    }


Wafpolicy = {
			"name": "Test-WAF-Policy",
			"tenant_ref": "/api/tenant?name=admin",
			"mode": "WAF_MODE_DETECTION_ONLY",
			"paranoia_level": "WAF_PARANOIA_LEVEL_LOW",
			"waf_profile_ref": "/api/wafprofile?name=Test-WAF-Profile"
    }

Ipaddrgroup = {
			"name": "New-Internal",
			"prefixes": [
				{
					"ip_addr": {
						"addr": "10.0.0.0",
						"type": "V4"
					},
					"mask": 8
				},
				{
					"ip_addr": {
						"addr": "192.168.0.10",
						"type": "V4"
					},
					"mask": 16
				},
				{
					"ip_addr": {
						"addr": "172.16.0.1",
						"type": "V4"
					},
					"mask": 14
				}
			],
			"tenant_ref": "/api/tenant/?name=admin"
    }


Ipamdnsproviderprofile = {
			"name": "test",
			"tenant_ref": "/api/tenant?name=admin",
			"internal_profile": {
				"dns_service_domain": [
					{
						"record_ttl": 150,
						"num_dns_ip": 1,
						"domain_name": "rohan",
						"pass_through": True
					}
				]
			},
			"type": "IPAMDNS_TYPE_INTERNAL_DNS"
    }


Webhook = {
			"name": "Test-webhook",
			"tenant_ref": "/api/tenant?name=admin",
			"description": "desc"
    }


MicroserviceGroup = {
			"name": "vs-marketing",
			"description": "Group created by my Secure My App UI.",
			"tenant_ref": "/api/tenant?name=admin"
    }


ActionGroupConfig = {
			"name": "Test-Syslog-Config",
			"tenant_ref": "/api/tenant/?name=admin",
			"level": "ALERT_HIGH",
			"autoscale_trigger_notification": False,
			"external_only": True
    }


AlertConfig = {
			"name": "Test-System-SSL-Alert",
			"enabled": True,
			"tenant_ref": "/api/tenant/?name=admin",
			"category": "REALTIME",
			"expiry_time": 86400,
			"summary": "System-SSL-Alert System Alert Triggered",
			"rolling_window": 300,
			"source": "EVENT_LOGS",
			"alert_rule": {
				"operator": "OPERATOR_OR",
				"sys_event_rule": [
					{
						"event_id": "SSL_CERT_EXPIRE",
						"not_cond": False
					},
					{
						"event_id": "SSL_CERT_RENEW",
						"not_cond": False
					},
					{
						"event_id": "SSL_CERT_RENEW_FAILED",
						"not_cond": False
					}
				]
			},
			"threshold": 1,
			"throttle": 0,
			"action_group_ref": "/api/actiongroupconfig/?name=System-Alert-Level-Medium"
    }


AlertEmailConfig = {
			"name": "test-email",
			"tenant_ref": "/api/tenant/?name=admin",
			"to_emails": "abc.pqx@gmail.com",
			"cc_emails": "avi.123@gmail.com"
    }

Network = {
			"name": "test-network",
			"synced_from_se": False,
			"tenant_ref": "/api/tenant?name=admin",
			"exclude_discovered_subnets": True,
			"dhcp_enabled": True
    }

NetworkSecurityPolicy = {
			"name": "Test-network-policy",
			"tenant_ref": "/api/tenant?name=admin"
    }

AlertScriptConfig = {
			"name": "test",
			"tenant_ref": "/api/tenant?name=admin",
			"action_script": "echo \"avi networks\""
    }

AlertSyslogConfig = {
			"name": "test",
			"tenant_ref": "/api/tenant/?name=admin",
			"syslog_servers": [
				{
					"udp": True,
					"syslog_server_port": 443,
					"syslog_server": "10.10.3.10"
				}
			]
    }


PkiProfile = {
			"name": "test-pkiprofile",
			"tenant_ref": "/api/tenant?name=admin",
			"is_federated": True,
			"ignore_peer_chain": False,
			"crl_check": True
    }

AnalyticsProfile = {
			"name": "Test-System-Analytics-Profile",
			"tenant_ref": "/api/tenant/?name=admin",
			"hs_event_throttle_window": 1209600,
			"description": "Test System Analytics Profile",
			"apdex_response_threshold": 500,
			"disable_se_analytics": False,
			"apdex_server_rtt_tolerated_factor": 4,
			"hs_security_nonpfs_penalty": 1,
			"hs_security_tls12_score": 5,
			"exclude_server_tcp_reset_as_error": False,
			"hs_min_dos_rate": 1000,
			"exclude_no_dns_record_as_error": False,
			"conn_server_lossy_zero_win_size_event_threshold": 2,
			"hs_max_resources_penalty": 25,
			"conn_lossy_total_rexmt_threshold": 50,
			"hs_pscore_traffic_threshold_l4_client": 10,
			"exclude_no_valid_gs_member_as_error": False,
			"apdex_server_response_threshold": 400,
			"hs_security_cipherscore_ge128b": 5,
			"hs_performance_boost": 0,
			"exclude_invalid_dns_domain_as_error": False,
			"exclude_http_error_codes": [
				475
			],
			"hs_max_anomaly_penalty": 10,
			"hs_security_tls11_score": 5,
			"exclude_gs_down_as_error": False,
			"apdex_server_response_tolerated_factor": 4,
			"disable_server_analytics": False,
			"conn_server_lossy_timeo_rexmt_threshold": 20,
			"exclude_client_close_before_request_as_error": True,
			"hs_security_weak_signature_algo_penalty": 1,
			"exclude_persistence_change_as_error": False,
			"hs_security_selfsignedcert_penalty": 1,
			"conn_server_lossy_total_rexmt_threshold": 50,
			"conn_lossy_timeo_rexmt_threshold": 20,
			"conn_lossy_ooo_threshold": 50,
			"apdex_rtt_tolerated_factor": 4,
			"hs_security_certscore_gt30d": 5,
			"hs_security_ssl30_score": 3.5,
			"conn_server_lossy_ooo_threshold": 50,
			"apdex_rum_tolerated_factor": 4,
			"hs_security_cipherscore_eq000b": 0,
			"hs_security_certscore_le30d": 4,
			"hs_pscore_traffic_threshold_l4_server": 10,
			"exclude_syn_retransmit_as_error": False,
			"apdex_server_rtt_threshold": 125,
			"hs_security_hsts_penalty": 1,
			"exclude_server_dns_error_as_error": False,
			"hs_security_certscore_le07d": 2,
			"conn_lossy_zero_win_size_event_threshold": 2,
			"hs_security_encalgo_score_rc4": 2.5,
			"hs_max_security_penalty": 100,
			"exclude_tcp_reset_as_error": False,
			"hs_security_encalgo_score_none": 0,
			"apdex_response_tolerated_factor": 4,
			"client_log_config": {
				"enable_significant_log_collection": True,
				"significant_log_processing": "LOGS_PROCESSING_SYNC_AND_INDEX_ON_DEMAND",
				"non_significant_log_processing": "LOGS_PROCESSING_SYNC_AND_INDEX_ON_DEMAND",
				"filtered_log_processing": "LOGS_PROCESSING_SYNC_AND_INDEX_ON_DEMAND"
			},
			"hs_security_chain_invalidity_penalty": 1,
			"exclude_invalid_dns_query_as_error": False,
			"apdex_rum_threshold": 5000,
			"hs_security_cipherscore_lt128b": 3.5,
			"hs_security_tls10_score": 5,
			"hs_security_certscore_expired": 0,
			"apdex_rtt_threshold": 250,
			"exclude_unsupported_dns_query_as_error": False
    }



PoolGroupDeploymentPolicy = {
			"name": "test-policy",
			"target_test_traffic_ratio": 2,
			"test_traffic_ratio_rampup": 3,
			"evaluation_duration": 7599
    }

AuthProfile = {
			"name": "Test-AuthProfile",
			"http": {
				"cache_expiration_time": 5,
				"group_member_is_full_dn": False
			},
			"ldap": {
				"base_dn": "dc=avi,dc=local",
				"bind_as_administrator": True,
				"port": 389,
				"security_mode": "AUTH_LDAP_SECURE_NONE",
				"server": [
					"10.10.0.100"
				],
				"settings": {
					"admin_bind_dn": "user@avi.local",
					"group_filter": "(objectClass=*)",
					"group_member_attribute": "member",
					"group_member_is_full_dn": True,
					"group_search_dn": "dc=avi,dc=local",
					"group_search_scope": "AUTH_LDAP_SCOPE_SUBTREE",
					"ignore_referrals": True,
					"password": "{{ avi_credentials.password }}",
					"user_id_attribute": "samAccountname",
					"user_search_dn": "dc=avi,dc=local",
					"user_search_scope": "AUTH_LDAP_SCOPE_ONE"
				}
			},
			"tenant_ref": "/api/tenant?name=admin",
			"type": "AUTH_PROFILE_LDAP"
    }


AutoScaleLaunchConfig = {
			"name": "Test-autoscalelaunchconfig",
			"tenant_ref": "/api/tenant?name=admin",
			"image_id": "default",
			"use_external_asg": True
    }

CloudConnecTorUser = {
			"name": "Test-User",
			"tenant_ref": "/api/tenant?name=admin",
			"private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDA7Lri81+WxnMx\nzg+b8Mw3tH6ls0WIdT90cZlgnb/0YBDzeft2etemC50cHVbqLYZ+UkYMQJjk0Zk9\nF1ANPcY6KhRM0oDh1tb2YdemO19lqy/pXub46rrFI4EutgvG4hMgQm6uBBOEZTxl\nntGzUeh6pLQpUcPvcjCKjDn0j/SMtjMo6q5/q+af0X4+CoASE84mv+VLWnhlF5gr\nZyW7OfkcPUqRcGnt/VplGJHvugcoNmrEuKi8fzK0WRsEYUwAWgQ3DDMuJSgrPSRc\nWanOV5BES8Wtv0CnicXa8wo05Rfnof1p6oOdhjAgN5OhD6Keq98UpgNkSDvZgW5R\nGJpeYqhrAgMBAAECggEBAKhhNQ+FWEVw+PNcJJV2ydZIi0y1tZdOtc48o6AGrpVs\nDv9h1I5o0rRSaJI0LTp/92VjC04ARzFWmgcOxMh5xPvY5BTUmLYDW2R4qs2j/jPv\nAAcP1EkmHVKYFVSegJLZl9XNBWqNljc0YE1VGzMF5wC7pZ52hasDn8gccSy5Q7hW\ne9Kiek3C02vDdlCEs5EK0O7+KBZb75YsOSEjaoDJGAPH3Iw3Y8FTDChpA5zv94PC\nY4XFxmxZ5hj3WJoKcf0MYTbUP31sjnWYPfckr8F6xic/AHO8e009bjRCSLeOrut7\n3pC1F+8ekuvdTtiQKMYWjZDKOIx65ClJP+8nC/VXG1ECgYEA8nxUSl2f3JOB/RmM\nuEXgmeY0iQqXmOH1WesRofCNXQA4ENzwl5ADrZ+rFJ9B9fjkT5+Q+QP7CClW6AhC\neBtHDxr6rUcZsKrZdZJrdOk6Wxw8+Ql3wGnd81frrhTSOStUm5X5ztBVtvdfDPhj\nmcJpRIbUtb8XZJWRMfz6gtxZIFkCgYEAy61J7iMbbzv+gTEd719A0ITGSAQ3FRWw\nL4Co0PtEhq0lmJHRcYVTX20fj2n0eTL23FRPAz1K48+pj9DpqXIsuzU0sgUe4erQ\n6pJ5kFy0TRisqgh2JBpYsMNAX+q1lTtjUR0IaSCIILXydX20yZHdgFx4dgjR+R9d\nzm7OPx/PlmMCgYARiMIDmp+LsLLunWFaldr25fmYi0aJDJXUSbY9sopWVkS3m3Je\nU1CgxnH1jMqVQckopM4z44DMh0i8gJRl4PsTcYz86K5H4yLUaKESlCbfHbye+XtK\nU510EkB9lw3YinSUx5SHyvLXxy19X5y8Kp24EdPhzI6hfFtCdRucSNi9CQKBgF7c\nH3GcwjtFStxqvtFsoKg9HogOBoV4a21EU9u5GwpKfBcZ2t0vRkxMa4WEyIrmFJk7\nXu1YT5fYcNV9bEYx2el690buIZsAnTqS67Ezq/m4QzqR5EweRS5WUZYan2WYmkH9\n7pvfvebWNs1Htbqnh+0vpB79LqYDWNI7Qy2dKDaXAoGBAKrS+3RKLBspcKtxh42u\nMDNgFykpHExlT09qqBmmD52+k7lGKeciwRiBPO2wckuTJHOsxOFt0IRCVtzrKzgL\nrz+GlYExiuvr08DvHabTwE0+ASTOlOfS1/XPO7OA2fbQTg/mUiSvqDPS225Ah6Gx\nCpfvapb71uWuMinrDbEhTEc5\n-----END PRIVATE KEY-----\n"
    }

CertificateManagementProfile = {
			"name": "test",
			"tenant_ref": "/api/tenant?name=admin",
			"script_path": "path/to/script"
    }


SystemConfiguration = {
			"avi_api_update_method": "put",
			"default_license_tier": "ENTERPRISE_18",
			"dns_configuration": {
				"search_domain": "",
				"server_list": [
					{
						"addr": "10.10.0.100",
						"type": "V4"
					}
				]
			},
			"docker_mode": False,
			"email_configuration": {
				"from_email": "admin@avi.com",
				"mail_server_name": "localhost",
				"mail_server_port": 25,
				"smtp_type": "SMTP_LOCAL_HOST"
			},
			"global_tenant_config": {
				"se_in_provider_context": True,
				"tenant_access_to_provider_se": True,
				"tenant_vrf": False
			},
			"ntp_configuration": {
				"ntp_servers": [
					{
						"server": {
							"addr": "0.us.pool.ntp.org",
							"type": "DNS"
						}
					},
					{
						"server": {
							"addr": "1.us.pool.ntp.org",
							"type": "DNS"
						}
					},
					{
						"server": {
							"addr": "2.us.pool.ntp.org",
							"type": "DNS"
						}
					},
					{
						"server": {
							"addr": "3.us.pool.ntp.org",
							"type": "DNS"
						}
					}
				]
			},
			"portal_configuration": {
				"allow_basic_authentication": True,
				"disable_remote_cli_shell": False,
				"enable_clickjacking_protection": True,
				"enable_http": False,
				"enable_https": True,
				"password_strength_check": False,
				"redirect_to_https": True,
				"sslkeyandcertificate_refs": [
					"/api/sslkeyandcertificate/?name=System-Default-Portal-Cert",
					"/api/sslkeyandcertificate/?name=System-Default-Portal-Cert-EC256"
				],
				"sslprofile_ref": "/api/sslprofile/?name=System-Standard-Portal",
				"use_uuid_from_input": False
			},
			"url": "/api/systemconfiguration"
    }



IpamdnsProviderProfile = {
			"name": "test",
			"tenant_ref": "/api/tenant?name=admin",
			"internal_profile": {
				"dns_service_domain": [
					{
						"record_ttl": 150,
						"num_dns_ip": 1,
						"domain_name": "rohan",
						"pass_through": True
					}
				],
				"ttl": 30
			},
			"type": "IPAMDNS_TYPE_INTERNAL_DNS"
    }


ServerautoscalePolicy = {
			"name": "TestAutoscaleProperty",
			"description": "Test desc",
			"tenant_ref": "/api/tenant?name=admin",
			"max_scalein_adjustment_step": 1,
			"intelligent_autoscale": False,
			"intelligent_scalein_margin": 40,
			"use_predicted_load": False,
			"intelligent_scaleout_margin": 20,
			"scaleout_alertconfig_refs": [
				"/api/alertconfig/alertconfig-bf87601c-e527-4a08-a9ba-3328b5ae94b9#Syslog-Config-Events",
				"/api/alertconfig/alertconfig-bd695fad-2100-48a1-b7a4-44e96787474f#Syslog-System-Events"
			],
			"min_size": 2,
			"scalein_alertconfig_refs": [
				"/api/alertconfig/alertconfig-81416167-98ae-40cc-947f-e5366c51605e#System-SE-Alert",
				"/api/alertconfig/alertconfig-40056299-073f-4e07-a39e-8f139f34bbdc#System-SSL-Alert"
			],
			"scalein_cooldown": 300,
			"max_scaleout_adjustment_step": 1,
			"scaleout_cooldown": 300,
			"max_size": 400
    }

ServiceengineGroup = {
			"name": "Test-Default-Group",
			"tenant_ref": "/api/tenant/?name=admin",
			"cloud_ref": "/api/cloud/?name=Default-Cloud",
			"archive_shm_limit": 8,
			"udf_log_throttle": 100,
			"se_ipc_udp_port": 1500,
			"ingress_access_data": "SG_INGRESS_ACCESS_ALL",
			"vcpus_per_se": 1,
			"disable_tso": False,
			"se_sb_dedicated_core": False,
			"async_ssl": False,
			"license_tier": "ENTERPRISE_18",
			"se_name_prefix": "Avi_new",
			"auto_redistribute_active_standby_load": False,
			"auto_rebalance": False,
			"aggressive_failure_detection": False,
			"vs_scaleout_timeout": 30,
			"auto_rebalance_interval": 300,
			"active_standby": False,
			"se_tunnel_mode": 0,
			"ignore_rtt_threshold": 5000,
			"extra_shared_config_memory": 0,
			"enable_vip_on_all_interfaces": True,
			"se_tunnel_udp_port": 1550,
			"disable_gro": False,
			"vs_scalein_timeout": 30,
			"hm_on_standby": True,
			"ha_mode": "HA_MODE_SHARED",
			"se_sb_threads": 1,
			"se_remote_punt_udp_port": 1501,
			"se_udp_encap_ipc": 0,
			"min_cpu_usage": 30,
			"disk_per_se": 10,
			"cpu_reserve": False,
			"disable_csum_offloads": False,
			"log_disksz": 10000,
			"cpu_socket_affinity": False,
			"se_probe_port": 7,
			"ingress_access_mgmt": "SG_INGRESS_ACCESS_ALL",
			"extra_config_multiplier": 0,
			"distribute_load_active_standby": False,
			"max_vs_per_se": 10,
			"async_ssl_threads": 1,
			"connection_memory_percentage": 50,
			"placement_mode": "PLACEMENT_MODE_AUTO",
			"max_scaleout_per_vs": 4,
			"vs_scalein_timeout_for_upgrade": 30,
			"vcenter_folder": "AviSeFolder",
			"os_reserved_memory": 0,
			"enable_routing": False,
			"se_bandwidth_type": "SE_BANDWIDTH_UNLIMITED",
			"waf_mempool": True,
			"se_thread_multiplier": 1,
			"se_deprovision_delay": 120,
			"dedicated_dispatcher_core": False,
			"per_app": False,
			"se_vs_hb_max_vs_in_pkt": 256,
			"vcenter_datastores_include": False,
			"advertise_backend_networks": False,
			"realtime_se_metrics": {
				"duration": 0,
				"enabled": True
			},
			"non_significant_log_throttle": 100,
			"max_cpu_usage": 80,
			"min_scaleout_per_vs": 2,
			"se_vs_hb_max_pkts_in_batch": 8,
			"host_gateway_monitor": False,
			"buffer_se": 1,
			"mem_reserve": True,
			"flow_table_new_syn_max_entries": 0,
			"vcenter_datastore_mode": "VCENTER_DATASTORE_ANY",
			"num_flow_cores_sum_changes_to_ignore": 8,
			"least_load_core_selection": True,
			"max_se": 11,
			"significant_log_throttle": 100,
			"waf_mempool_size": 64,
			"license_type": "LIC_CORES",
			"algo": "PLACEMENT_ALGO_DISTRIBUTED",
			"memory_per_se": 2048,
			"enable_vmac": False,
			"vs_host_redundancy": True
    }

GslbgeodbProfile = {
			"entries": [
				{
					"file": {
						"filename": "AviGeoDb.txt.gz",
						"format": "GSLB_GEODB_FILE_FORMAT_AVI"
					},
					"priority": 10
				}
			],
			"is_federated": True,
			"name": "test-profile",
			"tenant_ref": "/api/tenant?name=admin"
    }

ErrorPageProfile = {
			"error_pages": [
				{
					"enable": True,
					"error_page_body_ref": "/api/errorpagebody/?tenant=admin&name=Custom-Error-Page",
					"index": 2,
					"match": {
						"match_criteria": "IS_IN",
						"status_codes": [
							200
						]
					}
				}
			],
			"name": "test-pageprofile",
			"tenant_ref": "/api/tenant?name=admin"
    }

import os
Gslb = {
			"clear_on_max_retries": 20,
			"leader_cluster_uuid": "cluster-57c74b9e-551b-49f9-ba1c-d83a1acd2d19",
			"client_ip_addr_group": {
				"type": "GSLB_IP_PUBLIC"
			},
			"dns_configs": [
				{
					"domain_name": "com"
				}
			],
			"is_federated": True,
			"maintenance_mode": False,
			"name": "Default",
			"send_interval": 15,
			"sites": [
				{
					"cluster_uuid": "cluster-57c74b9e-551b-49f9-ba1c-d83a1acd2d19",
					"enabled": True,
					"ip_addresses": [
						{
							"addr": "10.10.28.132",
							"type": "V4"
						}
					],
					"location": {
						"location": {
							"latitude": 18.520429611206055,
							"longitude": 73.85674285888672,
							"name": "pune",
							"tag": "Pune"
						},
						"source": "GSLB_LOCATION_SRC_USER_CONFIGURED"
					},
					"member_type": "GSLB_ACTIVE_MEMBER",
					"name": "Test1",
					"password": "admin",
					"port": 443,
					"username": "admin"
				}
			],
			"tenant_ref": "/api/tenant?name=admin",
			"view_id": 0
    }

SeProperties = {
			"se_agent_properties": {
				"dp_enq_interval_msec": 10,
				"sdb_scan_count": 600,
				"dp_reg_pending_max_wait_time": 75,
				"controller_echo_rpc_aggressive_timeout": 2000,
				"dp_aggressive_enq_interval_msec": 1,
				"vnic_ip_delete_interval": 5,
				"dp_max_wait_rsp_time_sec": 60,
				"controller_rpc_timeout": 10,
				"controller_heartbeat_miss_limit": 6,
				"dp_aggressive_deq_interval_msec": 1,
				"controller_echo_rpc_timeout": 2000,
				"ignore_docker_mac_change": True,
				"sdb_pipeline_size": 100,
				"cpustats_interval": 5,
				"dp_batch_size": 100,
				"vnic_probe_interval": 5,
				"debug_mode": False,
				"vnic_dhcp_ip_max_retries": 10,
				"dp_deq_interval_msec": 20,
				"ctrl_reg_pending_max_wait_time": 150,
				"headless_timeout_sec": 0,
				"sdb_flush_interval": 100,
				"controller_echo_miss_aggressive_limit": 2,
				"controller_heartbeat_timeout_sec": 12,
				"controller_registration_timeout_sec": 10,
				"controller_echo_miss_limit": 4,
				"vnic_dhcp_ip_check_interval": 6
			},
			"se_runtime_properties": {
				"upstream_connpool_conn_life_tmo": -1,
				"log_agent_max_active_adf_files_per_vs": 100,
				"se_auth_ldap_conns_per_server": 1,
				"log_agent_file_sz_appl": 4,
				"se_packet_buffer_max": 0,
				"log_agent_max_logmessage_proto_sz": 65536,
				"se_hb_persist_fudge_bits": 3,
				"se_dp_vnic_stall_se_restart_window": 3600,
				"upstream_connpool_conn_max_reuse": -1,
				"upstream_connpool_server_max_cache": -1,
				"dp_aggressive_hb_timeout_count": 10,
				"se_metrics_rt_interval": 1000,
				"persistence_mem_max": 0,
				"upstream_connpool_core_max_cache": -1,
				"log_agent_log_storage_min_sz": 1024,
				"se_random_tcp_drops": False,
				"se_dp_if_state_poll_interval": 10,
				"se_auth_ldap_cache_size": 100000,
				"log_message_max_file_list_size": 64,
				"services_accessible_all_interfaces": False,
				"dupip_timeout_count": 5,
				"baremetal_dispatcher_handles_flows": False,
				"upstream_connpool_cache_thresh": -1,
				"connections_lossy_log_rate_limiter_threshold": 1000,
				"upstream_connpool_conn_idle_tmo": -1,
				"log_agent_unknown_vs_timer": 1800,
				"upstream_connpool_strategy": -1,
				"upstream_connpool_conn_idle_thresh_tmo": -1,
				"log_agent_min_storage_per_vs": 10,
				"feproxy_vips_enable_proxy_arp": True,
				"service_port_ranges": [
					{
						"start": 4000,
						"end": 9000
					}
				],
				"scaleout_udp_per_pkt": True,
				"se_dp_log_nf_enqueue_percent": 70,
				"http_rum_min_content_length": 64,
				"flow_table_batch_push_frequency": 5,
				"log_agent_file_sz_conn": 4
			}
    }



SnmptrapProfile = {
			"name": "test",
			"tenant_ref": "/api/tenant/?name=admin",
			"trap_servers": [
				{
					"community": "dummy-string",
					"ip_addr": {
						"addr": "10.10.10.2",
						"type": "V4"
					},
					"port": 162,
					"version": "SNMP_VER2"
				}
			]
    }

CustomipamdnsProfile = {
			"name": "test-ipanddns-profile",
			"script_params": [
				{
					"is_sensitive": True,
					"is_dynamic": True,
					"name": "test-profile",
					"value": "xyz"
				}
			],
			"tenant_ref": "/api/tenant?name=admin",
			"script_uri": "/"
    }

DnsPolicy = {
			"name": "test-dnspolicy",
			"tenant_ref": "/api/tenant?name=admin"
    }

ControllerProperties = {
			"vs_se_ping_fail": 60,
			"vs_se_create_fail": 1500,
			"cluster_ip_gratuitous_arp_period": 60,
			"persistence_key_rotate_period": 60,
			"unresponsive_se_reboot": 300,
			"attach_ip_retry_interval": 360,
			"vs_se_vnic_fail": 300,
			"attach_ip_retry_limit": 4,
			"se_vnic_cooldown": 120,
			"vnic_op_fail_time": 180,
			"max_pcap_per_tenant": 4,
			"vs_se_bootup_fail": 300,
			"seupgrade_fabric_pool_size": 20,
			"vs_key_rotate_period": 60,
			"seupgrade_segroup_min_dead_timeout": 360,
			"upgrade_lease_time": 360,
			"se_create_timeout": 900,
			"query_host_fail": 180,
			"vs_apic_scaleout_timeout": 360,
			"se_offline_del": 172000,
			"max_dead_se_in_grp": 1,
			"upgrade_dns_ttl": 5,
			"fatal_error_lease_time": 120,
			"allow_ip_forwarding": False,
			"max_seq_vnic_failures": 3,
			"allow_unauthenticated_nodes": False,
			"allow_unauthenticated_apis": False,
			"vs_awaiting_se_timeout": 60,
			"warmstart_se_reconnect_wait_time": 300,
			"dns_refresh_period": 60,
			"secure_channel_cleanup_timeout": 60,
			"vs_se_vnic_ip_fail": 120,
			"ssl_certificate_expiry_warning_days": [
				30,
				7,
				2
			],
			"secure_channel_se_token_timeout": 60,
			"secure_channel_controller_token_timeout": 60,
			"api_idle_timeout": 15,
			"crashed_se_reboot": 900,
			"appviewx_compat_mode": False,
			"se_failover_attempt_interval": 300,
			"dead_se_detection_timer": 360
    }
	

CloudProperties = {
			"cc_vtypes": [
				"CLOUD_OPENSTACK",
				"CLOUD_AWS",
				"CLOUD_VCA",
				"CLOUD_MESOS",
				"CLOUD_DOCKER_UCP",
				"CLOUD_RANCHER",
				"CLOUD_OSHIFT_K8S",
				"CLOUD_LINUXSERVER",
				"CLOUD_AZURE"
			],
			"hyp_props": [
				{
					"htype": "VMWARE_ESX",
					"max_nics": 10
				},
				{
					"htype": "VMWARE_VSAN",
					"max_nics": 10
				},
				{
					"htype": "KVM",
					"max_nics": 24
				},
				{
					"htype": "XEN"
				}
			],
			"info": [
				{
					"htypes": [
						"VMWARE_ESX"
					],
					"vtype": "CLOUD_VCENTER"
				},
				{
					"flavor_props": [
						{
							"id": "all",
							"max_ips_per_nic": 11,
							"name": "all",
							"public": True
						}
					],
					"htypes": [
						"KVM",
						"VMWARE_ESX",
						"VMWARE_VSAN"
					],
					"vtype": "CLOUD_OPENSTACK"
				},
				{
					"flavor_props": [
						{
							"cost": "{u'reserved': {u'yrTerm1Convertible.noUpfront': u'0.008', u'yrTerm3Convertible.allUpfront': u'0.005', u'yrTerm3Convertible.partialUpfront': u'0.005', u'yrTerm1Convertible.partialUpfront': u'0.008', u'yrTerm1Standard.partialUpfront': u'0.007', u'yrTerm3Standard.noUpfront': u'0.005', u'yrTerm3Convertible.noUpfront': u'0.006', u'yrTerm3Standard.allUpfront': u'0.004', u'yrTerm1Convertible.allUpfront': u'0.008', u'yrTerm1Standard.allUpfront': u'0.007', u'yrTerm3Standard.partialUpfront': u'0.005', u'yrTerm1Standard.noUpfront': u'0.007'}, u'ondemand': u'0.0116'}",
							"disk_gb": 0,
							"id": "t2.micro",
							"max_ips_per_nic": 2,
							"max_nics": 2,
							"name": "t2.micro",
							"public": True,
							"ram_mb": 1024,
							"vcpus": 1
						},
						{
							"cost": "{u'reserved': {u'yrTerm1Convertible.noUpfront': u'0.017', u'yrTerm3Convertible.allUpfront': u'0.011', u'yrTerm3Convertible.partialUpfront': u'0.011', u'yrTerm1Convertible.partialUpfront': u'0.016', u'yrTerm1Standard.partialUpfront': u'0.014', u'yrTerm3Standard.noUpfront': u'0.010', u'yrTerm3Convertible.noUpfront': u'0.012', u'yrTerm3Standard.allUpfront': u'0.009', u'yrTerm1Convertible.allUpfront': u'0.015', u'yrTerm1Standard.allUpfront': u'0.013', u'yrTerm3Standard.partialUpfront': u'0.009', u'yrTerm1Standard.noUpfront': u'0.014'}, u'ondemand': u'0.023'}",
							"disk_gb": 0,
							"id": "t2.small",
							"max_ips_per_nic": 4,
							"max_nics": 2,
							"name": "t2.small",
							"public": True,
							"ram_mb": 2048,
							"vcpus": 1
						}
					],
					"flavor_regex_filter": "[ctmr][0-9]+\\..*",
					"htypes": [
						"XEN"
					],
					"vtype": "CLOUD_AWS"
				},
				{
					"vtype": "CLOUD_MESOS"
				},
				{
					"vtype": "CLOUD_DOCKER_UCP"
				},
				{
					"vtype": "CLOUD_RANCHER"
				},
				{
					"vtype": "CLOUD_OSHIFT_K8S"
				},
				{
					"vtype": "CLOUD_LINUXSERVER"
				},
				{
					"htypes": [
						"VMWARE_ESX"
					],
					"vtype": "CLOUD_VCA"
				},
				{
					"flavor_props": [
						{
							"id": "all",
							"max_ips_per_nic": 150,
							"max_nics": 1,
							"name": "all",
							"public": True
						}
					],
					"vtype": "CLOUD_AZURE"
				}
			]
    }
	


TrafficCloneProfile = {
			"name": "test-traffic",
			"preserve_client_ip": True,
			"tenant_ref": "/api/tenant?name=admin"
    }

CreateUser = {
          "name": "shrikant",
          "obj_username": "shrikant",
          "obj_password": "test@1234",
          "role": "/api/role?name=Tenant-Admin",
          "user_profile_ref": "/api/useraccountprofile?name=Default-User-Account-Profile",
          "is_active": True,
          "is_superuser": True,
          "default_tenant_ref": "/api/tenant?name=admin",
          "tenant_ref": "api/tenant/admin#admin",
          "email": "test@abc.in"
}

UpdateUser = {
          "name": "shrikant",
          "obj_username": "shrikant",
          "obj_password": "test@1234",
          "role": "/api/role?name=Tenant-Admin",
          "user_profile_ref": "/api/useraccountprofile?name=Default-User-Account-Profile",
          "is_active": True,
          "is_superuser": True,
          "default_tenant_ref": "/api/tenant?name=admin",
          "tenant_ref": "api/tenant/admin#admin",
          "email": "testuser@avi.in",
}

DeleteUser = {
          "name": "shrikant",
          "state": "absent",
          "obj_username": "shrikant",
          "obj_password": "test@1234",
          "role": "/api/role?name=Tenant-Admin",
          "user_profile_ref": "/api/useraccountprofile?name=Default-User-Account-Profile",
          "is_active": True,
          "is_superuser": True,
          "default_tenant_ref": "/api/tenant?name=admin",
          "tenant_ref": "api/tenant/admin#admin",
          "email": "testuser@avi.in",
}

