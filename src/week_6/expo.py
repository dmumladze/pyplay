
def getSubsets(aList):
    if len(aList) == 0:
        return [[]]

    print(aList[:-1])
    smaller = getSubsets(aList[:-1])    
    extra = aList[-1:]
    new   = []

    for small in smaller:
        new.append(small+extra)
    
    return smaller+new

print(getSubsets([1,2]))
