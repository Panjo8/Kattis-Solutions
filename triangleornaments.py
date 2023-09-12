from math import sqrt

def dolzina_tri(a,b,c):
    '''Vrne dolžino trikotnika od skrajne
        leve do skrajno desno toèke'''
    if a == b:
        return c
    else:
        x = sqrt(c**2 - ((a**2 - b**2)**2)/(2*a**2 + 2*b**2 - c**2)) 
        return x



n = int(input())
tab = []
for _ in range(n):
    rez = [int(i) for i in input().split()]
    tab.append(rez)
    
total = 0
for i in range(n): #sprehajamo se po trikotnikih
    a = tab[i][0] 
    b = tab[i][1]
    c = tab[i][2]
    total += dolzina_tri(a,b,c)

print(total)
