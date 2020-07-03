#def printing(B):
#    print(f'With this function you can print {B}')
#
#printing('Serkan')


##This function, which we defined, gives the sum of the squares of arguments. Let's call and use it.#This function, which we defined, gives the sum of the squares of arguments. Let's call and use it.
#def first_function(argument_1, argument_2) :
#    print(argument_1**2 + argument_2**2)
#
#first_function(2,3)


#💡Tips:
#When there is no indentation, it means that the definition process of the function must end.


##Bu fonksiyonda 3ncü örnekte görüldüğü üzere string eğer çarpma ilekullanılırsa
##stringin yazımında tekrar miktarını verecektir.
#def multiply(a, b) :
#    print(a * b)
#
#multiply(3, 5)
#multiply(-1, 2.5)
#multiply('amazing ', 3)  # it's really amazing, right?




#Burada iki fonksiyon da aynı sonucu üretir ama fark nerede oluşur?
#İlk fonksiyon sadece içine yazılan ifadelerin çıktısını verir. Ama ikinci fonksiyon
#numerik tipte sahip bir değer üretir. Bu fark type çalıştırılıp görülebilir
#Bunun farkı da şurada çıkar, ilk fonksiyon değer üretmez ama ikinci fonksiyon bir değer üretir ve 
#bu değer sonrasında da kullanılabilir.

#def multiply_1(a, b) :
#    print(a * b)  # it prints something
#
#def multiply_2(a, b) :
#    return a * b  # returns any numeric data type value
#
#multiply_1(10, 5)
#print(multiply_2(10, 5))




#Q: What is the return keyword used for in Python?
#A: The purpose of a function is to receive the inputs and return some output. The return is a Python #statement which we can use in a function for sending a value back to its caller. 


#from datetime import datetime
#
#def print_time():
#    print('task completed')
#    print(datetime.now())
#    print()
#print_time()



##Arguments vs Parameters
#
##parametre ve argument fonksiyonlarda kullanılan iki tabirdir ve birbirleinie çok yakındır anlam ##olarak. Bunu şöyle düşünebiliriz f(x)=2x+5, f(5)=15 yazımında x parametredir, biz buna ##fonksiyonlarda değişken deriz ama bu x=5 yazıldığında buradaki 5 argument dir. Yani parametre yerine
##fonksiyonda yazılan değere karşılık gelir.
#
#def who(first, last) :  # 'first' and 'last' are the parameters(or variables)
#    print('Your first name is :', first)
#    print('Your last name is :', last)
#
#who('Guido', 'van Rossum')  # 'Guido' and 'van Rossum' are the arguments
#print()
#who('Marry', 'Bold')  # 'Marry' and 'Bold' are also the arguments

#Parametrede dikkat edilmesi gereken en önemli noktalardan biri de şudur: fonksiyon yazımında 
#eğer iki parametre verişmiş ise fonksiyon çağırıldığında bu iki parametre yerine iki tane 
#argument yazma gerekliliğidir. Eğer bir tane yazılırsa  error mesajı ilekarşılaşılacaktır.



#def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
#    print("-- This parrot wouldn't", action, end=' ')
#    print("if you put", voltage, "volts through it.")
#    print("-- Lovely plumage, the", type)
#    print("-- It's", state, "!")


#parrot(1000)                                          # 1 positional argument
#parrot(voltage=1000)                                  # 1 keyword argument
#parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
#parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments 
#parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
#parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

#Tips:
#If you have noticed the positions of the parameters voltage and action, 
# sequences or positions don't #matter when using keyword arguments.



##Aşağıdaki yazımlar hata mesajı veren yaımlardır. Bu yanlışlıklara düşmemek
#için dikkate etmek gerekmektedir.

#parrot()                     # required argument missing
#parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
#parrot(110, voltage=220)     # duplicate value for the same argument
#parrot(actor='John Cleese')  # unknown keyword argument








#En başta keyword argument tanımlanmış continent=Europe olarak
#eğer fonksiyon çağırılırken bu değere bir argument girilmez ise bu durumda
#default olarak Europe alınacaktır. İlk örnekte görüldüğü gibi
#Ama ikinci ve üçüncü örnekte de gözüldüğü üzere, yeni bir atama yapılabilir. Bu atama
#direk continent=Asia yazılarak da olabilir, o parametrenin pozisyonuna yeni atama yazılarak da 
#yapılabilmektir. Üçüncü örnek, pozisyone yeni argument i lyazarak yapılan yeni atamayı göstermektedir

#def city(capital, continent='Europe'):
#    print(capital, 'in', continent)
#
#city('Athens')  # we don't have to pass any arguments into 'continent'
#city('Ulaanbaatar', continent='Asia')  # we can change the default value by kwargs
#city('Cape Town', 'Africa')  # we can change the default value by positional args.





#*args and *kwargs
#bir fonksiyon yazdığımızda bazen fonksiyonu çağırmak istediğimizde içine 
#yazacağımız argument değerinin sayısını bilemeyiz. Bu durumda *args veya *kwargs kullanılır.

#def multp(a,b):
#    return a*b
#
#print(multp(5,7))
#
#Mesela yukarıdaki örnekte kaç sayı yazacağımı biliyorum ama ya çarpacağım eleman sayısını bilmiyorsam bu durumda aşağıdaki kulanım öne çıkar. Bu kullanımda keyf sayıda yazılan argument'ler 
#tuple olarak saklanır.

#def multpl(*nums):
#    multp=1
#    for i in nums:
#        multp *= i
#    return multp
#
#print(multpl(4,5,6,7,8))



#Peki ben bu sayıları bir listenin içine yazarsam: Bu durumda

#def multpl(*nums):
#    multp=1
#    for i in nums:
#        if type(i)==int or type(i)==float:
#            multp *= i
#    return multp
#
#mylist=[4,5,6,7,8]
#print(multpl(mylist))

#bu durumda içerideki listeyi bir tek eleman olarak alır ve o eleman da int ya da float olmadığı için 
#1 e dönecektir. Ancak ben lisyenin başına * koyarsam bu, listeyi unpack et demek olur. Yani;


#def multpl(*nums):
#    multp=1
#    for i in nums:
#        if type(i)==int or type(i)==float:
#            multp *= i
#    return multp
#
#mylist=[4,5,6,7,8]
#print(multpl(*mylist))
#print(*mylist) # Burada nasıl unpack ettiğini görebiliriz.




#Eğer positional argument değil de keyword argument ise kullanmak istediğim bakalım nasıl oluyor:

#def properCal(**fruits):
#    for i in fruits.items():
#        print(i)
#    print(type(fruits))
#
#B={'Ananas': 65, 'Kiwi':40, 'Mango':78, 'Kavun':46}
#properCal(**B) #Burada çağırırken ** koymak çok önemli. Bu unpack et demek oluyor.



#Eğer standart parametre il bu positional argument ve keywork argument koyacak olursak bu durumda #sıralama önem kazanır
#
#def myFunc(arg1, arg2, *args, **kwargs): #yazımındk gibi bir sıra izlenmek zorunluluğu vardır.
    

deger = int(input('Lutfen hesaplamak istediginiz n değerini giriniz : '))
listem =[*range(1,deger+1)]
def factorl(*args):
    multpl = 1
    for i in args:
        multpl *= i
    return multpl

toplam=0
print(listem)
for i in listem:
    toplam+=(factorl(*list(range(1,i+1))))/i
print(toplam)




