

class AnsibleExitJson(Exception):
    """Exception class to be raised by module.exit_json and caught by the test case"""
    pass


class AnsibleFailJson(Exception):
    """Exception class to be raised by module.fail_json and caught by the test case"""
    pass


class AnsibleModules:
    def exit_json(*args, **kwargs):
        """function to patch over exit_json; package return data into an exception"""
        print(kwargs)
        if 'changed' not in kwargs:
            kwargs['changed'] = False
        raise AnsibleExitJson(kwargs)

    def fail_json(*args, **kwargs):
        """function to patch over fail_json; package return data into an exception"""
        kwargs['failed'] = True
        raise AnsibleFailJson(kwargs)

    def get_bin_path(self, arg, required=False):
        """Mock AnsibleModule.get_bin_path"""
        if arg.endswith('my_command'):
            return '/usr/bin/my_command'
        else:
            if required:
                self.fail_json(msg='%r not found !' % arg)

