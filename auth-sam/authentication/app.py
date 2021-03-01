import boto3
import hmac
import hashlib
import base64
import json
import os

import sign_up, confirm_sign_up, login

client = boto3.client('cognito-idp')

CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
POOL_ID = os.environ['POOL_ID']


def get_secret_hash(username):
    message = username + CLIENT_ID
    dig = hmac.new(CLIENT_SECRET.encode('UTF-8'), msg=message.encode('UTF-8'),
                    digestmod=hashlib.sha256).digest()
    return base64.b64encode(dig).decode()


def sign_up_handler(event, context):
    body = json.loads(event['body'])
    username = body['username']
    password = body['password']
    email = body['email']

    info = {
        'CLIENT' : client,
        'CLIENT_ID' : CLIENT_ID,
        'USERNAME' : username,
        'PASSWORD' : password,
        'EMAIL' : email,
        'USER_HASH' : get_secret_hash(username)
    }

    resp = sign_up.sign_up(info)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": resp,
        }),
    }

def confirm_sign_up_handler(event, context):
    
    body = json.loads(event['body'])
    username = body['username']
    code = body['code']

    info = {
        'CLIENT' : client,
        'CLIENT_ID' : CLIENT_ID,
        'USERNAME' : username,
        'CODE' : code,
        'USER_HASH' : get_secret_hash(username)
    }

    resp = confirm_sign_up.confirm_sign_up(info)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": resp,
        }),
    }

def login_handler(event, context):
    print(event)
    body = json.loads(event['body'])
    username = body['username']
    password = body['password']

    info = {
        'CLIENT' : client,
        'CLIENT_ID' : CLIENT_ID,
        'POOL_ID' : POOL_ID,
        'AUTH_FLOW' : 'ADMIN_USER_PASSWORD_AUTH',
        'USERNAME' : username,
        'PASSWORD' : password,
        'USER_HASH' : get_secret_hash(username)
    }

    resp = login.login(info)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": resp,
        }),
    }
