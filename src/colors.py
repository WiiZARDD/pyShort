# BASIC PYTHON COLOR CLASS BY WiiZARDD
# CHECK BELOW FOR USAGE -

class Cl:
    def cl(text, cc):
        return cc + text + Cl.R

    R = '\033[0m'
    BO = '\033[1m'
    U = '\033[4m'
    B = '\033[30m'
    RE = '\033[31m'
    G = '\033[32m'
    Y = '\033[33m'
    BL = '\033[34m'
    M = '\033[35m'
    C = '\033[36m'
    W = '\033[37m'

    # EXAMPLE USAGE:
    # print(Cl.cl("Hello", Cl.BL))
    # BE SURE TO IMPORT FUNCTION FROM MODULE:
    # from colors import Cl
