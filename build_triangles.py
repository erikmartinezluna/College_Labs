def main():
    height = int(input('Height of Triangle: '))
    
    print()
    
    print(' '*height + '/\\' + ' '*height)
    
    i = 1
    
    while i < (height-1): 
        print(' '*(height-i) + '/' + ' '*i*2 + '\\' )   
        i+=1
    
    print(' /'+ '_'*((height*2)-2) + '\\')

main()