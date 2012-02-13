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
            cont = f.read();
            lastmt=mt;
            sys.stdout.write(cont);
            sys.stdout.flush();
            f.close();
    except OSError as e:
        print e;
