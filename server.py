import os
import subprocess
import base64
import urllib.request as urq
import shutil

from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/process-file', methods=['POST'])
def process_file():
    print("received")
    print(request.json)
    data = request.json.get('data')
    
    print(data != '');

    if not data:
        return jsonify({'error': 'No data provided.'}), 400
    
    temp_file = 'tmp/file.jpg'
    if os.path.isdir('tmp'):
        shutil.rmtree('tmp')
    os.mkdir('tmp')
        
    response = urq.urlopen(data)
    with open(temp_file, 'wb') as f:
        f.write(response.file.read())

    # Call the bash script with the temporary file as input
    subprocess.run(['./rsjk.sh', temp_file])

    # Convert the output to a string and remove any trailing newlines
    
    with open('tmp/code_output.txt') as handle:
        output = ('\n'.join(handle.readlines())).rstrip()
        # output = output.decode('utf-8').rstrip()

    # Return the output as a JSON response
    return jsonify({'output': output}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
