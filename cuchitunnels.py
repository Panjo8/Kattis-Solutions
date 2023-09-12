n = int(input())
sobe = [int(i) for i in input().split( )]
povezave = 0

for i, el in enumerate(sobe): #oštevilčimo sobe
    if i != 0:
    #izračunamo število povezav med sobami
        sobe[i] = sobe[i] - 1
    povezave += sobe[i]
    
def pravilno(n,sobe):
    '''Vrne ali je drevo pravilno ali ne'''
    veje = 0
    bool_ = True
    sobe = reversed(sobe) #začnemo na koncu veje
    for el in sobe:
        if el > veje:
            bool_ = False
        veje -= el
        veje += 1
    return bool_
    
print('YES' if pravilno(n,sobe)== True and povezave + 1 == n else 'NO')
