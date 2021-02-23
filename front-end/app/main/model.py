import boto3

s3 = boto3.client('s3')

def save_to_S3(filename: str, data: bytes):
    
    user = None #function to fetch username

    s3.put_object(
        ACL = 'public-read',
        Body = data,
        Bucket = '<BUCKET>',
        Key= f'{user}/{filename}'
    )