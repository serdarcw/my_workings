

#empty_tuple = ()

#tuple1 = empty_tuple()
#print(empty_tuple)
#print(type(empty_tuple_1))


#empty_tuple = tuple()
#To create a Tuple




# tuple nin içine sayı yerleştirmek için
#tuple1 = tuple(range(1,11))
#print(tuple1)





#planets = 'mercury', 'jupiter', 'saturn'

#print(planets)
#print(type(planets))

#Output : ('mercury', 'jupiter', 'saturn')
#<class 'tuple'>







#my_tuple=(1, 4, 3, 4, 5, 6, 7, 4)
#my_list = list(my_tuple)
#print(type(my_list), my_list)
#Output : Bir tuple ı listeye çevireviliriz. Yukarıda görüldüğü şekli ile uygulanırsa 
#bu kolaylıkla yapılabilir.
#<class 'list'> [1, 4, 3, 4, 5, 6, 7, 4]




#my_list = [1, 4, 3, 4, 5, 6, 7, 4]

#my_tuple = tuple(my_list)

#print(type(my_tuple), my_tuple)
#
#Output :  Benzer şekilde bir list de bir tuple a dönüşebilir. ve çıktısı aşağıdaki gibi olur
#<class 'tuple'> (1, 4, 3, 4, 5, 6, 7, 4)






#mountain = tuple('Ozlem')
#print(mountain) 
#Output: verilen bir string iterable bir hale getirilebilr. Benzer şey list'de de yaplabilir. 
# ('O', 'z', 'l', 'e', 'm')






#try_tuple = ('love')
#try_tuple_1 = ('love', 'happy', 'anger', 'eager')
#
#print(try_tuple)
#print(try_tuple_1)
#print(type(try_tuple)) # ilk ifade str olarak görülür, sonuna 
                         # virgül konursa tuple görür

#Output :
#love
#('love', 'serkan')
#<class 'str'>





#mix_value_tuple = (0, 'bird', 3.14, True)
#
#print(len(mix_value_tuple))
#Output : 4





#even_no = (4, 34, 23)
#print(even_no[0])    
#print(even_no[1])    
#print(even_no[2])   

#Output : İndexleme list e benzer şekilde yapılır.
#0
#2
#4


#notes = (4, 34, ('Serdar', 'Bilal', 'Selim'), 'mandalina', 'Şeftali')
#notes_1 = notes[2]
#notes_2 = notes[:2:2]
#print(notes_2)





#Not : List lerin aksine tuple larda item assign edilemez
#aşağıdaki örnekte ikisi arasındaki fark rahatlıkla görülebilir.
# Bu örneği göstermeyeblirsin

#city_list = ['London', 'Ankara', 'Sn.Petersburg', 'Marakesh']
#
#city_list[0] = 'Athens'
#city_list[1] = 'Cairo'
#print(city_list)
#output : ['Athens', 'Cairo', 'Moskow', 'Dublin']






#city_list = ['London', 'Ankara', 'Sn.Petersburg', 'Marakesh']

#city_tuple = tuple(city_list)

#city_tuple[0] = 'New York'  # you can't assign a value

#Output : 
#Traceback (most recent call last):
#  File "/Users/ODG/Documents/Belgeler/My Cloud Engineering/Python/Tuples.py", line 131, in <module>
#    city_tuple[0] = 'New York'  # you can't assign a value
#TypeError: 'tuple' object does not support item assignment






# vowels tuple
#vowels = ('a', 'e', 'i', 'o', 'i', 'o', 'e', 'i', 'u')
# count element 'i'
#count = vowels.count('i')
# print count
#print('The count of i is', count)
# count element 'p'
#count = vowels.count('p')
# print count
#print('The count of p is ', count)
#The count of i is: 3
#The count of p is: 0







## random tuple
#random = ('a', ('a', 'b'), ('a', 'b'), [3, 4])

# count element ('a', 'b')
#count = random.count(('a', 'b'))
#print (count)
#print("The count of ('a', 'b') is:", count)

#count element [3, 4]
#count = random.count([3, 4])
#print (count)
#print("The count of [3, 4] is", count)

#Output : 
#The count of ('a', 'b') is: 2
#The count of [3, 4] is: 1




# Tuples may be nested:

#u = t, (1, 2, 3, 4, 5)
#print(u)
#Output : ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))




# Tuples are immutable:

#t = (234,567,765,8978,5435)
#t[0] = 88888
#print(t[0])

#Traceback (most recent call last):
#  File "/Users/ODG/Documents/Belgeler/My Cloud Engineering/Python/Tuples.py", line 201, in <module>
#    t[0] = 88888
#TypeError: 'tuple' object does not support item assignment




#Peki tuple lara bir şey eklemek istersek ne yapalım
# Önce list yapıp ekleyip sonra tuple haline getirmeliyiz.
#x = ("apple", "banana", "cherry")
#y = list(x)
#y[1] = "kiwi"
#x = tuple(y)
#
#print(x)






# but they can contain mutable objects:
#v = ([1, 2, 3], [3, 2, 1])
#print(v)
#Output : 
#([1, 2, 3], [3, 2, 1])


#birden fazla tuple toplanarak yeni bir tuple oluşturulabilir
#tuple1 = ("a", "b" , "c")
#tuple2 = (1, 2, 3)
#
#tuple3 = tuple1 + tuple2
#print(tuple3)
















