from requests_aws4auth import AWS4Auth
import boto3
import requests
import time
import json
import sys


def upload_to_s3(file_name, bucket_name, s3_key):
    """Uploads file to S3"""
    s3 = boto3.client('s3')
    try:
        s3.upload_file(file_name, bucket_name, s3_key)
        print('Upload successful')
        return True
    except FileNotFoundError:
        sys.exit('File not found. Make sure you specified the correct file path.')
upload_to_s3('CV_Duc-Hong.pdf','personalbucket-hongnghiaduc121200', 'short-key123')