#empty_seat = 45
#
#if empty_seat > 34:  # in this case, 14>3=True, so the body will execute
#    print('there is still seat to sit')

# Cok Onemli : Note that the condition ends with a colon and
#  a new line starts with an indentation.


# Tips: Note that, else doesn't require any condition 
# and the body2 requires 4-space indentation here.



#course = 'clarusway'
#
#if course == "clarusway":
#    print("you guaranteed the job")
#else:
#    print("think about it again")






#number = 5
#if number <= 3:    
#    print("Number is smaller than or equal to 3") 
#else:  # Optional clause (you can only have one else)
#    print("Number is bigger than 3")





#basket = ['apple', 'peach', 'blackberry']
#fruit ='apple'
#
#if fruit not in basket:
#    print('I have already')
#else:
#    print('I can have a little')








#weight = 80
#
#if weight > 100:
#    print("That's too heavy!")
#elif weight > 75:
#    print("I can lift that!")
#else:
#    print("That's too light!")





#if audience == "kid":
#    print("it is free to go to cinema")
#elif audience == "teen":
#    print("discounted price!")
#elif audience == "adult":
#    print("normal price")
#else:
#    print("No such audience, stay at your home!")






#Short Hand If Else

#a = input()
#b = input()
#if a > b: print("a is greater than b")
#elif a==b: print("a equal to b")
#else: print("b is greater than a")




#a = input()
#b = input()
#print("A") if a > b else print("B")





#a = 330
#b = 330
#print("A") if a > b else print("=") if a == b else print("B")








#AND: her iki şartın da doğru olması gerekir
#a = input('a')
#b = input('b')
#c = input('c')
#if a > b and c > a:
#  print("Both conditions are True")







# OR : en az biri doğru olsa yeter
#a = input('a')
#b = input('b')
#c = input('c')
#if a > b or a > c:
#  print("At least one of the conditions is True")




#Problem:
#
#Create a function that takes two parameters and, if both parameters are strings, add them as if they were integers or if the two parameters are integers, concatenate them.
#
#Examples
#stupid_addition(1, 2) ➞ "12"
#
#stupid_addition("1", "2") ➞ 3
#
#stupid_addition("1", 2) ➞ None
#Notes
#If the two parameters are different data types, return None.
#All parameters will either be strings or integers.


#Solution:
a = input()
b = input()
if type(a)==str and type(b)==str:
    print(int(a)+int(b))
elif type(a)==int and type(b)==int:
    print(str(a),str(b))
else:
    print(None)

