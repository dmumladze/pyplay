def oddTuples(aTup):
    rTup = ()
    index = 0

    while index < len(aTup):
        rTup += (aTup[index],)
        index += 2

    return rTup

def oddTuples2(aTup):
    return aTup[::2]

#should print every other element in aTup ('I', 'a', 'tuple')
print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))
