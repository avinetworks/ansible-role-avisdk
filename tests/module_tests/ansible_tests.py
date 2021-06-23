import json
import pytest
import vcr
import unittest
from mock import patch
from ansible.module_utils._text import to_bytes
from ansible.module_utils import basic

from library import avi_healthmonitor, avi_virtualservice, \
    avi_tenant, avi_pool, avi_vsvip, avi_wafpolicy, avi_wafprofile, \
    avi_useraccountprofile, avi_dnspolicy, \
    avi_applicationpersistenceprofile, avi_applicationprofile, avi_network, avi_networkprofile, avi_gslb, \
    avi_vsdatascriptset, avi_sslprofile, avi_httppolicyset, avi_backupconfiguration, avi_role, avi_scheduler, \
    avi_vrfcontext, avi_cloud, avi_prioritylabels, avi_gslbservice, avi_stringgroup, avi_hardwaresecuritymodulegroup, \
    avi_ipaddrgroup, avi_webhook, avi_user, \
    avi_actiongroupconfig, avi_microservicegroup, avi_alertconfig, avi_alertemailconfig, avi_networksecuritypolicy, \
    avi_alertscriptconfig, avi_alertsyslogconfig, avi_pkiprofile, avi_analyticsprofile, avi_poolgroupdeploymentpolicy, \
    avi_authprofile, avi_autoscalelaunchconfig, avi_cloudconnectoruser, avi_certificatemanagementprofile, \
    avi_systemconfiguration, avi_ipamdnsproviderprofile, avi_serverautoscalepolicy, avi_serviceenginegroup, \
    avi_gslbgeodbprofile, avi_errorpageprofile, avi_seproperties, avi_snmptrapprofile, avi_customipamdnsprofile, \
    avi_controllerproperties, avi_cloudproperties, avi_trafficcloneprofile, avi_api_image
import config as configure
from baseModules import AnsibleModules
from baseModules import (AnsibleExitJson, AnsibleFailJson)
import os
import requests

modiles = AnsibleModules()

my_vcr = vcr.VCR(
    cassette_library_dir='fixtures/cassettes',
    record_mode='once'
)

ControllerCredentials = {
    "avi_credentials": {
        "controller": os.environ['AVI_CONTROLLER'],
        "username": os.environ["AVI_USERNAME"],
        "password": os.environ["AVI_PASSWORD"],
        "api_version": os.environ["API_VERSION"],
    }
}

def set_module_args(args):
    args = json.dumps({'ANSIBLE_MODULE_ARGS': args})
    basic._ANSIBLE_ARGS = to_bytes(args)

@my_vcr.use_cassette()
def get_cluster_id():

    login_url = 'https://%s/login' % os.environ['AVI_CONTROLLER']
    cluster_url = 'https://%s/api/cluster' % os.environ[
        'AVI_CONTROLLER']
    headers = {"Content-Type": "application/json"}
    login_data = {'username': os.environ["AVI_USERNAME"], 'password':
        os.environ["AVI_PASSWORD"]}

    session = requests.session()
    session.headers.update(headers)
    rsp = session.post(login_url, json.dumps(login_data), headers=headers,
                       verify=False)
    login_success = False

    if rsp.status_code == 200:
        login_success = True

    if not login_success:
        raise Exception(
            'Fail to login to controller %s' % os.environ['AVI_CONTROLLER'])

    csrftoken = requests.utils.dict_from_cookiejar(rsp.cookies).get(
        'csrftoken', '')
    referer = 'https://%s/' % os.environ['AVI_CONTROLLER']
    session.headers.update({"X-CSRFToken": csrftoken,
                            "Referer": referer})

    resp = session.get(cluster_url, headers=headers, verify=False)
    data = resp.json()
    return data['uuid']

