import math

n = int(input())
fra = [int(i) for i in input().split()]
st = 1 
ime = fra.pop() #dobimo zadnjo stevilo v imenovalcu
for i in reversed(fra):
    st += ime * i #damo na skupni imenovalec
    st, ime = ime, st # imenovalec in stevec se zamenjata, zaradi dvojnega ulomka
    d = math.gcd(st, ime)
    #skrajsamo ulomek
    st //= d 
    ime //= d

print(ime, "/", st, sep="")
