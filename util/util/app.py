import os
import json
import uuid
import time
from io import BytesIO

import PIL
from PIL import Image

from elasticsearch import Elasticsearch, RequestsHttpConnection, RequestError
from requests_aws4auth import AWS4Auth
import boto3
import requests

BUCKET = 'lolserverless' #os.environ['S3_BUCKET']
HOST = os.environ['ES_ENDPOINT']
INDEX = os.environ['ES_INDEX']
ACCESS_KEY = os.environ['ACCESS_KEY']
SECRET_KEY = os.environ['SECRET_KEY']

region = 'us-east-1'

service = 'es'
awsauth = AWS4Auth(ACCESS_KEY, SECRET_KEY, region, service)


es = Elasticsearch(
    hosts = [{'host': HOST, 'port': 443}],
    http_auth = awsauth,
    use_ssl = True,
    verify_certs = True,
    connection_class = RequestsHttpConnection
)

try:
    es.indices.create(INDEX)
except RequestError as e:
    pass

db = boto3.resource('dynamodb')
image_table = db.Table('ImageTable')

reko = boto3.client('rekognition')

s3 = boto3.resource('s3')


def lambda_handler(event, context):

    data = event['Records'][0]['s3']['object']['key']
    print(data,event)
    folder, user, image = data.split('/')   
    
    id = str(uuid.uuid4())

### Image resize
    obj = s3.Object(
        bucket_name=BUCKET,
        key=data,
    )
    obj_body = obj.get()['Body'].read()
    img = Image.open(BytesIO(obj_body))

    img = img.resize((400,400), PIL.Image.ANTIALIAS)
    buffer = BytesIO()
    img.save(buffer, 'JPEG')
    buffer.seek(0)

    resized_key = f'thumb/{user}/{image}'
    obj = s3.Object(
        bucket_name=BUCKET,
        key=resized_key,
    )
    obj.put(Body=buffer, ContentType='image/jpeg')
    obj_acl = s3.ObjectAcl(BUCKET,resized_key)
    obj_acl.put(ACL='public-read')

### Get tags using label detection

    response = reko.detect_labels(
        Image={
            'S3Object': {
                'Bucket': BUCKET,
                'Name': data,
            }
        },
        MaxLabels=3
    )

    tags = []
    for label in response['Labels']:
        tags.append(label['Name'])

### Add DynamoDB entry for the Image

    item = {
            'id' : id,
            'title' : image,
            'user' : str(user),
            'url' : f'https://{BUCKET}.s3.amazonaws.com/thumb/{user}/{image}',
            'fullUrl' : f'https://{BUCKET}.s3.amazonaws.com/{data}',
            'tags' : tags,
            'time' : str(int(time.time()))
        }

    image_table.put_item(Item = item) 

### Add item in the ElasticSearch
    
    try:
        resp = es.create(index=INDEX, id=item['id'], body=item)

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
            "message" : "indexed",
        })
    }
