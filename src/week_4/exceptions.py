#print('1' / 2)

# mylist = [10, 20, 30]
# mylist.index(11)

def fancy_divide(list_of_numbers, index):
    assert index > 0, "index must be greater than 0"
    denom = list_of_numbers[index]
    return [simple_divide(item, denom) for item in list_of_numbers]

def simple_divide(item, denom):
    try:
        return item / denom
    except ZeroDivisionError:
        return 0

#print(fancy_divide([0, 2, 4], 0))

def normalize(numbers):
    max_number = max(numbers)
    assert(max_number != 0), "Cannot divide by 0"
    for i in range(len(numbers)):
        numbers[i]  /= float(max_number)
        assert(0.0 <= numbers[i] <= 1.0), "output not between 0 and 1"
    return numbers  

normalize([0, 0, 0])

try:
    a = int(input("Input A value: "))
    b = int(input("Input B value: "))
    c = a/b
    print("Result: ", c)
except ValueError:
    raise Exception("Input is not in correct format")
except ZeroDivisionError:
    raise Exception("Cannot divide by zero")
except:
    raise Exception("Some error...")
else:
    print("No error")
finally:
    print("Done")
