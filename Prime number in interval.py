print("do number ke bich prime number\n dhunde ga ye program.")
#number can be in any order,ie you can give a>b or b>a
print("ye programm positive integer ke liye kaam \n karta hai")
print("Dhayan rakhen! 1 prime number nahi hai.")
print("you can Enter number in any order!")
print("Both number will be inclusive!")
a = int(input('A->  '))
b = int(input('B->  '))
if a > b:
	a,b = b,a
if a > 1 and b > 1:
    print("Prime number between",a,"&",b)
#ye for loop a ko dale ga number ko i me dale gaor woh
#number 2nd for loop me jaye ga
    for i in range(a,b+1):
#2nd for loop i = a le liye if condition check kare ga
#aur augar condition true hota hai toh 2nd forloop 
#band ho jaye ga aur wapas se i 1st for loop me jaye ga
#iss baar 1st for loop i= a+1 value 2nd for loop me de ga.
        for j in range(2,i):
#agar condition false ho jati hai toh 2nd for loop chalta rahega jab tak
#j ke liye aur koi range na bache isse hoga ki 2nd for loop ko pata chaljaye ga
#ki jo number i hai woh 2 se i ke range me kisi se completely divisible nahi hai
#toh 2nd forloop i ka value else me send ka ke 
#wapas 1st forloop me chala jaye ga
#aur 1st for loop i ka value tab tak 2nd forloop ko dega jabtak
#1st for loop ka range pura na ho jaye.
            if i % j == 0:
                break
        else:
             print(' ',i)
else:
    print("invalid input है मूर्ख :(")
#:))
print('!!!MISSION ACCOMPLISHED!!!')
