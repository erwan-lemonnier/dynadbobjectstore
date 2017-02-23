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
import json
import logging
from unittest import TestCase
from boto import dynamodb2
from boto.dynamodb2.exceptions import ItemNotFound
from dynadbobjectstore import ObjectStore

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


class Test(TestCase):

    def setUp(self):

        for k in ('AWS_DEFAULT_REGION', 'AWS_ACCESS_KEY_ID', 'AWS_SECRET_ACCESS_KEY'):
            if k not in os.environ:
                return

        conn = dynamodb2.connect_to_region(
            os.environ['AWS_DEFAULT_REGION'],
            aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
            aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY']
        )

        # Create both dynamodb table and ObjectStore
        self.store = ObjectStore(conn, 'objectstore-test-table--delete-at-will')
        self.store.create_table()


    def test_put_get_delete__dict(self):

        if not hasattr(self, 'store'):
            return

        # Store then retrieve a dict
        o = {
            'whatever': ['dois', 33, 'mtocare?'],
            'foo': 12123,
        }

        self.store.put('aname', o)
        oo = self.store.get('aname')

        self.assertDictEqual(o, oo)

        # Now delete it
        self.store.delete('aname')


    def test_put_get_delete__string(self):

        if not hasattr(self, 'store'):
            return

        # Store then retrieve a dict
        o = "blablabla"

        self.store.put('aname2', o)
        oo = self.store.get('aname2')
        log.info("got: %s (%s)" % (oo, type(oo)))

        self.assertEqual(o, oo)

        # Now delete it
        self.store.delete('aname2')


    def test_get_non_existing_item(self):
        # Should raise an ItemNotFound exception
        def shouldfail():
            self.store.get('foobar')
        self.assertRaises(ItemNotFound, shouldfail)


    def test_delete_non_existing_item(self):
        # No exception expected...
        self.store.delete('foobar')
