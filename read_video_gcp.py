# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 09:43:10 2019
@author: anubhav singh

Below code reads a video file stored on google cloud platform(google storage) using opencv.

Library needs to be installed:
    1. firebase_admin: pip install firebase_admin
    
Stackoverflow Link: https://stackoverflow.com/questions/57232521/how-to-read-video-from-google-cloud-storage-without-downloading-it-using-video/57233589#57233589

"""

import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import datetime

import urllib.request as req
import cv2

cred = credentials.Certificate('path\to\gcp-credentials-file.json')
app = firebase_admin.initialize_app(cred, {'storageBucket': 'cnc-designs.appspot.com'}, name='storage')
bucket = storage.bucket(app=app)
    
def generate_image_url(blob_path):
    """ generate signed URL of an image stored on firebase storage. """                                                        
    blob = bucket.blob(blob_path) 
    return blob.generate_signed_url(datetime.timedelta(seconds=300), method='GET')


url = generate_image_url('sample1.mp4')
req.urlretrieve(url, "sample1.mp4")
cap = cv2.VideoCapture('sample1.mp4')

if cap.isOpened():
    print ("File Can be Opened")
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        #print cap.isOpened(), ret
        if frame is not None:
            # Display the resulting frame
            cv2.imshow('Sample1',frame)
            # Press q to close the video windows before it ends if you want
            if cv2.waitKey(22) & 0xFF == ord('q'):
                break
        else:
            print("Frame is None")
            break
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    print ("Video stop")
else:
    print("Not Working")