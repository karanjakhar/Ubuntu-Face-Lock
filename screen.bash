#!/usr/bin/env bash
dbus-monitor --session "type='signal',interface='org.gnome.ScreenSaver',member='ActiveChanged'" | while read line ; do 
        if [ x"$(echo "$line" | grep 'boolean true')" != x ] ; then 
               python3 face_unlock_kj_ub.py
               
        fi
done
