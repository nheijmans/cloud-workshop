#!/usr/bin/python3

import boto3
import json

def lambda_handler(event, context):
    print("I'm in here!")

    return {
        "statusCode": 200,
        "body": json.dumps(
            {"message": "success!"}
        )
    }
