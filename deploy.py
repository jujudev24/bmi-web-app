import boto3
import os
from dotenv import load_dotenv  # Import dotenv

# Load environment variables from .env
load_dotenv()

# S3 Configuration
BUCKET_NAME = "bmi-web-app"  # S3 Bucket name
LOCAL_FOLDER = "build"  # Folder React build
S3_FOLDER = ""  # Root folder in S3

def upload_folder_to_s3(local_folder, bucket_name, s3_folder):
    # Check if the local folder exists
    if not os.path.exists(local_folder):
        print(f"Error: Local folder '{local_folder}' does not exist.")
        exit(1)

    s3_client = boto3.client(
        's3',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        aws_session_token=os.getenv('AWS_SESSION_TOKEN')
    )

    for root, dirs, files in os.walk(local_folder): 
        for file in files:
            local_file_path = os.path.join(root, file)
            s3_file_path = os.path.join(
                s3_folder, os.path.relpath(local_file_path, local_folder)
            ).replace("\\", "/")  # Support for Windows paths
            print(f"Uploading {local_file_path} to s3://{bucket_name}/{s3_file_path}")
            s3_client.upload_file(local_file_path, bucket_name, s3_file_path)

if __name__ == "__main__":
    upload_folder_to_s3(LOCAL_FOLDER, BUCKET_NAME, S3_FOLDER)
