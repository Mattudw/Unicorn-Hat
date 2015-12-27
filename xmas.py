import unicornhat as unicorn
import time

X = [0, 127, 0]         #Green
O = [0, 0, 0]           #Black
W = [127, 127, 127]     #White
B = [90, 40, 0]         #Brown
U = [0, 0, 128]         #Blue
R = [128, 0, 0]         #Red
J = [252, 210, 28]      #Yellow

unicorn.rotation(270)

def brightness(): #Brightness in fonction of the local time
        currentHour = time.strftime("%H")
        if currentHour == 23 or currentHour <= 07:
                unicorn.brightness(0.05)
                print currentHour
        else:
                unicorn.brightness(0.2)

def setPixel(liste):
        for y in range(8):
                for x in range(8):
                        a, b, c = liste[y][x][0], liste[y][x][1], liste[y][x][2]
                        unicorn.set_pixel(y, x, a, b, c)
        unicorn.show()
        time.sleep(0.5)
        brightness()


treeOne = [[O,O,O,J,O,O,O,O],[O,O,O,X,O,O,O,O],[O,O,X,X,X,O,O,O],[O,X,X,X,X,X,O,O],[O,O,X,X,X,O,O,O],[O,X,X,X,X,X,O,O],[X,X,X,X,X,X,X,O],[O,O,O,B,O,O,O,O]]

treeTwo = [[O,O,O,J,O,O,O,O],[O,O,O,X,O,O,O,O],[O,O,W,X,X,O,O,O],[O,W,X,X,W,X,O,O],[O,O,W,X,X,O,O,O],[O,X,X,W,W,X,O,O],[X,X,W,X,X,X,W,O],[O,O,O,B,O,O,O,O]]

treeThree = [[O,O,O,J,O,O,O,O],[O,O,O,U,O,O,O,O],[O,O,X,X,R,O,O,O],[O,X,R,X,X,X,O,O],[O,O,X,X,U,O,O,O],[O,X,U,X,X,R,O,O],[U,X,X,X,R,X,X,O],[O,O,O,B,O,O,O,O]]

brightness()

while True :
        setPixel(treeOne)
        setPixel(treeTwo)
        setPixel(treeThree)
