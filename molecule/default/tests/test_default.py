import os
import testinfra.utils.ansible_runner
from avi.sdk.avi_api import ApiSession

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_vs_create():
    api = ApiSession.get_session(controller_ip="10.10.25.128",
                                 username="admin", password="avi123$%",
                                 tenant="admin", api_version="18.1.5",
                                 verify=False)
    resp = api.get('virtualservice')
    assert resp.json()['count'] >= 1
