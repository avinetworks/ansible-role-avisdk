# avisdk


Using this role, you will be able to use the latest version, and version specific Avi Ansible Modules.

## Requirements

This role requires Ansible 2.0 or higher. Requirements are listed in the metadata file.

## Role Variables

Available variables listed below, for default values (see `defaults/main.yml`)

    version: 16.3b5


## Example Playbook

Install docker to your machine.

    ---
    - hosts: localhost
      connection: local
      vars:
        avisdk_version: 16.3b5
      roles:
         - role: avinetworks.avisdk
           version: {{ avisdk_version }}
      tasks:
        avi_<module>:
          ......


## License

BSD

## Author Information

Eric Anderson
