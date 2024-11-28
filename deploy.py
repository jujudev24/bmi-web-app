import boto3
import os
from dotenv import load_dotenv  # Import dotenv

# Load environment variables dari file .env
load_dotenv()

# Konstanta untuk S3
BUCKET_NAME = "bmi-web-app"  # Nama bucket S3
LOCAL_FOLDER = "build"  # Folder React hasil build
S3_FOLDER = ""  # Root folder di S3

def upload_folder_to_s3(local_folder, bucket_name, s3_folder):
    s3_client = boto3.client(
        's3',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),  # Dapatkan dari .env
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),  # Dapatkan dari .env
        aws_session_token=os.getenv('AWS_SESSION_TOKEN')  # Dapatkan dari .env
    )
    for root, dirs, files in os.walk(local_folder):
        for file in files:
            local_file_path = os.path.join(root, file)
            s3_file_path = os.path.join(
                s3_folder, os.path.relpath(local_file_path, local_folder)
            ).replace("\\", "/")  # Support untuk Windows
            print(f"Uploading {local_file_path} to s3://{bucket_name}/{s3_file_path}")
            s3_client.upload_file(local_file_path, bucket_name, s3_file_path)

if __name__ == "__main__":
    upload_folder_to_s3(LOCAL_FOLDER, BUCKET_NAME, S3_FOLDER)
