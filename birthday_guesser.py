# CSCE 110 Lab 3 Question 4

def calc(q_1, q_2, q_3, q_4, q_5):
    day = 0
    if q_1 == 'y':
        day += 1
    if q_2 == 'y':
        day += 2
    if q_3 == 'y':
        day += 4
    if q_4 == 'y':
        day += 8
    if q_1 == 'y':
        day += 16
    return(day)
    
def main():
    print('Question #1: Is your birthday in Set 1?\n')
    
    print('          1  3  5  7')
    print('          9 11 13 15')
    print('         17 19 21 23')
    print('         25 27 29 31\n')
    
    q_1 = input ('Enter (n)o or (y)es: ')
    
    print('Question #2: Is your birthday in Set 1?\n')
    
    print('          2  3  6  7')
    print('         10 11 14 15')
    print('         18 19 22 23')
    print('         26 27 30 31\n')
    
    q_2 = input ('Enter (n)o or (y)es: ')
    
    print('Question #3: Is your birthday in Set 1?\n')
    
    print('          4  5  6  7')
    print('         12 13 14 15')
    print('         20 21 22 23')
    print('         28 29 30 31\n')
    
    q_3 = input ('Enter (n)o or (y)es: ')
    
    print('Question #4: Is your birthday in Set 1?\n')
    
    print('          8  9  10 11')
    print('         12 13 14 15')
    print('         24 25 26 27')
    print('         28 29 30 31\n')
    
    q_4 = input ('Enter (n)o or (y)es: ')
    
    print('Question #5: Is your birthday in Set 1?\n')
    
    print('         16 17 18 19')
    print('         20 21 22 23')
    print('         24 25 26 27')
    print('         28 29 30 31\n')
    
    q_5 = input ('Enter (n)o or (y)es: ')
    
    print(calc(q_1, q_2, q_3, q_4, q_5))
    
main()
    