import firebase_admin
import google-cloud-storage
from firebase_admin import credentials
from firebase_admin import storage


cred = credentials.Certificate('Key/ServiceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'pooltablerugs.appspot.com'
})


def upload_blob(source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    bucket = storage.bucket()
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))
# 'bucket' is an object defined in the google-cloud-storage Python library.
# See https://googlecloudplatform.github.io/google-cloud-python/latest/storage/buckets.html
# for more details.

upload_blob('Uploaded/godlist.json', 'test')