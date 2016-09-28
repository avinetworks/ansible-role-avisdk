avisdk
=========

Using this role, you will be able to use the latest version, and version specific Avi Ansible Modules.

Requirements
------------

This role requires Ansible 1.9.3 or higher. Requirements are listed in the metadata file.


Example Playbook
----------------

Install docker to your machine.

    ---
    - hosts: localhost
      connection: local
      roles:
         - role: avinetworks.avisdk
      tasks:
        avi_module:
          ......


License
-------

MIT

Author Information
------------------

Eric Anderson
