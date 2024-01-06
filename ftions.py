def add(x, y):# you define a function using the def keyword
    print('The sum of a and b is:', (x+y))

def multiply (x, y): 
    print ('The product of x and y is:',(x*y))  

add (12, 10)     
multiply(7, 3)
add(9, 10)
multiply(20, 8)
# in-built functions
list1 = [1, 0, 3]
print (abs(-7)) #returns the positive value of the passed argument
print(all(list1))#returns true if all elements are true
print(any(list1))# returns true if any one element is true
print(len(list1))
print(min(list1))
print(max(list1))
print(sum(list1))
print(type(list1))