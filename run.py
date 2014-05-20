#!/usr/bin/env python

import urllib
import boto, boto.s3
from boto.s3.key import Key
import sys





#############
#AWS CONFIGS#
#############

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''

bucket_name = ''
conn = boto.connect_s3(AWS_ACCESS_KEY_ID,
            AWS_SECRET_ACCESS_KEY)

bucket = conn.create_bucket(bucket_name,
        location=boto.s3.connection.Location.DEFAULT)






############
#Upload URL#   
############
InputURL = urllib.urlopen("<Input URL HERE>")
LocalFileName = "<Local File Name HERE>"
localFile = open(LocalFileName, 'w')
localFile.write(InputURL.read())
localFile.close()
#Upload File
print 'Uploading %s to Amazon S3 bucket %s' % \
       (LocalFileName, bucket_name)
def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()


ScrollingResultsKey = Key(bucket)
ScrollingResultsKey.key = LocalFileName
ScrollingResultsKey.set_contents_from_filename(LocalFileName,
        cb=percent_cb, num_cb=10)





