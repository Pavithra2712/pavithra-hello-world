import boto3
import botocore
import json
import logging
logging.getLogger().setLevel(logging.INFO)
s3 = boto3.resource('s3')
BUCKET_NAME = 'dev-days-test' # replace with your bucket name
KEY = 'hello.txt' # replace with your object key

def lambda_handler(event, context):
    # TODO implement
    logging.info(event)
    
    
    try:
        temp_file = "/tmp/hello_local.txt"
        s3.Bucket(BUCKET_NAME).download_file(KEY, temp_file)
        file = open(temp_file, "r")
        return {
         'statusCode': 200,
         'body': file.read
        }
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise
    
