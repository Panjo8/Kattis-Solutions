niz = input()

def no_duplicates(niz):
    besede = niz.split() #besede razdelimo
    nove = []
    for beseda in besede:
        if beseda in nove: #preverimo, če je beseda v novem nizu
            return('no')
        else:
            nove.append(beseda) #besedo dodamo v novi niz
    return('yes')

print(no_duplicates(niz))