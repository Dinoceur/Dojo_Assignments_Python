##1
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0]=15
print(x)
#Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name']='Bryant'
print(students)
#In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0]='Andres'
print(sports_directory['soccer'])
#Change the value 20 in z to 30
z[0]['y']=30
print(z)

##2
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
#Create a function iterateDictionary(some_list) that, given a list of dictionaries, 
# the function loops through each dictionary in the list and prints each key and the 
# associated value. For example, given the following list
def iterate_dictionary(list):
    for x in range(0, len(list)):
        output='' 
        for key,val in list[x].items():
            output += f" {key} - {val},"
        print(output)
iterate_dictionary(students)

##3
def iterate_dictionary2(key_name,list):
    for x in range(0, len(list)):
        
        for key,val in list[x].items():
            if key == key_name:
                print(val)
iterate_dictionary2('first_name',students)
iterate_dictionary2('last_name',students)

##4
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for keys, x in some_dict.items():
        print((len(some_dict[keys])) , (keys))
        for x in x:
            print(x)

printInfo(dojo)