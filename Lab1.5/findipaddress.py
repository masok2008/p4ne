# 5th Python Lab

import glob


pathtofiles="C:\\Users\\user\\Seafile\\p4ne_training\\config_files"
ipaddr=set()
files=glob.glob(pathtofiles+"\\*.txt")
for fn in files:
    with open(fn) as f:
        for str in f:
            if str.find("ip address ") >= 0:
                print(str)
                ii= str.find("ip address ")
                str=str[ii+11:]
                ipaddr.add(str)
for str in ipaddr:
    print(str)
