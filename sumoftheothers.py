import sys

for vrstica in sys.stdin:
    print(sum(map(lambda x : int(x), vrstica.split(' '))) // 2)
    
      
        
    