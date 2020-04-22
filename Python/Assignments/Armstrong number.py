num = input("Please enter your number : ")
a = len(num)
sum = 0
if int(num)<0:
    print("Please enter positive number")
else:
    for i in num:
        sum +=int(i)**a
    if sum == 0:
        print("This is an Armstrong number")
    else:
        print("This is not an Armstrong number")
