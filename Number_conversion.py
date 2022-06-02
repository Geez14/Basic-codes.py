# converts binary to decimal
def binary(decimal,base):    # decimal as input will be string value
    list =  []
    length = len(decimal)
    binary = 0
    
    for i in range(length):
        # here we will append each character from input
        list.append(int(decimal[i]))
    for j in list:
        length -= 1
        binary += (base**length)*j
    return binary             # binary will return integer value




# converts decimal to binary
def decimal(binary,base):   # binary as input will be integer value
    list = []
    temp = ""
    while True:
        decimal = binary%base
        list.append(decimal)
        remaining = int(binary/base)
        if remaining == 0:
            break
        else:
            binary = remaining
    for i in list:
        temp += str(i)
    temp = int(temp[::-1])
    return temp      # temp will return integer


# ___________________________________________________________________________________________________

base_of_binary = 2
base_of_octadecimal = 8

print("BINARY TO DECIMAL: A\nDECIMAL TO BINARY: B\nOCTADECIMAL TO DECIMAL: C\nOCTADECIMAL TO BINARY: D")
decision = input("enter your option: ")

# -------------------------------------------------------------------------------------------------

# line 12 to 26 is for binary to decimal conversion


if decision.upper() == "A":                                                                     # checking the input entered in decision variable and .upper() line will convert option upper case.
    number = input("enter the binary number: ")                                                 # input of binary number in string format.
    base_of_binary = 2                                                                          # since we are converting binary to decimal so base of lower number is taken, in this case is binary.
    try:                                                                                        # checking input.
        check = int(number)                                                                     #        checking if the number is int or not.
        length = len(number)                                                                    #        meausring the length of input string.
        for i in range(length):                                                                 #        starting the for loop to check string entered is only 1 or 0.
            temp = int(number[i])                                                               #        making a variable and putting value of according to the string position.
            if temp == 0 or temp == 1:                                                          #        checking the temp variable to know whether the string stored is 0 or 1.
                if i == length-1:                                                               #        now checking if the all value is 0 or 1.
                    print(binary(number,base_of_binary))                                        #        then print the output and the output is int type.
            else:                                                                               #        taking else statement if the variable contain any other number except 0 or 1.
                print("Nmber you entered is not binary") # output is an integer                 #        printing the value if the wrong input is given.
                break                                                                           #        break the loop if the wrong number is input and terminate the process.
    except ValueError:                                                                          #        ooutput if the person is giving the required thing or not.
        print("Don't enter unnecessary things :(")                                              #        if something wrong is given in input then print the output to know mistake.

# -------------------------------------------------------------------------------------------------

# line 35 to 41 is for decimal to binary conversion




elif decision.upper() == "B":                                                                   # checking the input entered in decision variable and .upper() line will convert option upper case.
    base_of_binary = 2                                                                          # since we're converting decimal to binary so base of lower number form is taken, in this case is binary.
    try:                                                                                        # checking input.
        number = int(input("enter whole number: "))                                             #       checking the number input is int or not.
        unpacked = decimal(number,base_of_binary)                                               #       storing the number into variable.
        print(unpacked)                                                                         #       reversing the variable output.
    except ValueError:                                                                          #       output if the person is giving the required thing or not.
        print("enter only +ve whole number")                                                    #       printing message to the person if wrong thing is input.

# -------------------------------------------------------------------------------------------------

# line 48 to 65 is for octadecimal to decimal conversion

        

elif decision.upper() == "C":                                                                  # checking the input entered in decision variable and .upper() line will convert option upper case.                                                                    # since we're converting octadecimal to decimal so base of lower number form is taken, in this case is octadecimal.
    number = input("enter octadecimal number: ")                                               # input of octadecimal number in string format.
    try:                                                                                       # checking input.
        check = int(number)
        raw = [1,2,3,4,5,6,7]
        if "8" in number or "9" in number:
            print("Let me give you a hint:-")
            print(f"octadecimal include: {raw}")                                               #       breaking the loop if the wrong number is input and terminate the process.
        else:
            Decimal_number = binary(number,base_of_octadecimal)
            print(Decimal_number,"is decimal number of",number,"octadecimal number")
    except ValueError:                                                                         #       output if the person is giving the required thing or not.
        print("Don't enter unnecessary things :(")                                             #       message for wrong input.
        

# -------------------------------------------------------------------------------------------------

# line 73 to 87 is for octadecimal to binary conversion


elif decision.upper() == "D":
    octadecimal = input("Enter octadecimal number: ")
    if "9" in octadecimal or "8" in octadecimal:
        print("know i'm sure you are pile of shit")
    else:
        try:
            Decimal_number = binary(octadecimal,base_of_octadecimal)
            Binary_number = decimal(Decimal_number,base_of_binary)
            print(f"{Binary_number} is binary of {octadecimal} octadecimal")
        except :
            print("I Don't think you are 5 year old baby")
        
        
        
        
elif decision.upper() == "E":
    print("comming soon")
