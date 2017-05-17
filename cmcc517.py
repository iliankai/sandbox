from itertools import permutations
from operator import add, truediv, mul, sub
codes = [list(i) for i in permutations('*/+-', 3)]
target = 517
print("Enter the four numbers separated by space. Example: 21 25 20 28 (enter)")
m = [int(i) for i in input().strip().split(' ')]
ops={'*':mul, '/':truediv, '+':add, '-':sub}
f = False
for c in codes:    
    n, t = m[:], c[:]
    for i in '*/+-':
        if i in c:
            k = c.index(i)
            n = n[:k] + [ops[i](n[k], n[k+1])] + n[k+2:]
            c.remove(i)    
    if n[0] == target:
        print("Found it", t)
        f = True
        break
if not f:
    print("Cannot find one")

    
