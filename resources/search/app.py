import json
from dynamodb_handler import search


def lambda_handler(event, context):
    jan = str(event['queryStringParameters']['jan'])
    if len(jan) == 0:
        jan = '-1'
    response = search(jan)
    status = response['ResponseMetadata']['HTTPStatusCode']
    try:
        item = response['Item']
        item['price'] = int(item['price'])
        message = 'Found'
    except KeyError:
        item = None
        message = 'Not Found'
    if status == 200:
        return {
            "statusCode": status,
            "headers": {
                'Access-Control-Allow-Origin': '*',
                },
            "body": json.dumps({
                "message": message,
                "item": [item]
            }),
        }
    else:
        print(response)
        return {
            "statusCode": status,
            "headers": {
                'Access-Control-Allow-Origin': '*',
                },
            "body": json.dumps({
                "message": "Not Found",
                "item": {}
            })
        }
