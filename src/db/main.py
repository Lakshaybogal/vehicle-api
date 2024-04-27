import boto3
from os import getenv

dynamodb = boto3.resource('dynamodb', aws_access_key_id =  getenv("ACCESS_KEY"),
aws_secret_access_key = getenv("SECRET_KEY"), region_name='ap-south-1')

def get_db():
    return dynamodb.Table('vehicles')
