import json
import boto3

db = boto3.resource('dynamodb')
table = db.Table("ImageTable")


def lambda_handler(event, context):

    try :
        resp = table.scan()
        data = resp['Items']

        while 'LastEvaluatedKey' in resp:
            resp = table.scan(ExclusiveStartKey=resp['LastEvaluatedKey'])
            data.extend(resp['Items'])

    except Exception as e:
        print(e)
        return {
            "statusCode" : 500,
            "body" : json.dumps({
                "message" : "error"
            })
        }

    return{
        "statusCode" : 200,
        "body" : json.dumps({
            "message" : data,
        })
    }
