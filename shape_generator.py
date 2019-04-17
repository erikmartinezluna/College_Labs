# CSCE 110 Lab 4 Question 1
    
def row(width, symbol):
    row = width * symbol 
    return(row)
    
def column(height, width, symbol):
    column = (symbol + ' '*(width-2) + symbol)
    return(column)
    
def main():
    width = int(input('Width: '))
    height = int(input('height: '))
    symbol = input('Symbol: ')
    
    count = 0
    print('\n' + row(width, symbol))
    while count <= height - 3: 
        print(column(height, width, symbol))
        count += 1
    print(row(width, symbol))
    
    
main()
    