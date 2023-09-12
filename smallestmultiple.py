# Privzeto iz spletne strani: https://www.youtube.com/watch?v=rwL1eBWUFlw
#
#=====================================================================
def gcd(a, b):
    '''Vrne največji skupni deljitelj'''
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

while True:
    try:
        ans = 1
        l = [int(i) for i in input().split()]
        for i in range(len(l)):
            ans = ans * l[i] // gcd(ans,l[i])
        print(ans)
    except:
        break