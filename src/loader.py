# BASIC LOADER MODULE USING PYTHON

import subprocess
from colors import Cl
from clear import C
from timer import W

print(Cl.cl("    ┏┓┓      ", Cl.G))
print(Cl.cl("┏┓┓┏┗┓┣┓┏┓┏┓╋", Cl.G))
print(Cl.cl("┣┛┗┫┗┛┛┗┗┛┛ ┗", Cl.G))
print(Cl.cl("┛  ┛         ", Cl.G))

W.w()

print(Cl.cl("Created by WiiZARDD", Cl.G))
input(Cl.cl("Press ENTER to proceed", Cl.W))

C.c()
subprocess.run(['python', '../urlShortener/pyShort.py'])