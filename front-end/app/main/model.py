import os

import boto3
import requests

from app.auth.model import get_user

s3 = boto3.client('s3')

endpoint = os.environ['MAIN_ENDPOINT']

def save_to_S3(filename: str, data: bytes):
    
    user = get_user()

    if not user:
        return False

    s3.put_object(
        ACL = 'public-read',
        Body = data,
        Bucket = '<BUCKET>',
        Key= f'{user}/{filename}'
    )
    
    return True

def get_all_images():
    
    images = requests.get(f'{endpoint}/images').json()
    return images['data']

def get_image_by_id(id: int):
    
    image = requests.get(f'{endpoint}/image/{id}').json()
    return image['data']

def get_image_by_tag(tag: str):
    
    images = requests.get(f'{endpoint}/search?tag={tag}').json()
    return images['data']