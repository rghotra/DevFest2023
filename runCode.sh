#!/bin/bash

loc="tmp"
file_name="Code.java"

javac -d "$loc" "${loc}/${file_name}"
java -classpath "$loc" ${loc}.${file_name%.*} | tee "${loc}/code_output.txt"