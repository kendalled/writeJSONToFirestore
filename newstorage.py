import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import datetime

# Fetch the service account key JSON file contents
cred = credentials.Certificate('Key/ServiceAccountKey.json')

# Initialize the app with a service account, granting admin privileges
app = firebase_admin.initialize_app(cred, {
    'storageBucket': 'pooltablerugs.appspot.com',
}, name='storage')

bucket = storage.bucket(app=app)
blob = bucket.blob("Fold/a177-fold.jpg")

print(blob.generate_signed_url(datetime.timedelta(seconds=300), method='GET'))