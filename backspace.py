niz = input()  

sez = []
for elt in niz: 
    if elt == '<':
        sez.pop() #odstrani zadnji element iz seznama
    else:
        sez.append(elt)
        
print(str(''.join(sez))) #združi tabelo v niz

