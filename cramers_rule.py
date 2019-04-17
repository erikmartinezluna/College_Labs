# CSCE 110 Lab 3 Question 3

def calc_x(user_a, user_b, user_c, user_d, user_e, user_f):
    x_num = (user_e*user_d)-(user_b*user_f)
    x_den = (user_a*user_d)-(user_b*user_c)
    if x_den == 0:
        return(str('invalid'))
    else:
        x = x_num//x_den
        return(x)

def calc_y(user_a, user_b, user_c, user_d, user_e, user_f):   
    y_num = (user_a*user_f)-(user_e*user_c)
    y_den = (user_a*user_d)-(user_b*user_c)
    if y_den == 0:
        return(str('invalid'))
    else:
        y = y_num//y_den
        return(y)   

    
def main():
    user_a = float(input('Enter a: '))
    user_b = float(input('Enter b: '))
    user_c = float(input('Enter c: '))
    user_d = float(input('Enter d: '))
    user_e = float(input('Enter e: '))
    user_f = float(input('Enter f: '))
    
    x = calc_x(user_a, user_b, user_c, user_d, user_e, user_f)
    y = calc_y(user_a, user_b, user_c, user_d, user_e, user_f)
    
    print()
    print('Solivng for the following two equations.')
    
    print(str(user_a)+'x', '+', str(user_b)+'y =', str(user_e))
    print(str(user_c)+'x', '+', str(user_d)+'y =', str(user_f))
    
    print()
    if x == 'invalid' or y == 'invalid':
        print('No unique solution found!')
    else:
        print('x =', str(x))
        print('y =', str(y))

main()