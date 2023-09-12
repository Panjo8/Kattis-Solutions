#
#     Narejeno s pomočjo iz spletne strani: https://codereview.stackexchange.com/questions/266408/my-recursive-attempt-at-collatz-sequence-in-python
#
#====================================================================
def sum(n):
    '''Vrne vsoto zaporedja'''
    n = int(n)
    if n == 1:
        return 1
    if n % 2 == 0: #preveri, če je sodo število
        return int(n + sum(n/2))
    else: #je liho število
        return int(n + sum(3*n + 1))
    
        
        

n = int(input())
print(sum(n))

