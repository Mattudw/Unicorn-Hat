import unicornhat as unicorn
from time import sleep

unicorn.rotation(270)

def setPixel(liste):
        for y in range(8):
                for x in range(8):
                        a = liste[y][x][0]
                        b = liste[y][x][1]
                        c = liste[y][x][2]
                        unicorn.set_pixel(y, x, a, b, c)
        unicorn.show()
        sleep(0.5)

def signConstructor(y,x,color):
        unicorn.set_pixel(x,y,color[0],color[1],color[2])
        unicorn.set_pixel(x,y+1,color[0],color[1],color[2])
        unicorn.set_pixel(x+1,y,color[0],color[1],color[2])
        unicorn.set_pixel(x+1,y+1,color[0],color[1],color[2])
        unicorn.show()

def signVerificator(chaine):
        listComb = [["C","B","A"],["1","2","3"]]
        listXY = []
        for i in listComb:
                for j in i:
                        if select[listComb.index(i):listComb.index(i)+1] == j:
                                listXY.append(i.index(j)*3)
        return listXY

O = [0, 0, 0]           #Black
W = [128, 128, 128]     #White
B = [0, 0, 128]         #Blue
R = [128, 0, 0]         #Red
J = [252, 210, 28]      #Yellow

grilleMorpion = [
[O,O,W,O,O,W,O,O],
[O,O,W,O,O,W,O,O],
[W,W,W,W,W,W,W,W],
[O,O,W,O,O,W,O,O],
[O,O,W,O,O,W,O,O],
[W,W,W,W,W,W,W,W],
[O,O,W,O,O,W,O,O],
[O,O,W,O,O,W,O,O]
]

tour = R
setPixel(grilleMorpion)

while True:
        for i in range(9):
                actualColor = (255,255,255)
                while actualColor != (0,0,0):
                        select = raw_input("Selectionner une case (A ou B ou C et 1 ou 2 ou 3) :\n")
                        listeXY = signVerificator(select)
                        actualColor = unicorn.get_pixel(listeXY[1],listeXY[0])
                        if actualColor == (0,0,0):
                                signConstructor(listeXY[0],listeXY[1],tour)
                        else:
                                print("Deja joue\n\n")

                if tour == R:
                        tour = B
                else:
                        tour = R
