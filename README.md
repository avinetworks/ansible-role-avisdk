# avinetworks.avisdk
[![Build Status](https://travis-ci.org/avinetworks/ansible-role-avisdk.svg?branch=master)](https://travis-ci.org/avinetworks/ansible-role-avisdk)

Using this role, you will be able to use the latest version, and version specific Avi Ansible Modules.

## Requirements

 - python >= 2.6
 - avisdk

This role requires Ansible 2.0 or higher. Requirements are listed in the metadata file.

## Installation

To install the AviSDK Ansible Module, please issue the command on the machine you will run Ansible from.
```
ansible-galaxy install avinetworks.avisdk
```

For more information please visit http://docs.ansible.com/ansible/galaxy.html

## Role Variables

Available variables listed below, for default values (see `defaults/main.yml`)

```

avisdk_install: true    # default is false allows auto-installation of avisdk python package to localhost
avisdk_version: 16.3b5  # default is 'latest'
```

## Example Playbook

The following example is generic, applies to any module.

```
    ---
    - hosts: localhost
      connection: local
      roles:
        - role: avinetworks.avisdk
          avisdk_version: 16.3b5
          avisdk_install: true
      tasks:
        - avi_<module_name>:
          controller: 10.10.27.90
          username: admin
          password: AviNetworks123!
          ......
```

This example shows usage of the avi_healthmonitor module included in this role.

```
    ---
    - hosts: localhost
      connection: local
      roles:
        - role: avinetworks.avisdk
      tasks:
        - avi_healthmonitor:
            controller: 10.10.27.90
            username: admin
            password: AviNetworks123!
            https_monitor:
              http_request: HEAD / HTTP/1.0
              http_response_code:
                - HTTP_2XX
                - HTTP_3XX
            receive_timeout: 4
            failed_checks: 3
            send_interval: 10
            successful_checks: 3
            type: HEALTH_MONITOR_HTTPS
            name: MyWebsite-HTTPS
```

There are many more examples located at [https://github.com/avinetworks/avi-ansible-samples](https://github.com/avinetworks/avi-ansible-samples) and also available in the "EXAMPLES" within each module.

## License

MIT

## Author Information

Eric Anderson
[Avi Networks](http://avinetworks.com)
