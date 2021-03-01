import json
import boto3

db = boto3.resource('dynamodb')
table = db.Table("ImageTable")


def lambda_handler(event, context):

    id = event['pathParameters']['id']
    
    
    try:
        data = table.get_item(
            Key = {
                'id' : id
            }
        )
    except Exception as e:
        print(e)
        return {
            "statusCode" : 500,
            "body" : json.dumps({
                "message" : "error"
            })
        }

    try:
        return{
            "statusCode" : 200,
            "body" : json.dumps({
                "message" : data['Item'],
            })
        }

    except KeyError as e:
        return{
            "statusCode" : 200,
            "body" : json.dumps({
                "message" : '',
            })
        }
