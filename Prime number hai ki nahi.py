a = int(input('Enter any number greater than 1->>'))
if a>1:
    for i in range(2,a):
        if a % i == 0:
               print("it is not prime number")
               break
    else:
        print("it is prime number")       
else:
    print("invalid input")
    
