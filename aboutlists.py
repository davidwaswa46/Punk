'''
my_list =[1, 2, 3, 'learning', 'python']
print(my_list[:])#Accsessing all elements ata a go
print(my_list[3])#Accesessing the 3rd element of the list
print(my_list[0:4])#Accesessing the elements from 1 to 3 
print(my_list[::-1])#Acceseessing the elements of the list in a reverse order
print(my_list[0:5:2])#Access from index 0 to 4 and jumping two elements instead of one
print(my_list[3][2])#Accsess particular element of the string learning (a)
'''
#Adding elements to the list
'''
my_list =[1, 2, 3, 'learning', 'python']
my_list_2 =[4, 5, 3.142, 'fun', 'cool']
my_list.append([555, 12]) # Add passed parameters as a single element 
print(my_list)
print(len(my_list))
my_list_2.extend ([555, 12])#extending list by adding all the elements one by one
print(my_list_2)
print(len(my_list_2))
my_list.insert(1,'insert_example') #Insert passed parameter in place of index and extend list
print (my_list +['just for example']) #Concatination
print(my_list *2) #Multiply
print (my_list)
'''
'''
my_list =[1, 2, 3, 'learning' 'python']
my_list_2= [4, 5, 3.142, 'fun','cool']
#Deleting Elements from the list
my_list_2.extend([555, 12, 'example']) #extending list by adding all the elements one by one
print (my_list_2)
del my_list_2[5]# deleting using delete keyword
print(my_list_2)
my_list_2.remove ('example')#remove past element if present else error
print (my_list_2)
a = my_list_2.pop(5)# deleted element can be retrieved
print('Popped Element:', a, 'List remaining:', my_list_2 )
my_list_2.clear()
print (my_list_2)
'''
'''
my_list =[1, 2, 3, 'learning', 'python']
#Other functions
new = [5, 4, 12, 45, 3]
print(len(my_list)) #finds the length of the list
print(my_list.index('learning')) #finds index of the element
print(my_list.count('learning'))#finds count of times repeated in list
print(sorted(new))#sorts elements in the list but does not change original
print(new)
new.sort(reverse=True)#sorts original list in descending if reverse=True else in ascending order
print(new)
new.reverse()# reverses list elements
print(new)
new_list = my_list.copy()#copies elements of list to the new list
print(new_list)
'''
'''
my_tuple= tuple()
my_tuple_2= tuple()
print (my_tuple)
print(my_tuple_2)
my_tuple= my_tuple +(1, 2, 3)
print (my_tuple)
'''
'''
#Initializing elements to the tuple
my_tuple = (1, 2, 3)
my_tuple_2 = tuple (('Python', 'for', 'learning'))
print (my_tuple)
print(my_tuple_2)
my_tuple_3 = 'example', #add comma in the end if you want a tuple with single element, else it will be a string element
print(type(my_tuple_3))
'''
'''
#Accessing elements of a tuple
my_tuple= (1, 2, 3)
my_tuple_2 =('Python', 'for', 'edureka')
my_tuple_3 = (1, 2, 3,['English', 'python'])
print (my_tuple[0])
print (my_tuple_2[:])
print (my_tuple_3 [3][1])
'''
'''
#Elements in the tuple can be changed if the data type in the list is mutable
my_tuple_3 = (1, 2, 3,['English', 'python'])
my_tuple_3[3][0]='Hindi'
print(my_tuple_3)
'''
#tuple methods
my_tuple_3=(1, 2, 3, ['Hindi', 'Python'])
print(my_tuple_3.count(2))
print(my_tuple_3.index(['Hindi', 'Python']))

