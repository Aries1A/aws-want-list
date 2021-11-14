import json
from dynamodb_handler import get_all
import os

#scan
def lambda_handler(event, context):
    response = get_all()
    status = response['ResponseMetadata']['HTTPStatusCode']
    items = response['Items']
    for item in items:
        item['price'] = int(item['price'])
    if status == 200:
        return {
            "statusCode": status,
            "headers": {'Access-Control-Allow-Origin': '*'},
            "body": json.dumps({
                "message": items,
            }),
        }
    else:
        print(response)
        return {
            "statusCode": status,
            "headers": {'Access-Control-Allow-Origin': '*'},
        }
