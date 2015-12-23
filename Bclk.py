import unicornhat as unicorn
import time

R, O, Y, G, B, V = [255, 51, 51], [255, 153, 51], [255, 255, 51], [153, 255, 51], [51, 153, 255], [153, 51, 255]

def brightness(): #Brightness in fonction of the local time
        currentHour = time.strftime("%H")
        if currentHour == 23 or currentHour <= 07:
                unicorn.brightness(0.05)
        else:
                unicorn.brightness(0.1)

def clock(t, x, color, color2):
    for i in range(3):
        if t - 40/(2**i) >= 0:
                unicorn.set_pixel(x, (4-i), color[0], color[1], color[2])
                t -= 40/(2**i)
        else:
                unicorn.set_pixel(x, (4-i), 0, 0, 0)

    x -= 1
    for j in range(4):
        if t - 8/(2**j) >= 0:
                unicorn.set_pixel(x, (5-j), color2[0], color2[1], color2[2])
                t -= 8/(2**j)
        else:
                unicorn.set_pixel(x, (5-j), 0, 0, 0)

while True:
        for x in range(2, 7, 2):
                if x == 2:
                        t = int(time.strftime("%S"))
                        clock(t, x, B, V)
                elif x == 4:
                        t = int(time.strftime("%M"))
                        clock(t, x, Y, G)
                else:
                        t = int(time.strftime("%H"))
                        clock(t, x, R, O)

        brightness()
        unicorn.show()
