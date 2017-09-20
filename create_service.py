#!/usr/bin/env python

import os

payload = {
    "cloud-interconnect:cloud-interconnect": {
        "name": "the-customer",
        "dc-esc": "escDMZ",
        "cloud-esc": "escSJ",
        "cloud-router-public-ip": os.environ['cloud_public_ip'],
        "cloud-router-private-ip": os.environ['cloud_router_private_ip'],
        "cloud-vpc-private-network": os.environ['cloud_private_network'],
        "dc-router-public-ip": os.environ['dc_public_ip'],
        "dc-router-private-ip": os.environ['dc_private_ip'],
        "dc-router-private-network": os.environ['dc_private_network']
    }
}

# http://localhost:8080/restconf/data/cloud-interconnect=the-customer
# PUT
