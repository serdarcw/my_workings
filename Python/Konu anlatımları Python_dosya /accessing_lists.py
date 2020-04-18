#colors = ['red', 'purple', 'blue', 'yellow', 'green']
#print(colors[2])  # If we start at zero, 
## the second element will be 'blue'.
#sonuç : blue





#city = ['New York', 'London', 'Istanbul', 'Seoul', 'Sydney']
##
#city_list = []
#city_list.append(city) # we have created a nested list
##
#print(city_list)






#sonuç : [['New York', 'London', 'Istanbul', 'Seoul', 'Sydney']]
#Burada citynin sadece bir eleman olarak eklendiğini gözden kaçırma. Burada city yerine 'city' 
# olarak girilirse city'i tek başına ekleyecektir.




#city_list = [['New York', 'London', 'Istanbul', 'Seoul', 'Sydney']]
#print(city_list[0]) # access to first and only element




#city_list = [['New York', 'London', 'Istanbul', 'Seoul', 'Sydney']]
#print(city_list[0][4])
#
#Sonuç : Sydney, işlem soldan sağa ilerler. Önce listenin sıfırıncı elemanını alır 
#sonrasında o eleman liste olduğu için 4'üncü indexteki elemanı alır






#city_list = [['New York', 'London', 'Istanbul', 'Seoul', 'Sydney']]
#print(city_list[0][3][3])

#Sonuç : u, 0 incı elemanının (ki bu liste, 4 üncü indexinin, 3'üncü indexteki harfini çeker)




#fruits = ['apple', 'banana', 'watermelon', 'orange', 'mango', 'avocado']
#
#fruit_list = []
#fruit_list.insert(0, fruits)
#print(fruit_list[0][2][7])




#numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17]
#print(numbers[2:5])  
# 
# we get the elements from index=2 to index=5 (5 is not included) sonuç = [5,7,9]


#count = list(range(45))
#print(count)
#
#print(count[0:39:3])

#[0:40:3] ifadesinde ilk sayı başlangıç noktasını verir ve bu nokta aralığa dahildir, 
# ikinci sayı yani 39 bitiş noktasını verir ve bu nokta aralığa dahi değildir. 39 çıktıda dahil değil dikkat
# üçüncü sayı ise ilk ifadeden sonra atlama aralığını verir
#[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]



#my_list[:]: returns the full copy of the sequence
#
#my_list[start:] : returns elements from start to the end element
#
#my_list[:stop] : returns element from the 1st element to stop-1
#
#my_list[::step] : returns each element with a given step





#animals = ['elephant', 'bear', 'fox', 'wolf', 'rabbit', 'deer', 'giraffe']
#
#print(animals[:])  # all elements of the list
#
#sonuç : ['elephant', 'bear', 'fox', 'wolf', 'rabbit', 'deer', 'giraffe']




#animals = ['elephant', 'bear', 'fox', 'wolf', 'rabbit', 'deer', 'giraffe']
#print(animals[3:])
#sonuç : ['wolf', 'rabbit', 'deer', 'giraffe']




#animals = ['elephant', 'bear', 'fox', 'wolf', 'rabbit', 'deer', 'giraffe']
#print(animals[:5])
#Sonuç : ['elephant', 'bear', 'fox', 'wolf', 'rabbit']





#animals = ['elephant', 'bear', 'fox', 'wolf', 'rabbit', 'deer', 'giraffe']
#print(animals[::2])
#
#['elephant', 'fox', 'rabbit', 'giraffe'], belirtilen değer ararlığını atlayarak gider



#city = ['New York', 'London', 'Istanbul', 'Seoul', 'Sydney']
#print(city[-3])
#sonuç : Istanbul, geriden indexleme -1 den başlar





#reef = ['swordfish', 'shark', 'whale', 'jellyfish', 'lobster', 'squid', 'octopus']
#print(reef[-3:])
#
#
#sonuç : ['lobster', 'squid', 'octopus']



#reef = ['swordfish', 'shark', 'whale', 'jellyfish', 'lobster', 'squid', 'octopus']
#print(reef[:-3])
#sonuç : ['swordfish', 'shark', 'whale', 'jellyfish']




#reef = ['swordfish', 'shark', 'whale', 'jellyfish', 'lobster', 'squid', 'octopus']
#print(reef[::-1])  # we have produced the reverse of the list
#Sonuç : ['octopus', 'squid', 'lobster', 'jellyfish', 'whale', 'shark', 'swordfish']





#reef = ['swordfish', 'shark', 'whale', 'jellyfish', 'lobster', 'squid', 'octopus']
#print(reef[::-2])
#sonuç : ['octopus', 'lobster', 'whale', 'swordfish'] negatif artış verirseniz, sondan başlar ve reverse side 
#belirlenen miktarda artış veriyor













#city = ['New York', 'London', 'Istanbul', 'Seoul', 'Sydney']
#city_list = []
#city.append(city_list) # we have created a nested list

#print(city)
#sonuç : ['New York', 'London', 'Istanbul', 'Seoul', 'Sydney', []]


#odd_no = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#print(odd_no[7:3:-1])
#print(odd_no[2:6:-1])
#
#Sonuçlar
#[8, 7, 6, 5]
#[]

#Negatif artuş verildiğinden ilk index ikinci indexten büyük alınmalıdır. Diğer türlü örnekte görüldüğü
#gibi boş liste basar

