#!/usr/bin/python2.7
import os;
import os.path;  
import sys;

home = os.getenv("HOME");

path = home + "/.haickpage";
lastmt = 0;
while 1:
    try:
        mt = os.path.getmtime(path);
        if mt > lastmt:
            f = open(path, 'r')
            lastmt=mt;
            sys.stdout.write(f.read());
            f.close();
    except OSError as e: pass;
