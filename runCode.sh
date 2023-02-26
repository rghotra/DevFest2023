#!/bin/bash

loc="tmp"
file_name="Code.java"

javac "${loc}/${file_name}" 2>&1 | tee -a "${loc}/code_output.txt"

if [ -s "${loc}/code_output.txt" ]; then
    exit 1
fi

java ${loc}.${file_name%.*} 2>&1 | tee -a "${loc}/code_output.txt"