#!/bin/bash

loc="tmp"
file_name="Code.java"

javac "${loc}/${file_name}"
java ${loc}.${file_name%.*} | tee "${loc}/code_output.txt"