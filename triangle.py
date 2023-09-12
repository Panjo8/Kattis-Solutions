# Narejeno s pomočjo s spletne strani: https://www.youtube.com/watch?v=5plLxMnbtAw
#
#===========================================================
import sys, math

i = 1
for vrstica in sys.stdin:
    n = int(vrstica)
    obseg = math.ceil(n*math.log10(3/2) + math.log10(3)) #zaokrožimo na celo število
    print("Case " + str(i) + ": " + str(obseg))
    i += 1
    
