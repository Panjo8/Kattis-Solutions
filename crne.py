n = int(input())

def cuts(n):
    '''Vrne največje število rezov'''
    if n == 1:
        return 2
    if n % 2 == 0:  #preverimo če je sodo
        h = int(n/ 2)  #horizontalne črte
        v = int(n/ 2)  #vertikalne črte
        return int((h + 1)*(v + 1))
    else:          #je liho
        h = round(n/ 2)
        v = n - h
        return (int(h + 1)*(v + 1))

print(cuts(n))