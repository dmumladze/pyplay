
def bubble_sort(aList):
    swap = False
    while not swap:
        swap = True
        for i in range(1, len(aList)):
            a = aList[i-1] 
            b = aList[i]
            if a > b:
                swap = False
                aList[i], aList[i-1] = aList[i-1], aList[i]
    
L = [3,6,1,7,0,9,8,4,2]
bubble_sort(L)
print(L)
