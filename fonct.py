import unicornhat as unicorn
import time

def brightness(): #Brightness in fonction of the local time
        currentHour = time.strftime("%H")
        if currentHour == 23 or currentHour <= 07:
                unicorn.brightness(0.05)
                print currentHour
        else:
                unicorn.brightness(0.2)

def setPixel(liste):
        for y in range(len(liste)):
                for x in range(len(liste[y])):
                        a, b, c = liste[y][x][0], liste[y][x][1], liste[y][x][2]
                        unicorn.set_pixel(y, x, a, b, c)
        brightness()
        unicorn.show()
        time.sleep(0.5)
