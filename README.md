# dynadbobjectstore

Store and retrieve python objects stored in a DynamoDB table.

## Installing

```
pip install dynadbobjectstore
```

## Synopsis

```
from dynadbobjectstore import ObjectStore

from boto import dynamodb2

aws_conn = dynamodb2.connect_to_region(...)

# Initialize an ObjectStore using json serialization as default
s = S3ImageResizer(
    aws_conn,
    'some_table_name'
)

# Store an object
a = {'a': 1, 'b': [1, 2, 3]}
s.put('mykey', a)

# Retrieve it
aa = s.get('mykey')

# Delete it
s.delete('mykey')

# No object returns None
assert not s.get('foobar')
```

To use custom to/from string serializer:

```
def myobject_to_str(o):
    ...

def str_to_myobject(s):
    ...

s = S3ImageResizer(
    aws_conn,
    'some_table_name',
    to_string=myobject_to_str,
    from_string=str_to_myobject
)
```