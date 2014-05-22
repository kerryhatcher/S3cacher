import urllib
import boto
import boto.s3
from boto.s3.key import Key
import sys
import yaml
import os



#############
#AWS CONFIGS#
#############
"""
!!! WARNING !!!##
DO NOT EDIT, put settings in settings.yaml
"""

with open('settings.yaml', 'r') as f:
    doc = yaml.load(f)

AWS_ACCESS_KEY_ID = doc["AWS"]["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY = doc["AWS"]["AWS_SECRET_ACCESS_KEY"]

bucket_name = doc["AWS"]["AWS_BUCKET_NAME"]
conn = boto.connect_s3(AWS_ACCESS_KEY_ID,
            AWS_SECRET_ACCESS_KEY)

bucket = conn.create_bucket(bucket_name,
        location=boto.s3.connection.Location.DEFAULT)
#############
#AWS CONFIGS#
#############




class Cacher:
        """Upload html to s3"""
        def __init__(self):
            pass

        @staticmethod
        def upload(localfilename, inputurl):
            targeturl = urllib.urlopen(inputurl)
            localFile = open(localfilename, 'w')
            localFile.write(targeturl.read())
            localFile.close()
            #upload files
            print 'uploading %s to AWS S3 bucket %s' % \
                  (localfilename, bucket_name)

            def percent_cb(complete, total):
                sys.stdout.write('.')
                sys.stdout.flush()

            s3key = Key(bucket)
            s3key.key = localfilename
            s3key.set_contents_from_filename(localfilename,
                cb=percent_cb, num_cb=10)
            os.remove(localfilename)
