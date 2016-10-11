def deep_reverse(L):
    i = 0
    for itm in reversed(L[:]):
        #itm.sort(key=lambda x: abs(x), reverse=True)        
        L[i] = list(reversed(itm))
        i += 1