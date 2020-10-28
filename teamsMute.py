#!/usr/bin/env python3

import subprocess,re
 
#finds current name of MS Teams
name = subprocess.Popen("wmctrl -l| grep 'Microsoft Teams$'|awk '{print substr($0, index($0,$4))  }'",shell=True, stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
#if it has (Meeting) in name script is run, otherwise we're no in meeting so there is no need to do this
if str(name) == "Microsoft Teams":
    subprocess.Popen("notify-send 'RESTART TEAMS teamsMute can not work'", stdout=subprocess.PIPE, shell=True)
if "(Meeting)" in name:
#saving pid of the current window
    currentlyActive = subprocess.Popen("xdotool getactivewindow",shell=True, stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
#finding pid of MS Teams    
    pid = subprocess.Popen("xdotool search --name '" + name +"'", shell=True, stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
#focusing and sending CTRL + SHIFT + M    
    subprocess.Popen("xdotool windowactivate "+ pid +" key Ctrl+Shift+M", stdout=subprocess.PIPE, shell=True)
#focusing windows that was previously active    
    subprocess.Popen("xdotool windowactivate '" + currentlyActive + "'", stdout=subprocess.PIPE, shell=True)
