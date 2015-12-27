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

        #Chenipan
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon010 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon010)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Chrysacier
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon011 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon011)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Papilusion
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon012 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon012)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Aspicot
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon013 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon013)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Coconfort
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon014 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon014)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Dardargnan
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon015 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon015)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Roucool
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon016 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon016)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Roucoups
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon017 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon017)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Roucarnage
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon018 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon018)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Rattata
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon019 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon019)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Rattatac
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon020 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon020)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Piafabec
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon021 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon021)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Rapasdepic
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon022 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon022)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Abo
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon023 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon023)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Arbok
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon024 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon024)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Pikachu
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon025 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon025)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Raichu
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon026 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon026)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Sabelette
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon027 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon027)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Sablaireau
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon028 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon028)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Nidoran
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon029 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon029)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Nidorina
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon030 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon030)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Nidoqueen
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon031 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon031)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Nidoran
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon032 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon032)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Nidorino
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon033 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon033)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Nidoking
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon034 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon034)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Mélofee
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon035 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon035)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Mélodelfe
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon036 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon036)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Goupix
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon037 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon037)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Feunard
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon038 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon038)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Rondoudou
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon039 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon039)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Grodoudou
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon040 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon040)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Nosferapti
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon041 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon041)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Nosferalto
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon042 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon042)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Mystherbe
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon043 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon043)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Ortide
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon044 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon044)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Rafflésia
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon045 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon045)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Paras
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon046 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon046)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Parasect
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon047 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon047)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Mimitoss
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon048 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon048)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Aéromite
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon049 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon049)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Taupiqueur
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon050 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon050)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Triopikeur
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon051 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon051)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Miaouss
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon052 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon052)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Persian
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon053 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon053)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Psykokwak
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon054 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon054)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Akwakwak
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon055 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon055)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Férosinge
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon056 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon056)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Colossinge
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon057 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon057)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Caninos
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon058 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon058)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Arcanin
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon059 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon059)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Ptitard
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon060 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon060)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Têtarte
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon061 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon061)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Tartard
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon062 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon062)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Abra
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon063 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon063)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Kadabra
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon064 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon064)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Alakazam
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon065 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon065)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Machoc
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon066 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon066)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Machopeur
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon067 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon067)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Mackogneur
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon068 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon068)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Chétiflor
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon069 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon069)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Boustiflor
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon070 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon070)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Empiflor
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon071 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon071)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Tentacool
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon072 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon0072)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Tentacruel
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon073 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon073)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Racaillou
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon074 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon074)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Gravalanch
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon075 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon075)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Grolem
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon076 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon076)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Ponyta
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon077 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon077)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Galopa
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon078 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon078)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Ramoloss
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon079 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon079)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Flagadoss
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon080 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon080)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Magnéti
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon081 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon081)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Magnéton
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon082 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon082)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Canarticho
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon083 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon083)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Doduo
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon084 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon084)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Dodrio
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon085 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon085)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Otaria
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon086 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon086)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Lamantine
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon087 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon087)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Tadmorv
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon088 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon088)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Grotadmorv
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon089 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon089)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Kokiyas
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon090 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon090)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Crustabri
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon091 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon091)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Fantominus
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon092 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon092)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Spectrum
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon093 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon093)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Ectoplasma
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon094 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon094)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Onix
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon095 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon095)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Soporifik
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon096 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon096)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Hypnomade
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon097 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon097)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Krabby
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon098 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon098)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Krabboss
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon099 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon099)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Voltorbe
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon100 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon100)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Électrode
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon101 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon101)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Nœunœuf
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon102 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon102)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Noadkoko
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon103 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon103)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Osselait
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon104 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon104)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Ossatueur
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon105 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon105)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Kicklee
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon106 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon106)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Tygnon
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon107 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon107)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Excelangue
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon108 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon108)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Smogo
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon109 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon109)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Smogogo
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon110 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon110)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Rhinocorne
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon111 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon111)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Rhinoféros
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon112 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon112)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Leveinard
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon113 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon113)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Saquedeneu
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon114 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon114)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Kangourex
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon115 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon115)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Hypotrempe
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon116 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon116)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Hypocéan
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon117 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon117)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Poissirène
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon118 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon118)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Poissoroy
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon119 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon119)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Stari
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon120 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon120)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Staross
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon121 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon121)
        unicorn.show()
        time.sleep(2)
        brightness()

        #M. Mime
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon122 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon122)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Insécateur
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon123 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon123)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Lippoutou
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon124 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon124)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Élektek
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon125 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon125)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Magmar
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon126 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon126)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Scarabrute
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon127 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon127)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Tauros
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon128 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon128)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Magicarpe
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon129 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon129)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Léviator
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon130 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon130)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Lokhlass
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon131 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon0131)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Métamorph
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon132 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon132)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Évoli
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon133 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon133)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Aquali
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon134 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon134)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Voltali
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon135 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon135)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Pyroli
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon136 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon136)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Porygon
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon137 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon137)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Amonita
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon138 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon138)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Amonistar
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon139 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon139)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Kabuto
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon140 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon140)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Kabutops
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon141 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon141)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Ptéra
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon142 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon142)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Ronflex
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon143 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon143)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Artikodin
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon144 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon144)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Électhor
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon145 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon145)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Sulfura
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon146 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon146)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Minidraco
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon147 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon147)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Draco
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon148 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon148)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Dracolosse
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon149 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon149)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Mewtwo
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon150 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon150)
        unicorn.show()
        time.sleep(2)
        brightness()

        #Mew
        A = [, , ]
        B = [, , ]
        C = [, , ]
        D = [, , ]
        E = [, , ]

        pokemon151 = [
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O],
        [O,O,O,O,O,O,O,O]
        ]

        setPixel(pokemon151)
        unicorn.show()
        time.sleep(2)
        brightness()
