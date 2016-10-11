i = -1
t = ""
r = 0
c = 0

while (True):
    i +=1
    if i == len(s):
        break
    t = t + s[i]
    if len(t) == 3:
        if t == "bob":
            r += 1
            t = s[i]
        else:
            i = i-2
            t = ""
print("Number of times 'bob' occurs is: " + str(r))