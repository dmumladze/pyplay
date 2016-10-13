def how_many(aDict):
    total = 0
    for v in aDict.values():
        total += len(v)
    return total

def biggest(aDict):
    key = ''
    total = 0
    for k, v in aDict.items():
        if sum(v) > total:
            total = sum(v)
            key = k       
    return key    
    
print(biggest({'b': [1, 7, 5, 4, 3, 18, 10, 0], 'a': []}))
print(how_many({'B': [15], 'u': [10, 15, 5, 2, 6]}))