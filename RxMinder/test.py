#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 23:04:11 2019

@author: max

"""

import io
import os

os.environ[
    "GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/max/Desktop/Hackathon Fall 2019/PennApps 2019 RxMinder-49ae1b133ea3.json"

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.join(
    os.path.dirname(__file__),
    'images/IMG_2807.JPG')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file

response = client.text_detection(image=image)
retrieved_texts = response.text_annotations
document = response.full_text_annotation

print('Texts:')

texts = []

# for text in retrieved_texts:
#    print('\n"{}"'.format(text.description))
#    texts.append('\n"{}"'.format(text.description))
#    
#    
#    vertices = (['({},{})'.format(vertex.x, vertex.y)
#                for vertex in text.bounding_poly.vertices])
#
#    print('bounds: {}'.format(','.join(vertices)))

# for page in document.pages:
#    for block in page.blocks:
#        print(block.text)
#        if (feature == FeatureType.BLOCK):
#            print(block.block.bounding_box)


# %%
# print(texts[0])
print(document.text)

data = document.text.lower().replace('\n', ' ')
print(data)
# %%