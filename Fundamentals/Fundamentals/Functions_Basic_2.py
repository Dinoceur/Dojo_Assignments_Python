temp=[]
def countdown(a):
    for x in range(a,-1,-1):
        temp.append(x)
    print(temp)
countdown(5)

def print_and_return(list):
    print(list[0])
    return list[1]
print(print_and_return([1,2]))

def first_plus_length(list):
    return list[0] + len(list)
print(first_plus_length([1,2,3,4,5]))

def values_greater_than_second(list):
    if len(list) < 2:
        return False
    new = []
    for x in range(len(list)):
        if list[x] > list[1]:
            new.append(list[x])
    print(len(new))
    return new

print(values_greater_than_second([5,2,3,2,1,4]))

def length_and_value(size,value):
    list=[size]*value
    return list
print(length_and_value(4,7))