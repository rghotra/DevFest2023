import os
import subprocess
import base64
import urllib.request as urq
import shutil
import json

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin


"""
app = Flask(__name__, template_folder='website', static_folder='website/css')

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file uploaded'

    file = request.files['file']

    if file.filename == '':
        return 'No file selected'

    if file:
        file.save(file.filename)
        return 'File uploaded successfully'
"""

app = Flask(__name__)
cors = CORS(app)
# app.config['CORS_HEADER'] = 'Content-Type'


@app.route('/process-file', methods=['POST'])
# @cross_origin()
def process_file():
    print("Request Received")
    
    data = json.loads(request.data)['data']

    print("Loaded json")
    
    if not data:
        return jsonify({'output': 'No data provided.'}), 400
    
    temp_file = 'tmp/file.jpg'
    if os.path.isdir('tmp'):
        shutil.rmtree('tmp')
    os.mkdir('tmp')
    
    print("Set-up directories")
        
    response = urq.urlopen(data)
    with open(temp_file, 'wb') as f:
        f.write(response.file.read())
        
    print("Decoded image")

    # Call the bash script with the temporary file as input
    subprocess.run(['./rsjk.sh', temp_file])

    # Convert the output to a string and remove any trailing newlines
    
    with open('tmp/code_output.txt') as handle:
        output = ('\n'.join(handle.readlines())).rstrip()
        # output = output.decode('utf-8').rstrip()

    # Return the output as a JSON response
    return jsonify({'output': output}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=int(os.environ.get("PORT", 8080)))
