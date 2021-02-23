import boto3
import requests

s3 = boto3.client('s3')

endpoint = None # Api-GW endpoint for fetching image records

def save_to_S3(filename: str, data: bytes):
    
    user = None #function to fetch username

    s3.put_object(
        ACL = 'public-read',
        Body = data,
        Bucket = '<BUCKET>',
        Key= f'{user}/{filename}'
    )

def get_all_images():
    
    images = requests.get(f'{endpoint}/images')
    return images

def get_image_by_id(id: int):
    
    image = requests.get(f'{endpoint}/image/{id}')
    return image

def get_image_by_tag(tag: str):
    
    images = requests.get(f'{endpoint}/search?tag={tag}')
    return images