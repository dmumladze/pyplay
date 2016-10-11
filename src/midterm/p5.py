def dotProduct(listA, listB):
    product = 0
    for i in range(len(listA)):
        a = listA[i]
        b = listB[i]
        product += (a*b)
    return product