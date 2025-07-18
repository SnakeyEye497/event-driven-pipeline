import boto3
import json
import os
from datetime import datetime, timezone
import csv
from io import StringIO

s3 = boto3.client('s3')
bucket = "sensor-data-bucket-swaraj"

def lambda_handler(event, context):
    today = datetime.now(timezone.utc).strftime('%Y%m%d')
    prefix = f"data/sensor-{today}"
    
    response = s3.list_objects_v2(Bucket=bucket, Prefix=prefix)
    if 'Contents' not in response:
        return {"statusCode": 200, "body": "No data to process today."}
    
    total_temp = 0
    count = 0
    device_ids = set()

    for obj in response['Contents']:
        key = obj['Key']
        file = s3.get_object(Bucket=bucket, Key=key)
        content = json.loads(file['Body'].read().decode('utf-8'))
        total_temp += content.get('temperature', 0)
        count += 1
        device_ids.add(content.get('device_id'))

    avg_temp = total_temp / count if count else 0

    # Generate CSV
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(["Date", "Total Readings", "Avg Temp", "Unique Devices"])
    writer.writerow([today, count, round(avg_temp, 2), len(device_ids)])

    report_key = f"reports/report-{today}.csv"
    s3.put_object(
        Bucket=bucket,
        Key=report_key,
        Body=output.getvalue()
    )

    return {"statusCode": 200, "body": f"Report created: {report_key}"}
