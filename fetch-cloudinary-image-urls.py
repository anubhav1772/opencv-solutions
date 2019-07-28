# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 00:05:37 2019
@author: anubhav singh
Get urls of images inside a folder in cloudinary storage
"""

import urllib.request as req 
import cloudinary
import cv2

cloudinary.config(
  cloud_name = 'YOUR-CLOUD-NAME',  
  api_key = 'YOUR-CLOUDINARY-API-KEY',  
  api_secret = 'YOUR-CLOUDINARY-API-SECRET-KEY'  
)

for i in cloudinary.Search().expression("folder:your_folder_name").execute()['resources']:
    image_url = cloudinary.CloudinaryImage(i['url']).build_url()
    image_ext = image_url.split('/')[8].split('.')[1]
    req.urlretrieve(image_url, "filename"+image_ext) 
    img = cv2.imread('filename.jpg')
    # other logics for image manifpulation