#Initialize elements in the dictionary
'''
my_dict ={1:'Python', 2: 'Java'}
my_dict_2= dict ({1: 'C++', 2: 'Ruby'})
print (my_dict)
print (my_dict_2)
'''
#Accessing the elements of the dictionary
'''
my_dict ={'Fisrt': 'Python', 'Second': 'Java'}
print(my_dict['Fisrt'])# get value by keys
print (my_dict.get('Second'))
'''
#Adding and changing elements in a dictionary
'''
my_dict ={'First': 'Python', 'Second': 'Java'}
print (my_dict)
my_dict ['Second']='C++' #change the value key second
my_dict ['Third'] = 'Ruby'#add new key, value pair
print (my_dict)
'''
'''
#Deleting elements from the dictionary
my_dict ={'First': 'Python', 'Second': 'Java', 'Third': 'Ruby'}
print(my_dict)
a= my_dict.pop ('Third')#remove the key and return value
print('\nValue:', a)
print('Dictionary:', my_dict)
b= my_dict.popitem() #Remove a key value pair and return them as a tuple
print('\nKey, value pair:', b)
print('Dictionary', my_dict)
my_dict.clear() # Used to clear all the values in the dictionary
#you can use del keyword to delete the values too
'''
#Other Functions
my_dict={'First':'Python', 'Second': 'Java', 'Third':'Ruby'}
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
print(my_dict.get('First'))
