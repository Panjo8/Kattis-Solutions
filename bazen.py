# Privzeto iz spletne strani: https://github.com/iamvickynguyen/Kattis-Solutions/blob/master/bazen.py
#
#===============================================
import math


def coordinate(n, area):
    h = (250-n)/math.sqrt(2)
    l = area/h
    x = l/math.sqrt(2)
    y = 250 - x
    return x, y


point = [int(x) for x in input().split()]
area = 1/2 * (250**2)

if point[0] == 0 and point[1] == 0: #točka na izhodišču
    print("125.00 125.00")
elif point[0] == 0: #če je točka na abscisni osi
    if point[1] >= 125:
        y = area/point[1]
        print("{0:.2f} 0.00".format(y))
    else:  # na hipotenuzi
        x, y = coordinate(point[1], area)
        print("{0:.2f}".format(x) + " {0:.2f}".format(y))

elif point[1] == 0: #če je točka na ordinatni osi
    if point[0] >= 125:
        x = area/point[0]
        print("0.00 {0:.2f}".format(x))
    else:
        x, y = coordinate(point[0], area)
        print("{0:.2f}".format(y) + " {0:.2f}".format(x))
else:
    # točka je na hipotenuzi
    # preverimo, če je y nad 125
    if point[1] > 125:
        x = 250 - area/point[1]
        print("{0:.2f} 0.00".format(x))
    else:
        x = 250 - area/point[0]
        print("0.00 {0:.2f}".format(x))

    
    

