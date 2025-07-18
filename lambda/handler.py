import json
import boto3
import os
from datetime import datetime

s3 = boto3.client('s3')
bucket = "sensor-data-bucket-swaraj"  # or use os.environ.get('BUCKET_NAME')

def lambda_handler(event, context):
    try:
        print("Incoming event:", event)

        if 'body' not in event or event['body'] is None:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Missing request body'})
            }

        body = json.loads(event['body'])
        timestamp = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
        key = f"data/sensor-{timestamp}.json"

        s3.put_object(
            Bucket=bucket,
            Key=key,
            Body=json.dumps(body)
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Data stored successfully'})
        }

    except Exception as e:
        print("Error:", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
