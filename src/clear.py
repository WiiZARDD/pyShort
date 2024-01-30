import os


class C:
    @staticmethod
    def c():
        os.system('cls' if os.name == 'nt' else 'clear')
