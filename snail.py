from unicornhat import * #import unicornhat as unicorn
import time

VB = [0, 200, 40]

while True:
    x = 3
    y = 3
    unicorn.set_pixel(y, x, VB[0], VB[1], VB[2])
    unicorn.show()
    for i in range(9):
        for j in range(i):
            time.sleep(0.05)
            if i % 2 == 0:
                x -= 1
            else:
                x += 1
            unicorn.set_pixel(y, x, VB[0], VB[1], VB[2])
            unicorn.show()

        for j in range(i):
            time.sleep(0.05)
            if i % 2 == 0:
                y -= 1
            else:
                y += 1
            unicorn.set_pixel(y, x, VB[0], VB[1], VB[2])
            unicorn.show()

    unicorn.clear()
