#while True:

num=int(input("please enter your number : "))
count=0
for i in range(2,round((num)**(0.5))):
    if num%i==0:
        count+=1
if count>1:
    print(f"{num} isn't a prime number")
else:
    print(f"{num} is a prime number")

