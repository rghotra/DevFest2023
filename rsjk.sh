#!/bin/bash

file_name=$1

# rm -rf tmp
export GOOGLE_APPLICATION_CREDENTIALS="gcloud_account_key.json"

python3 imageToJson.py $file_name
python3 jsonToCode.py
./runCode.sh

python3 GPT.py

cat tmp/summary.txt >> tmp/code_output.txt

echo "Output stored in tmp/code_output.txt"
