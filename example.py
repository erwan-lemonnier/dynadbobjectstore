#!/usr/bin/env python

# Illustrate using dynadbobjectstore for serializing/deserializing a python
# data structure to dynamodb
#
# Assuming you set the following environment variables:
# * AWS_DEFAULT_REGION: your aws region (ex: eu-west-1)
# * AWS_ACCESS_KEY_ID: your aws access key
# * AWS_SECRET_ACCESS_KEY: your aws secret key


import os
import sys
import logging
from boto import dynamodb2

# Setup logging
log = logging.getLogger(__name__)
root = logging.getLogger()
root.setLevel(logging.DEBUG)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s: %(levelname)s %(message)s')
ch.setFormatter(formatter)
root.addHandler(ch)
logging.getLogger('boto').setLevel(logging.INFO)


conn = dynamodb2.connect_to_region(
    os.environ['AWS_DEFAULT_REGION'],
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY']
)

from dynadbobjectstore import ObjectStore

store = ObjectStore(conn, 'objectstore-test-table--delete-at-will')

store.create_table()
