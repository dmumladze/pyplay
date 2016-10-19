
text  = "anhghdfbobbobkmgwxmnbobobobpoxypodftgjhbob"
find  = "bob"

#solution 1 
index = 0
word  = ""
match = 0

while index < len(text):    
    word = word + text[index]
    if len(word) == len(find):
        if word == find:
            match += 1
            word = text[index]
        else:
            index -= len(find)-1
            word = "" 
    index += 1 
print("Number of times '", find, "' occurs is: ", str(match), sep='')

#solution 2
start = 0
end   = len(find)
match = 0

while end <= len(text):
    word = text[start:end]
    if word == find:
        match += 1
        start = end-1
        end   = end + len(find)-1
    else:
        start += 1
        end   += 1              
print("Number of times '" ,find, "' occurs is: ", str(match), sep='')