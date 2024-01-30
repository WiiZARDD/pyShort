import subprocess
from colors import Cl
from clear import C
from timer import W


class M:
    @staticmethod
    def m():
        print(Cl.cl("    ┏┓┓      ", Cl.G))
        print(Cl.cl("┏┓┓┏┗┓┣┓┏┓┏┓╋", Cl.G))
        print(Cl.cl("┣┛┗┫┗┛┛┗┗┛┛ ┗", Cl.G))
        print(Cl.cl("┛  ┛         ", Cl.G))
        W.w()
        print(Cl.cl("1. SHORTEN URL", Cl.G))
        print(Cl.cl("2. CREDITS    ", Cl.G))

        option = input(Cl.cl("Choose an option: ", Cl.W))
        if option == "1":
            subprocess.run(["python", "src/short.py"])
        elif option == "2":
            C.c()
            print(Cl.cl("THANK YOU FOR SHORTENING", Cl.G))
            print(Cl.cl("URL SHORTENING TOOL", Cl.G))
            print(Cl.cl("CREATED BY @WiiZARDD", Cl.W))
            print(Cl.cl("THIS IS MEANT FOR EASE OF USE", Cl.G))
            print(Cl.cl("OPEN-SOURCE FOR SKIDS, ENJOY!", Cl.G))
            W.w()
            input("PRESS ANYTHING TO RETURN TO MENU")

            M.m()
