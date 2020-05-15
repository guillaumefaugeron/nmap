import subprocess
import re
from datetime import datetime
import pathlib
basedir = '/home'
now = datetime.now()
time = now.strftime('%d-%m-%Y_%H:%M:%S')
currentdir = basedir+"/"+time+"/"

ip = subprocess.check_output("ip -o -f inet addr show | awk '/scope global/ {print $4}'", shell=True).decode()
print("SCAN STARTED ON " + ip)


def write(iplist):
    pathlib.Path(currentdir).mkdir(parents=True, exist_ok=True)
    filename = currentdir + "iplist"
    f = open(filename, "a")
    for item in iplist:
        f.write("%s\n" % item)
    f.close()
