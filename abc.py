import unicornhat as unicorn
import time
from fonct import *

unicorn.rotation(270)

def scrol(lettre):
        alpbt = lettre
        for y in len(alpbt):
                alpbt2 = alpbt[y]
                for x in len(alpbt2):
                        alpbt[y][x].append(lettre[y][x]
