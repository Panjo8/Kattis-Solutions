n = int(input())
rez =  []
fibo = [1, 1]
while fibo[-1] <= n:
        fibo.append(fibo[-1] + fibo[-2]) #tabla fibonaccijevih števil do n-ja
        
while n != 0:
    while fibo[-1] > n: #odštevamo čim večja števila
        fibo.pop()
    n -= fibo[-1]
    rez.append(fibo[-1])
  
niz = ''
for el in sorted(rez):
    niz += f'{el} '
    
print(niz)
    