'''
#creating the set
my_set ={1, 2, 3, 4, 5, 5, 5} # since is a collection of unique elements 5 will only be printed once
print(my_set)
'''
'''
#Adding elements in sets
my_set={1, 2, 3}
my_set.add(4)
print (my_set)
'''
#Other methods in sets
'''
my_set={1, 2, 3, 4,}
my_set_2={3, 4, 5, 6}
print(my_set.union(my_set_2), '------', my_set |my_set_2)#union operations can be done
print(my_set.intersection(my_set_2), '------', my_set & my_set_2)# intersection using intersecting elements
print(my_set.difference(my_set_2), '------', my_set - my_set_2) #performs the difference
print(my_set.symmetric_difference(my_set_2), '------', my_set ^ my_set_2)#perform the symmetric difference
my_set.clear()# empty the set
print(my_set)
'''
#operations with set
superset={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s1={1, 2, 3, 4}
s2={3, 4, 5, 6}
print(s1 == s2)#if symmetric
print(s1 != s2)#if not symmetric
print(s1<= superset)#if s1 is a subset of the superset
print(s1< superset)#if s1 is a proper subset of the superset
print(s1>= s2)#if s2 is a subset of s1
print(s1>s2)# if s2 is a proper subset of s1

