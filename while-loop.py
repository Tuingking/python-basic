import random

''' While Loop
=========================================================================================================
'''
random_num = random.randrange(0,100)
x = 0
while(random_num != 15):
    x +=1
    random_num = random.randrange(0,100)

print (x)

i = 0
while(i<=20):
    if(i%2 == 0):
        print ("{} ==> genap".format(i))
    elif(i == 9):
        break
    else:
        i += 1
        continue

    i += 1
