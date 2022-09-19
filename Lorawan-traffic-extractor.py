import re
import sys
#import subprocess
pattern  = re.compile("Receive")
sys.stdout = open("output.txt", "w")
for line in open("system.log"):
    for match in re.finditer(pattern, line):
        alist = line.split(":")
        t = alist[-1]
        print(t.replace('\n', ''))
#subprocess.call(['java', '-jar', '${PWD}/lorawanparser.jar' ' -hex' ' output.txt'])
