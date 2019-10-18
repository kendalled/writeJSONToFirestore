# Write data from json file to firestore in batches
# Python 3.7.4
# Kendall Jackson

import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore
import json
from glob import glob
import shutil
import time

# Credentials and Firestore Reference
cred = credentials.Certificate('Key/ServiceAccountKey.json')
app = firebase_admin.initialize_app(cred)

db = firestore.client()
doc_ref = db.collection(u'Rugs')