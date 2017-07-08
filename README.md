# dynamodbobjectstore

Store and retrieve python objects stored in a DynamoDB table.

Serialize objects as json strings by default, though you can specify your own
de/serializing methods.

## Installing

```
pip install dynadbobjectstore
```

## Synopsis

```
from boto import dynamodb2
from dynadbobjectstore import ObjectStore

aws_conn = dynamodb2.connect_to_region(...)

# Initialize an ObjectStore using json serialization as default
store = ObjectStore(
    aws_conn,
    'some_table_name'
)

# Create the table if needed
store.create_table()

# Store an object
a = {'a': 1, 'b': [1, 2, 3]}
store.put('mykey', a)

# Retrieve it
aa = store.get('mykey')

# Delete it
store.delete('mykey')

# No object returns None
assert not store.get('foobar')
```

To use custom to/from string serializer:

```
def myobject_to_str(o):
    return json.dumps(o)

def str_to_myobject(s):
    return json.loads(o)

s = ObjectStore(
    aws_conn,
    'some_table_name',
    to_string=myobject_to_str,
    from_string=str_to_myobject
)
```

## Testing

```
# Set the following environment variables:
export AWS_DEFAULT_REGION='eu-west-1'
export AWS_ACCESS_KEY_ID='...'
export AWS_SECRET_ACCESS_KEY='...'

nosetests test.py
```