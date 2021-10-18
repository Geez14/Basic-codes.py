#develop by Monabbar Anjum.
#COPYRIGHT reserved to developer
import random
s = random.randint(1,100)
print("hint- Number is lying between 1 and 100")
for i in range(10):
    print("Tries left: ",10-i)
    Input = int(input("input Integer: "))
    if Input == s :
        print("Congratulations!", end=" ")
        print("Your IQ is above 100")
        break
    elif Input < s :
        print("Increase The Value Of Integer")
    else :
        print("Decrease The Value of Integer")
print("Answer is: ",s)
print("Reload this programm to use it again.")

