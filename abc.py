import unicornhat as unicorn
from fonct import *

unicorn.rotation(270)

O = [0, 0, 0]
W = [128, 128, 128]

a = [
[O,O,O,O,O,O],
[O,O,O,O,O,O],
[O,O,O,O,O,O],
[O,W,W,W,O,O],
[W,O,O,O,O,O],
[W,W,W,W,O,O],
[W,O,O,O,W,O],
[W,W,W,W,O,O]
]

b = [
[O,O,O,O,W,O],
[O,O,O,O,W,O],
[O,O,O,O,W,O],
[O,W,W,O,W,O],
[W,O,O,W,W,O],
[W,O,O,O,W,O],
[W,O,O,O,W,O],
[O,W,W,W,W,O]
]

c = [
[O,O,O,O,O,O],
[O,O,O,O,O,O],
[O,O,O,O,O,O],
[W,W,W,W,O,O],
[O,O,O,O,W,O],
[O,O,O,O,W,O],
[O,O,O,O,W,O],
[W,W,W,W,O,O]
]

d = [
[O,O,O,O,O,O],
[O,O,O,O,O,O],
[O,O,O,O,O,O],
[O,O,O,O,O,O],
[O,O,O,O,O,O],
[O,O,O,O,O,O],
[O,O,O,O,O,O],
[O,O,O,O,O,O]
]

Exemple = [
[O,O,O,O,O,O],
[O,O,O,O,O,O],
[O,O,O,O,O,O],
[O,O,O,O,O,O],
[O,O,O,O,O,O],
[O,O,O,O,O,O],
[O,O,O,O,O,O],
[O,O,O,O,O,O]
]

def scrol(lettre):
        alpbt = lettre
        for y in len(alpbt):
                alpbt2 = alpbt[y]
                for x in len(alpbt2):
                        alpbt[y][x].append(lettre[y][x]