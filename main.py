import os
import subprocess
import re
from datetime import datetime
import pathlib
basedir = '/home'
now = datetime.now()
time = now.strftime('%d-%m-%Y_%H:%M:%S')
currentdir = basedir+"/"+time+"/"

# ip = os.system("hostname -I | awk '{print $1;exit}'")
def scan(ip):
    if ip is None:
        ip = subprocess.check_output("ip -o -f inet addr show | awk '/scope global/ {print $4}'", shell=True).decode()
        print("SCAN STARTED ON "+ip)
    command = "nmap -sn " + ip
    scannet = subprocess.check_output(command, shell=True).decode()
    ips = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", scannet)

    return ips


def write(iplist):
    pathlib.Path(currentdir).mkdir(parents=True, exist_ok=True)
    filename = currentdir + "iplist"
    f = open(filename, "a")
    for item in iplist:
        f.write("%s\n" % item)
    f.close()

# isIp = re.fullmatch(r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b",ip)


def choice():
    loop = True
    while loop:
        inputUser = input("Saissez une ip VALIDE ou ecrivez auto pour une détection automatique : \n")
        ipsplited = re.findall(
            r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",
            inputUser)
        print(inputUser)

        if inputUser == 'auto':
            print(inputUser)
            return 'auto'
        elif ipsplited is not None:
            for truc in ipsplited:
                for i in range(0, 3):
                    if truc[i] == '01' or truc[i] == '00' or truc[i] == '0':
                        choice()
                    else:
                        mask = input("Saissez le mask correspondant au reseau à scanner : \n")
                        if 30 > int(mask) > 0:
                            mask = "/" + mask
                            network = ipsplited.append(mask)
                            return network
                        else:
                            choice()


choice = choice()
if choice == 'auto':
    print("STARTING AUTO SCAN")
    write(scan(None))
else:
    print("STARTING SCAN ON SPECIFED IP")
    write(scan(None))




