import json
from dynamodb_handler import search


def lambda_handler(event, context):
    jan = str(event['queryStringParameters']['jan'])
    response = search(jan)
    status = response['ResponseMetadata']['HTTPStatusCode']
    item = response['Item']
    item['price'] = int(item['price'])
    if status == 200:        
        return {
            "statusCode": status,
            "body": json.dumps({
                "message": "Found",
                "item": item
            }),
        }
    else:
        print(response)
        return {
            "statusCode": status,
        }