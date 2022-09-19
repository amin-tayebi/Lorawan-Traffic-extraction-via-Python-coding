#!/bin/sh
python payload.py
java -jar /home/jeem/Downloads/program/lorawanparser.jar -hex output.txt > outputfinal.txt
