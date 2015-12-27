import unicornhat as unicorn

def intensity(color):
    r = color[0]
    g = color[1]
    b = color[2]

    while r < 254 and g < 254 and b < 254:
        for j in range(8):
            for k in range(8):
                unicorn.set_pixel(j,k,r,g,b)
                unicorn.show()
        r += 2
        g += 2
        b += 2

    while r > 1 or g > 1 or b > 1:
        for j in range(8):
            for k in range(8):
                unicorn.set_pixel(j,k,r,g,b)
                unicorn.show()
        if r > 1:
            r -= 2
        if g > 1:
            g -= 2
        if b > 1:
            b -= 2

X = [0, 127, 0]         #Green
O = [0, 0, 0]           #Black
W = [127, 127, 127]     #White
B = [90, 40, 0]         #Brown
U = [0, 0, 128]         #Blue
R = [128, 0, 0]         #Red
J = [252, 210, 28]      #Yellow

while True:
    intensity(X)
    intensity(B)
    intensity(U)
    intensity(R)
    intensity(J)
