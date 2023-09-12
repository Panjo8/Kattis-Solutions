n = int(input())
st = [int(i) for i in input().split()]
st.sort() #razporedimo po velikosti
vsota = 0
for i in range(n-1):
    vsota += (st[i] - st[i+1])**2 #formula

print(vsota)
    
