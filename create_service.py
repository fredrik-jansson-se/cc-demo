#!/usr/bin/env python

import os
import urllib2
import json
import time

host = os.environ['nso_host']

baseUrl = host + '/restconf/data'
auth_handler = urllib2.HTTPBasicAuthHandler()
auth_handler.add_password(realm='restconf',
                          uri=baseUrl,
                          user='admin',
                          passwd='admin')

opener = urllib2.build_opener(auth_handler, urllib2.HTTPHandler(debuglevel=1))
urllib2.install_opener(opener)

tpayload = """{{
    "cloud-interconnect:cloud-interconnect": {{
        "name": "the-customer",
        "dc-esc": "escDMZ",
        "cloud-esc": "escSJ",
        "cloud-router-public-ip": "{}",
        "cloud-router-private-ip": "{}",
        "cloud-vpc-private-network": "{}",
        "dc-router-public-ip": "{}",
        "dc-router-private-ip": "{}",
        "dc-router-private-network": "{}"
    }}
}}""".format(os.environ['cloud_public_ip'],
             os.environ['cloud_router_private_ip'],
             os.environ['cloud_private_network'],
             os.environ['dc_public_ip'],
             os.environ['dc_private_ip'],
             os.environ['dc_private_network'])

PUTREQ = urllib2.Request(baseUrl + '/cloud-interconnect=the-customer',
                         headers={'Content-Type': 'application/yang-data+json',
                                  'Accept': 'application/yang-data+json'},
                         data=tpayload)
PUTREQ.get_method = lambda: 'PUT'
res = opener.open(PUTREQ)

REQ = urllib2.Request(baseUrl+'/cloud-interconnect=the-customer/plan/'
                      'component=self/state=ready/status',
                      headers={"Accept": "application/yang-data+json"})
while True:
    TXT = urllib2.urlopen(REQ).read()
    JDATA = json.loads(TXT)
    print(JDATA)
    if JDATA['cloud-interconnect:status'] == 'reached':
        break
    time.sleep(5)
