#yas = int(input('Lütfen yaşınızı giriniz : '))

#if yas >= 18:
 #   print('Mekana girebilirsiniz!')    #if'in yanında verilen koşul sağlanırsa
                                       #bu durumda altındaki girintiden başlayın koşul uygulanır
                                       # yok eğer if in koşulu sağlanmıyorsa bu durumda else
                                       # uygulanır  

#else:
 #   print('Mekana giremezsiniz!')



#note = float(input('Lütfen Notunuzu Giriniz : '))
#
#if note>= 90:
#    print('AA aldınız')
#
#elif note>75:
#    print('BA aldınız')             # elif için yukarıdaki aralık gözönünde bulundurup 
#                                    # 90 ile 85 denmesine gerek yoktur
#                                    # elif yukarıdaki koşulun sağlanmadığı zaman manasına geldiği
#                                    #için zaten otomatikman 90 dan küçük alınmış olur.
#elif note>60:
#    print('CC aldınız')
#else:
#    print('desten kaldınız')



#WHILE LOOPS


#number = 0
#
#while number < 6:
#    print(number)
#    number += 1
#print('now, number is bigger or equal to 6')

#Avoid ! :
#If we make a logical mistake in the loop variable (since you don’t 
#increase your variable, a condition never becomes False and can work forever), 
#we can start an infinite loop! For this reason, we have to specify a condition 
#for the loop to give False to exit the loop.




#my_list=["a", "b", "c", "d", "e"]
#
#a = 0
#
#while a < len(my_list):
#    print('square of {} is : {}'.format(a, a**2))
#    a+=1








#answer = 44
#
#question = 'What number am I thinking of?  '
#print ("Let's play the guessing game!")
#
#while True:
#    guess = int(input(question))
#
#    if guess < answer:
#        print('Little higher')
#    elif guess > answer:
#        print('Little lower')
#    else:  # guess == answer
#        print('Are you a MINDREADER!!!')
#        break


name = input('Please enter your first name : ')
dict_1 = {'name': 'Serkan', 'passwd':'@12'}

if name == dict_1['name']:
    print(f"Hello, {dict_1['name']} The password is : {dict_1['passwd']}")
else:
    print("Hello "+name+"!"+"See you later.")
























































