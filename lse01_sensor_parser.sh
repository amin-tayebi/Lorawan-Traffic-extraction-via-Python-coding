#!/bin/sh
python payload.py
java -jar lorawanparser.jar -hex output.txt > outputfinal.txt
