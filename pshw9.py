#! usr/bin/python
# -*- coding: ISO-8859-1 -*-
#http://www.pokepedia.fr/Liste_des_Pok%C3%A9mon_de_la_premi%C3%A8re_g%C3%A9n%C3%A9ration
import unicornhat as unicorn
import time

unicorn.rotation(270)

O = [0, 0, 0] #Light off

def brightness(): #Brightness in fonction of the local time
        currentHour = time.strftime("%H")
        currentHour = str(currentHour)
        if currentHour == "23" or currentHour == "00" or currentHour == "01" or currentHour == "02" or currentHour == "03" or currentHour == "04" or currentHour == "05" or currentHour == "06" or currentHour == "07":
                unicorn.brightness(0.05)
        else:
                unicorn.brightness(0.2)
brightness()

def setPixel(pokemon):
        for y in range(8):
                for x in range(8):
                        a = pokemon[y][x][0]
                        b = pokemon[y][x][1]
                        c = pokemon[y][x][2]
                        unicorn.set_pixel(y, x, a, b, c)

while True :

        #Bulbizarre
        A = [57, 148, 148]
        B = [100, 212, 180]
        C = [115, 172, 49]
        D = [164, 212, 65]

        pokemon001 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,C,D,O,O,O,O],
        [O,O,C,C,A,B,O,O],
        [O,O,A,A,A,A,O,O],
        [O,O,A,O,A,O,O,O]
        ]

        setPixel(pokemon001)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Herbizarre
        A = [32, 148, 90]
        B = [90, 200, 150]
        C = [75, 140, 30]
        D = [106, 180, 32]
        E = [213, 65, 90]
        F = [255, 123, 123]

        pokemon002 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,E,F,O,O,O],
        [O,D,O,E,E,O,D,O],
        [O,C,C,C,D,D,C,O],
        [O,O,C,B,B,C,O,O],
        [O,O,A,B,B,B,O,O],
        [O,A,O,A,A,O,A,O]
        ]

        setPixel(pokemon002)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Florizarre
        A = [32, 139, 115]
        B = [82, 205, 172]
        C = [106, 189, 74]
        D = [57, 139, 41]
        E = [131, 49, 0]
        F = [222, 65, 65]
        G = [255, 131, 115]
        H = [222, 189, 41]

        pokemon003 = [
        [O,F,F,O,O,F,F,O],
        [G,G,F,H,H,F,G,G],
        [F,F,G,F,F,G,F,F],
        [O,F,F,E,E,F,F,O],
        [O,C,D,D,D,D,C,O],
        [C,A,B,C,C,A,B,C],
        [O,A,A,B,B,B,A,O],
        [A,O,A,A,A,A,O,A]
        ]

        setPixel(pokemon003)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Salamèche
        A = [230, 172, 90]
        B = [255, 213, 123]
        C = [252, 105, 69]
        D = [255, 148, 65]
        E = [255, 213, 8]

        pokemon004 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,D,D,O,O,O],
        [O,O,O,C,D,O,O,O],
        [O,E,C,A,B,D,O,O],
        [O,D,O,A,B,O,O,O],
        [O,C,C,A,A,C,O,O]
        ]

        setPixel(pokemon004)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Reptincel
        A = [213, 41, 82]
        B = [230, 172, 90]
        C = [255, 82, 74]
        D = [255, 213, 106]
        E = [255, 65, 0]

        pokemon005 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,C,C,O,O,E,O],
        [O,C,A,O,O,O,D,O],
        [O,O,O,D,C,O,C,O],
        [O,O,C,B,B,C,O,O],
        [O,O,A,O,O,A,O,O]
        ]

        setPixel(pokemon005)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Dracaufeu
        A = [205, 82, 65]
        B = [238, 180, 90]
        C = [238, 131, 41]
        D = [238, 222, 123]
        E = [131, 49, 24]
        F = [8, 65, 82]
        E = [32, 115, 148]
        G = [255, 213, 16]
        H = [230, 65, 16]
        I = [131, 49, 24]

        pokemon006 = [
        [O,O,O,H,O,O,O,O],
        [O,F,O,G,O,O,O,O],
        [F,E,F,O,O,C,C,O],
        [O,I,F,A,C,F,A,C],
        [A,O,A,C,C,A,O,O],
        [A,C,O,D,D,O,A,O],
        [O,A,C,B,B,C,O,O],
        [O,O,A,O,O,A,O,O]
        ]

        setPixel(pokemon006)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Carapuce
        A = [230, 172, 90]
        B = [255, 213, 16]
        C = [90, 172, 156]
        D = [65, 115, 98]
        E = [148, 213, 205]
        F = [180, 246, 238]
        G = [189, 106, 0]

        pokemon007 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,E,F,O,O],
        [O,O,O,C,E,E,C,O],
        [O,C,E,G,A,B,O,O],
        [O,D,C,C,A,A,C,O]
        ]

        setPixel(pokemon007)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Carabaffe
        A = [148, 98, 98]
        B = [189, 139, 57]
        C = [222, 197, 139]
        D = [98, 106, 197]
        E = [148, 139, 238]
        F = [197, 213, 222]

        pokemon008 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,D,E,O,O],
        [O,O,O,O,D,D,O,O],
        [O,O,F,D,C,C,D,O],
        [O,F,E,O,B,C,O,O],
        [O,E,F,D,A,A,D,O]
        ]

        setPixel(pokemon008)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Tortank
        A = [114, 74, 50]
        B = [54, 111, 216]
        C = [187, 122, 43]
        D = [90, 139, 205]
        E = [139, 98, 65]
        F = [213, 172, 74]
        G = [205, 205, 213]

        pokemon009 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,B,D,O,O],
        [O,O,G,E,F,F,O,O],
        [O,E,D,C,C,C,D,O],
        [O,A,E,D,F,F,O,D],
        [O,A,E,C,C,F,O,O],
        [B,A,D,C,C,C,D,O],
        [O,O,B,A,A,O,B,O]
        ]

        setPixel(pokemon009)
        unicorn.show()
        time.sleep(2)
        brightness()
