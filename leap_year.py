# CSCE 110 Lab 4 Question 2
    
def main():
    start = int(input("Starting Year: "))
    end = int(input("Ending Year: "))
    
    while start <= end: 
        if start % 4 == 0 and start % 100 != 0:
            print(start)
        if start % 100 == 0 and start % 400 == 0:
            print(start)
        start += 1
main()
    