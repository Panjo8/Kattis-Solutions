vrstica = int(input())

for i in range(vrstica):
    podatki = [int(x) for x in input().split()]
    avg = sum(podatki[1:])/podatki[0] #delimo vsoto podatkov, s število podatkov
    n = len([x for x in podatki[1:] if x > avg]) #preverimo, koliko števil je nad povpreèjem
    print("%.3f" % (n*100/podatki[0]) + "%") 