import json
from dynamodb_handler import register


def lambda_handler(event, context):
    payload = json.loads(event['body'])
    jan = str(payload['jan'])
    price = int(payload['price'])
    response = register(jan, price)
    status = response['ResponseMetadata']['HTTPStatusCode']
    item = {'jan': jan, 'price': price}
    if status == 200:
        return {
            "statusCode": status,
            "body": json.dumps({
                "message": "OK",
                "item": item
            }),
        }
    else:
        print(response)
        return {
            "statusCode": status,
        }
