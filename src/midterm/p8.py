def f(i):
    return i + 2
def g(i):
    return i > 5

def applyF_filterG(L, f, g):
    for itm in L[:]:
        if not g(f(itm)):
            L.remove(itm)
    
    if len(L) == 0:
        return -1

    result = 0
    for itm in L:
        if itm > result:
            result = itm
    return result

L = [0, -10, 5, 6, -4]
print(applyF_filterG(L, f, g))
print(L)