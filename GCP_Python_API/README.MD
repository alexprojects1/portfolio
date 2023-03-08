# GCP Python API - Create bucket, upload to bucket, download from bucket

### Steps:

+ Enable API
  + API and Services 
  + Select Cloud Storage API and enable 
+ Enable credentials
  + Give the  credentials a name
  + Cloud storage - Owner Role 
  + Click on the service account you just created and download the JSON key file
+ Python:
  + pip install --upgrade google-cloud-storage
+ GCP
  + Create a new bucket 
  + Upload to bucket
  + Download from bucket





## Quick Command Reference:
```
pip install --upgrade google-cloud-storage

```

## Errors Encountered:

+ Note bucket.location is depricated

Assignment to 'Bucket.location' is deprecated, as it is only valid before the bucket is created. Instead, pass the location to `Bucket.create

https://stackoverflow.com/questions/54992263/creating-bucket-in-google-cloud-storage-in-custom-location

+ Note use unique google storage bucket name
google.api_core.exceptions.Conflict: 409 POST https://storage.googleapis.com/storage/v1/b?project=tranquil-lore-340713&prettyPrint=false: You already own this bucket. Please select another name.

```
import os
from google.cloud import storage #storage module

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'cloudstorage2_service_key_GCP.json'  #locate the service account file

storage_client = storage.Client()  #create storage client instance

bucket_name = '<bucket name'

"""
Create New Bucket
"""
bucket_name = 'data_bucket_20220208_version2'
bucket = storage_client.bucket(bucket_name)
bucket.create(location='US')

"""
Print Bucket Detail
"""
vars(my_bucket)   #vars function

"""
Accessing a specific bucket
"""

my_bucket = storage_client.get_bucket('data_bucket_20220208_version2')

"""
Upload Files
"""

#Upload file to bucket function

def upload_to_bucket(blob_name, file_path, bucket_name):
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        block.upload_from_filename(file_path)
        return True
    except Exception as e:
        print(e)
        return False
    
file_path = 'E:\\2022_GCP\\Data Files'
upload_to_bucket('test file', os.path.join(file_path, 'test.csv', 'data_bucket_20220208_version2')
"""
Download Files
"""
#To be continued

# Credit to tutorial: https://www.youtube.com/watch?v=pEbL_TT9cHg&t=659s

```