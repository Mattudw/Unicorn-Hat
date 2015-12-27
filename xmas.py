import unicornhat as unicorn
from fonct import *

X = [0, 127, 0]         #Green
O = [0, 0, 0]           #Black
W = [127, 127, 127]     #White
B = [90, 40, 0]         #Brown
U = [0, 0, 128]         #Blue
R = [128, 0, 0]         #Red
J = [252, 210, 28]      #Yellow

unicorn.rotation(270)

treeOne = [
[O,O,O,J,O,O,O],
[O,O,O,X,O,O,O],
[O,O,X,X,X,O,O],
[O,X,X,X,X,X,O],
[O,O,X,X,X,O,O],
[O,X,X,X,X,X,O],
[X,X,X,X,X,X,X],
[O,O,O,B,O,O,O]]

treeTwo = [
[O,O,O,J,O,O,O],
[O,O,O,X,O,O,O],
[O,O,W,X,X,O,O],
[O,W,X,X,W,X,O],
[O,O,W,X,X,O,O],
[O,X,X,W,W,X,O],
[X,X,W,X,X,X,W],
[O,O,O,B,O,O,O]]

treeThree = [
[O,O,O,J,O,O,O],
[O,O,O,U,O,O,O],
[O,O,X,X,R,O,O],
[O,X,R,X,X,X,O],
[O,O,X,X,U,O,O],
[O,X,U,X,X,R,O],
[U,X,X,X,R,X,X],
[O,O,O,B,O,O,O]]

while True :
        setPixel(treeOne)
        setPixel(treeTwo)
        setPixel(treeThree)
