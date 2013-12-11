#!/usr/bin/env python2.7


import os
import boto.s3

conn = boto.connect_s3()

def get_region():
	# Gives the user a list of the current S3 locations
	from boto.s3.connection import Location
	print '\n'.join(i for i in dir(Location) if i[0].isupper())

def new_bucket(bucket_name, loc):
	# Create a new bucket, in a specific location
	from boto.s3.connection import Location
	conn.create_bucket(bucket_name, location='Location.%s' %loc) #this line isn't working

def upload_data():
	#upload all files in current working directory to S3 bucket
	from boto.s3.key import Key
	k = Key(new_bucket)
	for root, dirs, files in os.walk(".", topdown=True):
		    for name in files:
		    	k.key = (os.path.join(root, name)[2:])
		        k.set_contents_from_filename(k.key)

