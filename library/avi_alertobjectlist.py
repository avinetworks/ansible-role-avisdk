#!/usr/bin/python
#
# Created on Aug 25, 2016
# @author: Gaurav Rastogi (grastogi@avinetworks.com)
#          Eric Anderson (eanderson@avinetworks.com)
# module_check: supported
#
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#

ANSIBLE_METADATA = {'metadata_version': '1.0',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_alertobjectlist
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: Module for setup of AlertObjectList Avi RESTful Object
description:
    - This module is used to configure AlertObjectList object
    - more examples at U(https://github.com/avinetworks/devops)
requirements: [ avisdk ]
version_added: "2.4"
options:
    state:
        description:
            - The state that should be applied on the entity.
        default: present
        choices: ["absent","present"]
    name:
        description:
            - Name of the object.
        required: true
    objects:
        description:
            - Enum options - virtualservice, pool, healthmonitor, networkprofile, applicationprofile, httppolicyset, dnspolicy, ipaddrgroup, stringgroup,
            - sslprofile, sslkeyandcertificate, networksecuritypolicy, applicationpersistenceprofile, analyticsprofile, vsdatascriptset, tenant, pkiprofile,
            - authprofile, cloud, serverautoscalepolicy, autoscalelaunchconfig, microservicegroup, ipamprofile, hardwaresecuritymodulegroup, poolgroup,
            - prioritylabels, poolgroupdeploymentpolicy, gslbservice, gslbhealthmonitor, gslbserviceruntime, scheduler, gslbgeodbprofile,
            - gslbapplicationpersistenceprofile, trafficcloneprofile, vsvip, serviceengine, debugserviceengine, debugcontroller, debugvirtualservice,
            - serviceenginegroup, seproperties, network, controllernode, controllerproperties, systemconfiguration, vrfcontext, user, alertconfig,
            - alertsyslogconfig, alertemailconfig, alerttypeconfig, application, role, cloudproperties, snmptrapprofile, actiongroupprofile, microservice,
            - alertparams, actiongroupconfig, cloudconnectoruser, gslb, gslbdnsupdate, gslbsiteops, glbmgrwarmstart, ipamdnsrecord, gslbdnsgsstatus,
            - gslbdnsgeofileops, gslbdnsgeoupdate, gslbdnsgeoclusterops, gslbdnscleanup, tcpstatruntime, udpstatruntime, ipstatruntime, arpstatruntime,
            - mbstatruntime, ipstkqstatsruntime, mallocstatruntime, shmallocstatruntime, cpuusageruntime, l7globalstatsruntime, l7virtualservicestatsruntime,
            - seagentvnicdbruntime, seagentgraphdbruntime, seagentstateruntime, interfaceruntime, arptableruntime, dispatcherstatruntime,
            - dispatcherstatclearruntime, dispatchertabledumpruntime, dispatcherremotetimerlistdumpruntime, metricsagentmessage, healthmonitorstatruntime,
            - metricsentityruntime, persistenceinternal, httppolicysetinternal, dnspolicyinternal, connectiondumpruntime, shareddbstats, shareddbstatsclear,
            - icmpstatruntime, routetableruntime, virtualmachine, poolserver, sevslist, meminforuntime, rteringstatruntime, algostatruntime,
            - healthmonitorruntime, cpustatruntime, sevm, host, portgroup, cluster, datacenter, vcenter, httppolicysetstats, dnspolicystats, metricssestats,
            - ratelimiterstatruntime, networksecuritypolicystats, tcpconnruntime, poolstats, connpoolinternal, connpoolstats, vshashshowruntime,
            - selogstatsruntime, networksecuritypolicydetail, licenseruntime, serverruntime, metricsruntimesummary, metricsruntimedetail,
            - dispatchersehmprobetempdisableruntime, pooldebug, vslogmgrmap, seruminsertionstats, httpcache, httpcachestats, sedosstatruntime, vsdosstatruntime,
            - serverupdatereq, vsscaleoutlist, sememdistruntime, tcpconnruntimedetail, seupgradestatus, seupgradepreview, sefaultinjectexhaustm,
            - sefaultinjectexhaustmcl, sefaultinjectexhaustmclsmall, sefaultinjectexhaustconn, seheadlessonlinereq, seupgrade, seupgradestatusdetail,
            - sereservedvs, sereservedvsclear, vscandidatesehostlist, segroupupgrade, rebalance, segrouprebalance, seauthstatsruntime, autoscalestate,
            - virtualserviceauthstats, networksecuritypolicydos, keyvalinternal, keyvalsummaryinternal, serverstateupdateinfo, cltrackinternal,
            - cltracksummaryinternal, microserviceruntime, semicroservice, virtualserviceanalysis, clientinternal, clientsummaryinternal,
            - microservicegroupruntime, bgpruntime, requestqueueruntime, migrateall, migrateallstatussummary, migrateallstatusdetail, interfacesummaryruntime,
            - interfacelacpruntime, dnstable, gslbservicedetail, gslbserviceinternal, gslbservicehmonstat, setrolesrequest, trafficcloneruntime,
            - geolocationinfo, sevshbstatruntime, geodbinternal, gslbsiteinternal, seresourceproto, seconsumerproto, secreatependingproto, placementstats,
            - sevipproto, rmvrfproto, vcentermap, vimgrvcenterruntime, interestedvms, interestedhosts, vcentersupportedcounters, entitycounters,
            - transactionstats, sevmcreateprogress, placementstatus, visubfolders, vidatastore, vihostresources, cloudconnector, vinetworksubnetvms,
            - vidatastorecontents, vimgrvcentercloudruntime, vivcenterportgroups, vivcenterdatacenters, vimgrhostruntime, placementglobals, apicconfiguration,
            - ciftable, apictransaction, virtualservicestatedbcachesummary, poolstatedbcachesummary, serverstatedbcachesummary, apicagentinternal,
            - apictransactionflap, apicgraphinstances, apicepgs, apicepgeps, apicdevicepkgver, apictenants, apicvmmdomains, nsxconfiguration, nsxsgtable,
            - nsxagentinternal, nsxsginfo, nsxsgips, nsxagentinternalcli, maxobjects.
    source:
        description:
            - Enum options - conn_logs, app_logs, event_logs, metrics.
        required: true
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
    url:
        description:
            - Avi controller URL of the object.
    uuid:
        description:
            - Unique object identifier of the object.
extends_documentation_fragment:
    - avi
'''


EXAMPLES = '''
  - name: Avi Alert object list
    avi_alertobjectlist:
      controller: ''
      username: ''
      password: ''
      name: EventObjectList
      objects:
      - VIRTUALSERVICE
      - POOL
      - SERVICEENGINE
      - CLUSTER
      source: EVENT_LOGS
      tenant_ref: admin
'''
RETURN = '''
obj:
    description: AlertObjectList (api/alertobjectlist) object
    returned: success, changed
    type: dict
'''

from ansible.module_utils.basic import AnsibleModule
try:
    from avi.sdk.utils.ansible_utils import avi_common_argument_spec
    from pkg_resources import parse_version
    import avi.sdk
    sdk_version = getattr(avi.sdk, '__version__', None)
    if ((sdk_version is None) or (sdk_version and
            (parse_version(sdk_version) < parse_version('17.1')))):
        # It allows the __version__ to be '' as that value is used in development builds
        raise ImportError
    from avi.sdk.utils.ansible_utils import avi_ansible_api
    HAS_AVI = True
except ImportError:
    HAS_AVI = False


def main():
    argument_specs = dict(
        state=dict(default='present',
                   choices=['absent', 'present']),
        name=dict(type='str', required=True),
        objects=dict(type='list',),
        source=dict(type='str', required=True),
        tenant_ref=dict(type='str',),
        url=dict(type='str',),
        uuid=dict(type='str',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk>=17.1) is not installed. '
            'For more details visit https://github.com/avinetworks/sdk.'))
    return avi_ansible_api(module, 'alertobjectlist',
                           set([]))

if __name__ == '__main__':
    main()
