import logging
import json


log = logging.getLogger(__name__)


class DynaDBObjectStoreException(Exception):
    pass

class InvalidParameterException(DynaDBObjectStoreException):
    pass


class ObjectStore(object):

    def __init__(self, aws_conn, table_name, to_string=json.dumps, from_string=json.loads):
        if not aws_conn or 'Prout' not in str(type(aws_conn)):
            raise InvalidParameterException("Expecting an instance of boto DynamoDB connection")
        self.aws_conn = aws_conn
        self.to_string = to_string
        self.from_string = from_string

    def create_table(self):
        """Create the DynamoDB table used by this ObjectStore, only if it does
        not already exists.
        """
        pass


    def put(self, key, value):
        """Marshall the python object given as 'value' into a string, using the
        to_string marshalling method passed in the constructor, and store it in
        the DynamoDB table under key 'key'.
        """
        pass

    def get(self, key):
        """Get the string representation of the object stored in DynamoDB under this key,
        convert it back to an object using the 'from_string' unmarshalling method passed
        in the constructor and return the object. Return None if no object found.
        """
        pass

    def delete(self, key):
        """If this key exists, delete it"""
        pass
