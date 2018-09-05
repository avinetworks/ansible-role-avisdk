# avinetworks.avisdk

[![Build Status](https://travis-ci.org/avinetworks/ansible-role-avisdk.svg?branch=master)](https://travis-ci.org/avinetworks/ansible-role-avisdk)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-avinetworks.avisdk-blue.svg)](https://galaxy.ansible.com/avinetworks/avisdk/)


Using this role, you will be able to use the latest version, and version specific Avi Ansible Modules.

## Requirements

 - python >= 2.6
 - avisdk
 - requests-toolbelt

This role requires Ansible 2.0 or higher. Requirements are listed in the metadata file.

Please install avisdk from pip prior to running this module.
```

pip install avisdk --upgrade
```

## Installation

To install the AviSDK Ansible Module, please issue the command on the machine you will run Ansible from.
```

ansible-galaxy install avinetworks.avisdk
```

For more information please visit http://docs.ansible.com/ansible/galaxy.html

## Role Variables



## Example Playbooks

The following example is generic, applies to any module.

```
---
- hosts: localhost
  connection: local
  roles:
    - role: avinetworks.avisdk
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
        api_version: 17.1
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

There are many more examples located at [https://github.com/avinetworks/devops/tree/master/ansible](https://github.com/avinetworks/devops/tree/master/ansible) and also available in the "EXAMPLES" within each module.

## License

MIT

## Author Information

Eric Anderson  
[Avi Networks](http://avinetworks.com)
