def site1(n):
    s = 0
    for i in range(n + 1):
        s = s + i
    return s

def site2(n):
    s = 0
    print ("n", "s")
    for i in range(n + 1):
        s = s + i
        print(i, s)
    return s

def srec1(n):
    if n == 0:
        return 0
    else:
        return srec1(n - 1) + n

print(srec1(3))

def srec2(n):
    s = 0
    if n == 0:
        print("n", "s")
        print(n, s)
        return 0
    else:
        s = srec2(n - 1) + n
        print(n, s)
        return s

srec2(3)
