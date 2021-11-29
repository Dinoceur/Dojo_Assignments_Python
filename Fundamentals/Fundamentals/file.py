num1 = 42 #variable declaration
num2 = 2.3 #variable declaration
boolean = True #data types, primitive, boolean
string = 'Hello World' #data types, primitive, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #composite, list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #composite, tuples
fruit = ('blueberry', 'strawberry', 'banana') #composite, list
print(type(fruit)) #composite, list, initialize
print(pizza_toppings[1]) #composite, list, access value
pizza_toppings.append('Mushrooms') #composite, list, add value
print(person['name']) #composite, tuples, access value
person['name'] = 'George' #composite, tuples, change value
person['eye_color'] = 'blue' #composite, tuples, add value
print(fruit[2]) #composite, list, access value

if num1 > 45: #conditional, if
    print("It's greater") 
else: #conditional, else
    print("It's lower")

if len(string) < 5: #conditional, if
    print("It's a short word!")
elif len(string) > 15: #conditional, else if
    print("It's a long word!")
else: #conditional, else
    print("Just right!")

for x in range(5): #for loop, start
    print(x)
for x in range(2,5): #for loop, start
    print(x)
for x in range(2,10,3): #for loop, start
    print(x)
x = 0
while(x < 5): #while loop, start
    print(x)
    x += 1

pizza_toppings.pop() #composite, list, delete value
pizza_toppings.pop(1) #composite, list, delete value

print(person)
person.pop('eye_color') #composite, tuples, delete value
print(person)

for topping in pizza_toppings: #for loop
    if topping == 'Pepperoni': #conditional, if
        continue #continue
    print('After 1st if statement') #return
    if topping == 'Olives': #conditional, if
        break #break

def print_hello_ten_times(): #function
    for num in range(10): #parameter
        print('Hello') #return

print_hello_ten_times() #function, return

def print_hello_x_times(x): #function
    for num in range(x): #parameter
        print('Hello') #return

print_hello_x_times(4) #function, return

def print_hello_x_or_ten_times(x = 10): #function
    for num in range(x): #parameter
        print('Hello') #return

print_hello_x_or_ten_times() #function, return
print_hello_x_or_ten_times(4) #function, return


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)