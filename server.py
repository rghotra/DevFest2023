import os
import subprocess
import base64

from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/process-file', methods=['POST'])
def process_file():
    blob = request.json.get('blob')

    if not blob:
        return jsonify({'error': 'No blob provided.'}), 400

    # Decode the base64-encoded blob to binary data
    file_data = base64.b64decode(blob)

    # Save the binary data to a temporary file
    temp_file = 'tmp/file.tmp'
    with open(temp_file, 'wb') as f:
        f.write(file_data)

    # Call the bash script with the temporary file as input
    subprocess.run(['./rsjk.sh', temp_file])

    # Convert the output to a string and remove any trailing newlines
    
    with open('tmp/code_output.txt') as handle:
        output = ('\n'.join(handle.readlines())).decode('utf-8').rstrip()
        # output = output.decode('utf-8').rstrip()

    # Return the output as a JSON response
    return jsonify({'output': output}), 200


if __name__ == '__main__':
    app.run(debug=True)