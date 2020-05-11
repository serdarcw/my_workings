
num = int(input("Please enter a number between 1 and 100: "))

if int(num)%3 == 0 and int(num)%5 != 0: print("Fizz")
elif int(num)%5 == 0 and int(num)%3 != 0: print("Buzz")
elif int(num)%5 == 0 and int(num)%3 == 0: print("FizzBuzz")
else:print(str(num))
