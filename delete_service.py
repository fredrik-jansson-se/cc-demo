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
                          passwd=os.environ['nso_password'])

opener = urllib2.build_opener(auth_handler, urllib2.HTTPHandler(debuglevel=1))
urllib2.install_opener(opener)


DELREQ = urllib2.Request(baseUrl + '/cloud-interconnect=the-customer',
                         headers={'Accept': 'application/yang-data+json'})
DELREQ.get_method = lambda: 'DELETE'
res = opener.open(DELREQ)