class test_ansible_modules(unittest.TestCase):

    def setUp(self):
        self.mock_module_helper = patch.multiple(basic.AnsibleModule,
                                                 exit_json=modiles.exit_json,
                                                 fail_json=modiles.fail_json,
                                                 get_bin_path=modiles.get_bin_path)
        self.mock_module_helper.start()
        self.addCleanup(self.mock_module_helper.stop)

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_create_http_hm(self):
        configure.HealthMonitor.update(ControllerCredentials)
        set_module_args(configure.HealthMonitor)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_healthmonitor.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_VsVip(self):
        configure.VsVip.update(ControllerCredentials)
        set_module_args(configure.VsVip)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_vsvip.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_virtual_service(self):
        configure.VirtualService.update(ControllerCredentials)
        set_module_args(configure.VirtualService)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_virtualservice.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_tenant(self):
        configure.Tenant.update(ControllerCredentials)
        set_module_args(configure.Tenant)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_tenant.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_pool(self):
        configure.Pool.update(ControllerCredentials)
        set_module_args(configure.Pool)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_pool.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_userAccountProfile(self):
        configure.Useraccountprofile.update(ControllerCredentials)
        set_module_args(configure.Useraccountprofile)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_useraccountprofile.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_wafPolicy(self):
        configure.WafPolicy.update(ControllerCredentials)
        set_module_args(configure.WafPolicy)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_wafpolicy.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_wafProfile(self):
        configure.Wafprofile.update(ControllerCredentials)
        set_module_args(configure.Wafprofile)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_wafprofile.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_appPersistProfile(self):
        configure.Applicationpersisteceprofile.update(ControllerCredentials)
        set_module_args(configure.Applicationpersisteceprofile)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_applicationpersistenceprofile.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_applicationProfile(self):
        configure.ApplicationProfile.update(ControllerCredentials)
        set_module_args(configure.ApplicationProfile)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_applicationprofile.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_NetworkProfile(self):
        configure.Networkprofile.update(ControllerCredentials)
        set_module_args(configure.Networkprofile)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_networkprofile.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_SslProfile(self):
        configure.SslProfile.update(ControllerCredentials)
        set_module_args(configure.SslProfile)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_sslprofile.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_HttpPolicySet(self):
        configure.HttpPolicySet.update(ControllerCredentials)
        set_module_args(configure.HttpPolicySet)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_httppolicyset.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_BackupConfiguration(self):
        configure.BackupConfiguration.update(ControllerCredentials)
        set_module_args(configure.BackupConfiguration)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_backupconfiguration.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_Role(self):
        configure.Role.update(ControllerCredentials)
        set_module_args(configure.Role)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_role.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_Scheduler(self):
        configure.Scheduler.update(ControllerCredentials)
        set_module_args(configure.Scheduler)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_scheduler.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_Prioritylabels(self):
        configure.Prioritylabels.update(ControllerCredentials)
        set_module_args(configure.Prioritylabels)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_prioritylabels.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_Cloud(self):
        configure.Cloud.update(ControllerCredentials)
        set_module_args(configure.Cloud)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_cloud.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_Vrfcontext(self):
        configure.Vrfcontext.update(ControllerCredentials)
        set_module_args(configure.Vrfcontext)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_vrfcontext.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_Gslbservice(self):
        configure.Gslbservice.update(ControllerCredentials)
        set_module_args(configure.Gslbservice)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_gslbservice.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_Useraccountprofile(self):
        configure.Useraccountprofile.update(ControllerCredentials)
        set_module_args(configure.Useraccountprofile)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_useraccountprofile.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_VsDataScriptSet(self):
        configure.VsDataScriptSet.update(ControllerCredentials)
        set_module_args(configure.VsDataScriptSet)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_vsdatascriptset.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_StringGroup(self):
        configure.StringGroup.update(ControllerCredentials)
        set_module_args(configure.StringGroup)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_stringgroup.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_HardwareSecurityModuleGroup(self):
        configure.HardwareSecurityModuleGroup.update(ControllerCredentials)
        set_module_args(configure.HardwareSecurityModuleGroup)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_hardwaresecuritymodulegroup.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_Ipaddrgroup(self):
        configure.Ipaddrgroup.update(ControllerCredentials)
        set_module_args(configure.Ipaddrgroup)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_ipaddrgroup.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_Ipamdnsproviderprofile(self):
        configure.Ipamdnsproviderprofile.update(ControllerCredentials)
        set_module_args(configure.Ipamdnsproviderprofile)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_ipamdnsproviderprofile.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_Webhook(self):
        configure.Webhook.update(ControllerCredentials)
        set_module_args(configure.Webhook)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_webhook.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_MicroserviceGroup(self):
        configure.MicroserviceGroup.update(ControllerCredentials)
        set_module_args(configure.MicroserviceGroup)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_microservicegroup.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_ActionGroupConfig(self):
        configure.ActionGroupConfig.update(ControllerCredentials)
        set_module_args(configure.ActionGroupConfig)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_actiongroupconfig.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_AlertConfig(self):
        configure.AlertConfig.update(ControllerCredentials)
        set_module_args(configure.AlertConfig)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_alertconfig.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_AlertEmailConfig(self):
        configure.AlertEmailConfig.update(ControllerCredentials)
        set_module_args(configure.AlertEmailConfig)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_alertemailconfig.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_Network(self):
        configure.Network.update(ControllerCredentials)
        set_module_args(configure.Network)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_network.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_NetworkSecurityPolicy(self):
        configure.NetworkSecurityPolicy.update(ControllerCredentials)
        set_module_args(configure.NetworkSecurityPolicy)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_networksecuritypolicy.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_AlertSyslogConfig(self):
        configure.AlertSyslogConfig.update(ControllerCredentials)
        set_module_args(configure.AlertSyslogConfig)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_alertsyslogconfig.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_PkiProfile(self):
        configure.PkiProfile.update(ControllerCredentials)
        set_module_args(configure.PkiProfile)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_pkiprofile.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_AnalyticsProfile(self):
        configure.AnalyticsProfile.update(ControllerCredentials)
        set_module_args(configure.AnalyticsProfile)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_analyticsprofile.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_AuthProfile(self):
        configure.AuthProfile.update(ControllerCredentials)
        set_module_args(configure.AuthProfile)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_authprofile.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_AutoScaleLaunchConfig(self):
        configure.AutoScaleLaunchConfig.update(ControllerCredentials)
        set_module_args(configure.AutoScaleLaunchConfig)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_autoscalelaunchconfig.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_CloudConnecTorUser(self):
        configure.CloudConnecTorUser.update(ControllerCredentials)
        set_module_args(configure.CloudConnecTorUser)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_cloudconnectoruser.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_CertificateManagementProfile(self):
        configure.CertificateManagementProfile.update(ControllerCredentials)
        set_module_args(configure.CertificateManagementProfile)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_certificatemanagementprofile.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_SystemConfiguration(self):
        configure.SystemConfiguration.update(ControllerCredentials)
        set_module_args(configure.SystemConfiguration)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_systemconfiguration.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_ServerautoscalePolicy(self):
        configure.ServerautoscalePolicy.update(ControllerCredentials)
        set_module_args(configure.ServerautoscalePolicy)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_serverautoscalepolicy.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_ServiceengineGroup(self):
        configure.ServiceengineGroup.update(ControllerCredentials)
        set_module_args(configure.ServiceengineGroup)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_serviceenginegroup.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_GslbgeodbProfile(self):
        configure.GslbgeodbProfile.update(ControllerCredentials)
        set_module_args(configure.GslbgeodbProfile)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_gslbgeodbprofile.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_ErrorPageProfile(self):
        configure.ErrorPageProfile.update(ControllerCredentials)
        set_module_args(configure.ErrorPageProfile)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_errorpageprofile.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_Gslb(self):
        id = get_cluster_id()

        configure.Gslb.update(ControllerCredentials)
        configure.Gslb['sites'][0]["ip_addresses"][0]["addr"] = str(os.environ[
           "AVI_CONTROLLER"])
        configure.Gslb["leader_cluster_uuid"] = str(id)
        configure.Gslb['sites'][0]["cluster_uuid"] = str(id)
        configure.Gslb['sites'][0]['password'] = str(os.environ[
                                                         "AVI_PASSWORD"])
        set_module_args(configure.Gslb)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_gslb.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_SeProperties(self):
        configure.SeProperties.update(ControllerCredentials)
        set_module_args(configure.SeProperties)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_seproperties.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_SnmptrapProfile(self):
        configure.SnmptrapProfile.update(ControllerCredentials)
        set_module_args(configure.SnmptrapProfile)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_snmptrapprofile.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_CustomipamdnsProfile(self):
        configure.CustomipamdnsProfile.update(ControllerCredentials)
        set_module_args(configure.CustomipamdnsProfile)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_customipamdnsprofile.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_DnsPolicy(self):
        configure.DnsPolicy.update(ControllerCredentials)
        set_module_args(configure.DnsPolicy)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_dnspolicy.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_ControllerProperties(self):
        configure.ControllerProperties.update(ControllerCredentials)
        set_module_args(configure.ControllerProperties)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_controllerproperties.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_CloudProperties(self):
        configure.CloudProperties.update(ControllerCredentials)
        set_module_args(configure.CloudProperties)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_cloudproperties.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_TrafficCloneProfile(self):
        configure.TrafficCloneProfile.update(ControllerCredentials)
        set_module_args(configure.TrafficCloneProfile)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_trafficcloneprofile.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_AlertScriptConfig(self):
        configure.AlertScriptConfig.update(ControllerCredentials)
        set_module_args(configure.AlertScriptConfig)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_alertscriptconfig.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_PoolGroupDeploymentPolicy(self):
        configure.PoolGroupDeploymentPolicy.update(ControllerCredentials)
        set_module_args(configure.PoolGroupDeploymentPolicy)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_poolgroupdeploymentpolicy.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_create_user(self):
        configure.CreateUser.update(ControllerCredentials)
        set_module_args(configure.CreateUser)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_user.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_update_user(self):
        configure.CreateUser.update(ControllerCredentials)
        set_module_args(configure.UpdateUser)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_user.main()
            self.assertTrue(result.exception.args[0]['changed'])

    @pytest.mark.travis
    @my_vcr.use_cassette()
    def test_delete_user(self):
        configure.CreateUser.update(ControllerCredentials)
        set_module_args(configure.DeleteUser)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_user.main()
            self.assertTrue(result.exception.args[0]['changed'])

    # TODO: add support for travis test
    def test_upload_image(self):
        configure.ImageApi.update(ControllerCredentials)
        set_module_args(configure.ImageApi)
        with self.assertRaises(AnsibleExitJson) as result:
            avi_api_image.main()
            self.assertTrue(result.exception.args[0]['changed'])

