num=int(input("please enter your number : "))
count=0
if num==2:
    print(f"{num} is a prime number")
elif num==1:
    print(f"{num} isn't a prime number")
else:
    for i in range(2,num):
        if num%i==0:
            count+=1
    if count>1:
        print(f"{num} isn't a prime number")
    else:
        print(f"{num} is a prime number")