# CSCE 110 Lab 3 Question 1

user_input = float(input('Enter the change amount: '))

user_mod = int(user_input*100)

dol = int((user_mod)//100)
ch1 = user_mod - dol*100 

qua = int((ch1)//25)
ch1 = ch1 - qua*25 

dim = int((ch1)//10)
ch1 = ch1 - dim*10

nic = int((ch1)//5)
ch1 = ch1 - nic*5

pen = int(ch1)

print()

print(str(dol), 'dollars')
print(str(qua), 'quarters')
print(str(dim), 'dimes')
print(str(nic), 'nickels')
print(str(pen), 'pennies')