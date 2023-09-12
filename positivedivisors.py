#
# Nalog privzeta iz spletne strani: https://stackoverflow.com/questions/171765/what-is-the-best-way-to-get-all-the-divisors-of-a-number
#
#========================================================================================================================================

import math

def divisors(n):
    divs = [1]
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0: #dobimo prvi delitelj
            divs.extend([i,n/i]) #dobimo drugega
    divs.extend([n])
    return list(set(divs))

for el in sorted(divisors(int(input()))):
    print(int(el))

