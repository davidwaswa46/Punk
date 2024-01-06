#while loop
'''
seconds =10
while seconds >= 0:
    print(seconds, end='->')
    seconds -=1
print('Happy new year 2024!!')   
'''
'''
counter = 0
while counter < 3:
    print("Hello there?")
    counter = counter +1
else:
    print("Why are you not replying bro?")
'''
# nested loops
count = 1
for i in range (10):
    print (str(i)* i)
    for j in range (0,i):
        count = count +1