#!/bin/bash

file_name=$1

rm -rf tmp

./imageToJson.sh $file_name
python3 jsonToCode.py
./runCode.sh

echo "Output stored in tmp/code_output.txt"