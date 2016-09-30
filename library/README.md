# Configuring Ansible for Avi Vantage

## Setup
### Instlaling dependencies
- Install the Avi SDK
```
pip install avisdk
```
- You will need to download the Avi fork of `ansible-modules-extras`  
```
wget https://github.com/avinetworks/avi_ansible_modules/archive/master.tar.gz
```  
- Untar the devel.tar.gz into ansible directory `/etc/ansible/library`
```
sudo mkdir -p /etc/ansible/library/avi
tar -xvf master.tar.gz -C /etc/ansible/library
```
### Configure Ansible for the Module
>Modules can be written in any language and are found in the path specified by ANSIBLE_LIBRARY or the --module-path command line option.
>
>By default, everything that ships with Ansible is pulled from its source tree, but additional paths can be added.
>
>Documentation from: http://docs.ansible.com/ansible/developing_modules.html

Using the `-M` parameter:
```
ansible-playbook -M /etc/ansible/library/avi
```

Using the `ANSIBLE_LIBRARY` environment variable:
```
export ANSIBLE_LIBRARY=/etc/ansible/library/avi
```

- For help using the module and understanding key value pairs, please check out [Avi API Guide](https://kb.avinetworks.com/docs/latest/api-guide/)  
You can also find a visual representation of current values using https://\<controller_ip\>/api/\<object\> ex. https://10.10.27.90/api/virtualservice

## Usage
This is an example playbook:
```yaml
---
- hosts: localhost
  connection: local
  vars:
    controller: 10.10.27.90
    username: admin
    password: AviNetworks123!
  tasks:
  - avi_pool:
      controller: "{{ controller }}"
      username: "{{ username }}"
      password: "{{ password }}"
      name: testpool2
      state: present
      health_monitor_refs:
        - '/api/healthmonitor?name=System-HTTP'
      servers:
        - ip:
            addr: 10.90.130.8
            type: V4
        - ip:
            addr: 10.90.130.7
            type: V4
  - avi_virtualservice:
      controller: "{{ controller }}"
      username: "{{ username }}"
      password: "{{ password }}"
      name: newtestvs
      state: present
      performance_limits:
        max_concurrent_connections: 1000
      services:
        - port: 443
          enable_ssl: true
        - port: 80
      ssl_profile_ref: '/api/sslprofile?name=System-Standard'
      application_profile_ref: '/api/applicationprofile?name=System-Secure-HTTP'
      ssl_key_and_certificate_refs:
        - '/api/sslkeyandcertificate?name=System-Default-Cert'
      ip_address:
        addr: 10.90.131.103
        type: V4
      pool_ref: '/api/pool?name=testpool2'
```

- Other examples can be found in the `examples` folder.
