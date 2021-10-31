import boto3
import os
from boto3.resources.model import ResponseResource


dynamoDB = boto3.resource('dynamodb')
table = dynamoDB.Table(os.environ['TABLE_NAME'])


def get_all():
    response = table.scan()
    return response


def search(jan):
    response = table.get_item(Key={'jan': jan})
    return response


def register(jan, price):
    response = table.put_item(
        Item={
            'jan': jan,
            'price': price
        }
    )
    return response
