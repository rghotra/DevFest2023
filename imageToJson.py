import os, io
import sys
from google.cloud import vision
import json

if not os.path.isdir('tmp'):
    os.mkdir('tmp')
    

client = vision.ImageAnnotatorClient()

with io.open(sys.argv[1], 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)
response = client.document_text_detection(image=image)


response_json = vision.AnnotateImageResponse.to_json(response)
response = json.loads(response_json)
# response['fullTextAnnotation']['text']

with open('tmp/output.json', 'a') as f:
        json.dump(response, f)