# operators are constructs you use to manipulate data
#Describes actions that need to be done
#Derive information from data or manipulate them to obtain solutions

#Arithmetic Operators
'''
a=10
b=5
print('Addition:', a+b)
print('Subtraction:', a-b)
print('Multiplication:', a*b)
print('Division:', a/b)
print('Remainder:', a%b)
print('Exponential:', a**b)
'''
#Assignment Operators
'''
a=5
add, sub, mul, div, rem, expo =0, 0, 0, 1, 1, 1
add += a #Add value a with add and assign to add
print(add)
sub -= a #subtract value a with sub and assign to sub
print(sub)
mul *= a #Multiply value a with mul and assign to mul
print(mul)
div /= a #Divide value a with mul and assign to div
print(div)
rem %= a #Find remainder with value a with rem and assign to rem
print(rem)
expo **= a #Exponent the values a with expo and assign to expo
print(expo)
'''
#Comparison Operators
'''
a= 5
b= 10
print(a == b) # true if equal
print(a != b) # True if not equal
print(a > b) # True if a is  greater than b
print(a < b) # True if a is  less than b
print(a >= b) # True if a is  greater than or equal to b
print(a <= b) # True if b is  greater than or equal to b
'''
#Logical Operators -> Used to obtain logic
'''
a=5
b=0
print( a and b) # True if both are true
print (a or b) #True if either one is true
print(not a) # returns opposite of value
print(not b) # returns opposite of value
#It is true if the value of the number is 1 or anything greater and false if the value is zero and a -ve value
'''
#Bitwise Operators. Used to manipulate the bits and value directly 
'''
a=5
b=6
print(a & b) #Perform bit by bit and operation
print(a | b) #Perform bit by bit or operation
print(a ^ b) #Perform bit by bit xor operation
print(~a) #Perform the complement
print(a << b) #Perform left shift operation . shifting by 1 is equal to multipying by 2
print(a>>b) #Perform right shift operation. shifting by 1 is equal to dividing by 2
'''
#Identity Operators. Check whether values are identical or not
'''
a=[1, 2, 3]
b=[2, 3, 4]
print(a is b) #True if a and b are equal
print(a is not b) #True if a and b are not equal
'''
#Membership Operators. Check whether a value exists or not
a=[1, 2, 3]
print (2 in a)#true if value in a
print (2 not in a)#true if value not in a


