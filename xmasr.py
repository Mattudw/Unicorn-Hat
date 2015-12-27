import unicornhat as unicorn
import time
from random import *

R, O, Y, G, B, V = [255, 51, 51], [255, 153, 51], [255, 255, 51], [153, 255, 51], [51, 153, 255], [153, 51, 255]
light = [R, O, B, V]

unicorn.rotation(270)

def brightness(): #Brightness in fonction of the local time
        currentHour = time.strftime("%H")
        if currentHour == 23 or currentHour <= 07:
                unicorn.brightness(0.05)
        else:
                unicorn.brightness(0.2)
X = [1]
Y = [2]
O = [0]

while True :

        tree = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,Y,O,O,O,O],
        [O,O,Y,X,Y,O,O,O],
        [O,Y,X,Y,X,Y,O,O],
        [O,O,Y,X,Y,O,O,O],
        [O,Y,X,Y,X,Y,O,O],
        [Y,X,Y,X,Y,X,Y,O],
        [O,O,O,O,O,O,O,O]
        ]

        for y in range(8):
                for x in range(8):
                        if tree[y][x][0] == 2:
                                unicorn.set_pixel(y, x, G[0], G[1], G[2])
                        elif tree[y][x][0] == 1:
                                color = choice(light)
                                unicorn.set_pixel(y, x, color[0], color[1], color[2])
                        else:
                                unicorn.set_pixel(y, x, 0, 0, 0)

        unicorn.set_pixel(0, 3, 255, 255, 51)   #Yellow/Top
        unicorn.set_pixel(7, 3, 200, 140, 51)   #Brown/Botton
        brightness()
        unicorn.show()
        time.sleep(0.5)
