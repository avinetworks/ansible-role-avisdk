avisdk
=========

Using this role, you will be able to use the latest version, and version specific Avi Ansible Modules.

Requirements
------------

This role requires Ansible 2.0 or higher. Requirements are listed in the metadata file.


Example Playbook
----------------

Install docker to your machine.

    ---
    - hosts: localhost
      connection: local
      roles:
         - role: avinetworks.avisdk
      tasks:
        avi_<module>:
          ......


License
-------

BSD

Author Information
------------------

Eric Anderson
