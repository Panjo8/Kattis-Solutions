import math

while True:
    try:
        l = input().split()
        r = int(l[0])
        s = float(l[1])
        v = math.sqrt(r*(s+0.16)/0.067)
        print(round(v))
    except:
        break