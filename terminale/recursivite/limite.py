import sys

sys.setrecursionlimit(4000)
print(sys.getrecursionlimit())

def s(n):
    if n == 0:
        return 0
    else:
        return n + s(n-1)
    
r = s(3997)
print(r)