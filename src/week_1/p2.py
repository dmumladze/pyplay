i = -1
t = ""
r = 0
c = 0
q = "bob"
s = "anhghdfbobbobmnmnmnbobobobpopopodffgjh"

while (True):
    i +=1
    if i == len(s):
        break
    t = t + s[i]
    if len(t) == len(q):
        if t == q:
            r += 1
            t = s[i]
        else:
            i -= len(q)-1
            t = ""            
print("Number of times '" + q + "' occurs is: " + str(r))