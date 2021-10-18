c = float(input("Enter Temperature in degree Celsius: "))
if c>=1.0 and c<=1000.0:
    f = c*9/5+32
    print(c,"Degree Celsius is equal to: ", end="")
    print(f"{float(f)} Fahrenheit")
else:
    print("please input degree Celsius\nBetween 1 and 1000 in numbers only")
F = float(input("Enter Temperature in Fahrenheit: "))
if F>=1.0 and F<=1000.0:
    C = F*5/9-32
    print(F,"Degree Fahrenheit is equal: ",end="")
    print(f"{float(C)} Celcius")
else:
    print("Please input degree Fahrenheit\nBetween 1 and 1000 in numbers only")
