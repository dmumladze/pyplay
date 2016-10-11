c = {i:0 for i in "aeiou"}

r = 0

for l in s:
    if l in c:
        r+=1
        
print("Number of vowels: " + str(r))