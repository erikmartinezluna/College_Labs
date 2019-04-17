size = int(input('Size : '))

print()

a1 = 1 
s1 = size*2 - 1

count = 0
while count < size*2 -1:
    print(' '*s1 +'/'*a1 + '**' + '\\'*a1) 
    a1 += 1
    s1 -= 1
    count += 1


e1 = size*2
print('+' + '=*'*e1 + '+')
 
d1 = size - 1
d2 = size*2 - 2 
t1 = 1

count = 0
while count < size:
    print('|' + '.'*d1 + '/\\'*t1 + '.'*d2 + '/\\'*t1 + '.'*d1 + '|')
    d1 -= 1
    d2 -= 2    
    t1 += 1
    count +=1

t1 -= 1
d1 += 1
d2 += 2

count = 0
while count < size:
    print('|' + '.'*d1 + '\/'*t1 + '.'*d2 + '\/'*t1 + '.'*d1 + '|')
    d1 += 1
    d2 += 2
    t1 -= 1
    count +=1
    
e1 = size*2
print('+' + '=*'*e1 + '+')

d1 = 0
d2 = 0
t1 = size

count = 0
while count < size:
    print('|' + '.'*d1 + '\/'*t1 + '.'*d2 + '\/'*t1 + '.'*d1 + '|')
    d1 += 1
    d2 += 2
    t1 -= 1
    count +=1

d1 = size - 1
d2 = size*2 - 2 
t1 = 1

count = 0 
while count < size:
    print('|' + '.'*d1 + '/\\'*t1 + '.'*d2 + '/\\'*t1 + '.'*d1 + '|')
    d1 -= 1
    d2 -= 2    
    t1 += 1
    count +=1    
    
print('+' + '=*'*e1 + '+')

a1 = 1 
s1 = size*2 - 1

count = 0
while count < size*2 -1:
    print(' '*s1 +'/'*a1 + '**' + '\\'*a1) 
    a1 += 1
    s1 -= 1
    count += 1