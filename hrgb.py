import unicornhat as unicorn

unicorn.rotation(270)

def hex_to_rgb(value):
        value = value.lstrip('#')
        lv = len(value)
        return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def test(color):
        color *= 2
        if color > 255:
                color = 255
        return color

while True :
        color = raw_input("Donnez une couleur en hexadecimal:\n")
        if color == "stop":
                break
        else:
                colorRgb = hex_to_rgb(color)
                print "Votre couleur en RGB : ", colorRgb
                color1 = colorRgb[0] / 5
                color2 = colorRgb[1] / 5
                color3 = colorRgb[2] / 5
                a = 0
                b = 8
                while a <= 3:
                        for i in range(a, b):
                                for j in range(a, b):
                                        unicorn.set_pixel(i,j,color1,color2,color3)
                        a += 1
                        b -= 1
                        color1 = test(color1)
                        color2 = test(color2)
                        color3 = test(color3)

                unicorn.show()
