r = []
f = []

for l in s:
    r = r + [l]        
    if r == sorted(r) and len(r) > len(f):
        f = r            
    elif r != sorted(r):
        r = [r[len(r)-1]]        

print("Longest substring in alphabetical order is: " + "".join(f))