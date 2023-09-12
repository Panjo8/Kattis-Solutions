n = int(input())

sez = []
sez_kvadrati=[]
for i in range(n):
    nova = int(input())
    sez.append(nova)
    sez_kvadrati.append(nova**2)

zmnozek = 0

vsota1 = 0
vsota2 = sum(sez) # seštejemo vsa podana števila 
for i in range(n):
    vsota1 += sez_kvadrati[i]
    # z odštevanjem od celote se izognemo vsakičnem
    # seštevanju dolgega seznama števil
    vsota2 -= sez[i] 
    skupaj = vsota1 * vsota2
    if skupaj > zmnozek:
        zmnozek = skupaj
print(zmnozek)
        
