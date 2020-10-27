#!/usr/bin/env python3

import subprocess,re
 
#finds current name of MS Teams
name = subprocess.Popen("wmctrl -l| grep 'Microsoft Teams$'|awk '{print substr($0, index($0,$4))  }'",shell=True, stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
print(name)
#if it has (Meeting) in name script is run, otherwise we're no in meeting so there is no need to do this
if "(Meeting)" in name:
#save pid of current window
    currentlyActive = subprocess.Popen("xdotool getactivewindow",shell=True, stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
    print(currentlyActive)
#finding pid of MS Teams    
    pid = subprocess.Popen("xdotool search --name '" + name +"'", shell=True, stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
    print(pid)
#facusing and sending CTRL + SHIFT + M    
    subprocess.Popen("xdotool windowactivate "+ pid +" key Ctrl+Shift+M", stdout=subprocess.PIPE, shell=True)
#focusing windows that was previously active    
    subprocess.Popen("xdotool windowactivate '" + currentlyActive + "'", stdout=subprocess.PIPE, shell=True)
