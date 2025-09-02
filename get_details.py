import boto3
import csv
from datetime import datetime
import os

# Initialize IAM client
client = boto3.client('iam')

def list_iam_users():
    try:
        # Get account ID for filename
        sts_client = boto3.client('sts')
        account_id = sts_client.get_caller_identity()['Account']
        
        # Create CSV filename
        csv_filename = f"iam_users_{account_id}.csv"
        
        # List all IAM users
        users = client.list_users()['Users']
        
        # Create CSV file
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Account_ID', 'User_Name', 'Access_Key_ID', 'Created_Date', 'Last_Accessed']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write header
            writer.writeheader()
            
            # Write user data
            for user in users:
                access_keys = client.list_access_keys(UserName=user['UserName'])['AccessKeyMetadata']
                for key in access_keys:
                    last_accessed = key.get('LastUsedDate', 'Never')
                    if last_accessed != 'Never':
                        last_accessed = last_accessed.strftime('%Y-%m-%d %H:%M:%S')
                    
                    writer.writerow({
                        'Account_ID': account_id,
                        'User_Name': user['UserName'],
                        'Access_Key_ID': key['AccessKeyId'],
                        'Created_Date': key['CreateDate'].strftime('%Y-%m-%d %H:%M:%S'),
                        'Last_Accessed': last_accessed
                    })
        
        print(f"CSV file created: {csv_filename}")
        print(f"Found {len(users)} users with {sum(len(client.list_access_keys(UserName=user['UserName'])['AccessKeyMetadata']) for user in users)} access keys")
        
    except Exception as e:
        print(f"Error: {e}")

list_iam_users()