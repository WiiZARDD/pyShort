import subprocess
from timer import W
from colors import Cl
from clear import C
from license import L

v = L.l()

print(Cl.cl("┓┏┏┓┳┓┳┏┓┓┏           ", Cl.G))
print(Cl.cl("┃┃┣ ┣┫┃┣ ┗┫ - WiiZARDD", Cl.G))
print(Cl.cl("┗┛┗┛┛┗┻┻ ┗┛           ", Cl.G))
print(Cl.cl("  Skids not allowed   ", Cl.G))
print(" ")
W.w()

a = input("ENTER LICENSE: ")
if a == v:
    C.c()
    print("Loading pyShort!")
    W.w()
    C.c()
    print("Initializing pyShort Modules! Almost finished.")
    C.c()
    subprocess.run(['python', 'src/loader.py'])
else:
    print(Cl.cl("INVALID LICENSE CODE", Cl.RE))
