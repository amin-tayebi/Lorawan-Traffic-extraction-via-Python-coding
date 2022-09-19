# It is able to parse any system log file.

It looks for "Receive" word you can replace it with any word you are searching. 

Finaly separate the payload which is located after ":" and export all of them in a separated rows in a output.txt file.

# It can be used also in Lorawan Traffic extraction.

By analysing Lorawan traffic, main payload of the whole packets (which has been sent by sensors e.g. Humidity) extracted from the LOG file of the Gateway sepatated and decoded using a python script.

# shell files are including a java based lorawan_parser to decode the payload of specific sensor (LSE01 soil moixture).
