
def selection_sort(aList):
    end = 0
    while end != len(aList):
        for i in range(end, len(aList)):
            a = aList[i]
            b = aList[end]
            if a < b:
                aList[end], aList[i] = aList[i], aList[end]
        end += 1

L = [3,6,1,7,0,9,8,4,2]
selection_sort(L)
print(L)