import unicornhat as unicorn
import time

G = [0, 255, 0]         #Green
B = [0, 0, 255]         #Blue
R = [255, 0, 0]         #Red
Y = [255, 255, 0]       #Yellow
C = [0, 255, 255]       #Cyan
M = [255, 0 , 255]      #Magenta
O = [255, 127 , 0]      #Orange
T = [0, 127, 255]       #Turquoise

def setPixel(liste):
        for y in range(8):
                for x in range(8):
                        a = liste[y][x][0]
                        b = liste[y][x][1]
                        c = liste[y][x][2]
                        unicorn.set_pixel(y, x, a, b, c)
        unicorn.show()
        time.sleep(0.1)

def scroll(liste,pas = 1):
    LE = len(liste)-1
    for i in range(pas):
        liste = [liste[LE]]+liste[0:LE]
    return liste

ArcEnCiel = [
[B,M,R,O,Y,G,C,T],
[B,M,R,O,Y,G,C,T],
[B,M,R,O,Y,G,C,T],
[B,M,R,O,Y,G,C,T],
[B,M,R,O,Y,G,C,T],
[B,M,R,O,Y,G,C,T],
[B,M,R,O,Y,G,C,T],
[B,M,R,O,Y,G,C,T]]

while True:
    setPixel(ArcEnCiel)
    ArcEnCielt = ArcEnCiel
    ArcEnCiel = []
    for i in ArcEnCielt:
          ArcEnCiel.append(scroll(i))
