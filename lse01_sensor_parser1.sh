#!/bin/sh
read -p "Please enter the payload : " payload
java -jar lorawanparser.jar -LSE01 -X $payload
