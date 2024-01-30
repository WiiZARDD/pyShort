import sys
import subprocess
from src.timer import W
from src.colors import Cl

print(Cl.cl("> Loading ...", Cl.G))
W.w()
print(Cl.cl("Booting requirements,  this might take a minute...", Cl.RE))
W.w()
subprocess.run(['python', 'src/verify.py'])
