#pip install google-cloud-storage
from google.cloud import storage
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/to/your/credentials.json'

bucket_name = 'test-bucket-1'

storage_client = storage.Client()

#create bucket
bucket = storage_client.bucket(bucket_name)
bucket.location = 'europe-west1'
storage_client.create_bucket(bucket)

#get bucket
bucket = storage_client.get_bucket(bucket_name)
vars(bucket)

#upload
url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2019-01.csv.gz'
output_csv = 'yellow_tripdata_2019-01.csv'
os.system(f'wget {url} -O /tmp/{output_csv}.gz')
os.system(f'gunzip /tmp/{output_csv}.gz')
try:
    blob = bucket.blob(output_csv)
    blob.upload_from_file_name(f'/tmp/{output_csv}')
except Exception as e:
    print(e)

