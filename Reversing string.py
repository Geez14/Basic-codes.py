# works only in input taking ide only.
while True:
    drop = str(input("Enter some text to be reverse\n--> "))
    text = drop[::-1]
    print(text)
    function = str(input("Do you want to continue? y/n\n--> "))
    function = function.upper()
    if function == "Y":
        continue
    else:
        break
print("see you later!")
