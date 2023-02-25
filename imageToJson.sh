#!/bin/bash

if [ ! -d './tmp' ]; then
    mkdir 'tmp/'
fi

if [ $# -gt 0 ]; then
    file_name=$1
else
    file_name="image.jpg"
fi

gcloud ml vision detect-text ${file_name} > tmp/output.json