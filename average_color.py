import numpy as np
from colormap import rgb2hex



def avgColor(color1, color2):
    n = 2
    color1 = [(color1[i:i+n]) for i in range(0, len(color1), n)]
    color2 = [(color2[i:i+n]) for i in range(0, len(color2), n)]

    red1 = color1[0]
    red2 = color2[0]

    green1 = color1[1]
    green2 = color2[1]

    blue1 = color1[2]
    blue2 = color2[2]

    avg_red = int((int(red1, 16) + int(red2, 16)) /2)
    avg_green = int((int(green1, 16) + int(green2, 16)) /2)
    ava_blue = int((int(blue1, 16) + int(blue2, 16)) /2)

    avg_color = rgb2hex(avg_red, avg_green, ava_blue)

    # hex_red = hex(avg_red)
    # hex_green = hex(avg_green)
    # hex_blue = hex(ava_blue)

    # avg_color = hex_red + hex_green + hex_blue

    return avg_color






c1 = '0000FF'
c2 = 'FF0000'
result = avgColor(c1, c2)
print(result)
