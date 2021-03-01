import json
import os

import boto3
from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth

endpoint = os.environ['ES_ENDPOINT']
index = os.environ['ES_INDEX']
access_key = os.environ['ACCESS_KEY']
secret_key = os.environ['SECRET_KEY']

region = 'us-east-1'
service = 'es'
awsauth = AWS4Auth(access_key, secret_key, region, service)

es = Elasticsearch(
    hosts = [{'host': endpoint, 'port': 443}],
    http_auth = awsauth,
    use_ssl = True,
    verify_certs = True,
    connection_class = RequestsHttpConnection
)


def lambda_handler(event, context):
    
    tag = event['queryStringParameters']['tag']

    try:
        
        resp = es.search(index=index, body = {
            'query' : {
                'match' : {
                    'tags' : tag 
                }
            }
        })

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
            "message" : resp['hits']['hits'],
        })
    }

