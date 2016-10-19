
def compute(i):
    digits = '123456789'
    result = ''
    if i == 0:
        return result
    while i > 0:
        result = digits[i%10] + result
        i = i//10
    return result

print(convert(30000))