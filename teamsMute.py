#!/usr/bin/env python3

import subprocess,re
 
#Listing possible PIDs of MS Teams
#p = process
p = subprocess.Popen("xdotool search \'Teams$\'", stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
 
#converting output to string and cutting unnecesary parts 
#we end up left with clen list of possible pids
output = str(output)
print(output)
output = output.replace('\'','')
output = output.replace('b','')
pids = output.split("\\n",)
del pids[-1]
print("Command output : ", pids)

for pid in pids :
    print(pid)
    #looking for window that hasn't parameter _NET_WM_STATE_SKIP_TASKBAR
    
    p = subprocess.Popen("xprop -id "+ pid +"|grep _NET_WM_STATE_SKIP_TASKBAR", stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    output = str(output)
    output = output.replace('\'','')
    output = output.replace('b','')
    print(output)
    #if there is parameter _NET_WM_STATE_SKIP_TASKBAR it means that teams is closed so we don't try to send ctrl+shift+m to it
    if output == '':
        print('tried')
        subprocess.Popen("xdotool windowactivate --sync "+ pid +" key Ctrl+Shift+M", stdout=subprocess.PIPE, shell=True)