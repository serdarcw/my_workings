#empty_set1 = set()
#empty_set2 = {} 
#print(type(empty_set1))
# Boş bir set oluşturmanın tek yolu set() yazmaktır, eğer {} kullanılırsa bu dictionary olur. 



#class_list1 = {'Serhat'}
#class_list2 = {'Hasan', 'Sami', 'Serkan', 'Serdar', 'Kerim', 'Tolga', 'Berk', 'Tunç'}
#print(class_list2)
#print(type(class_list1))
#Önemli not = set'lerde hem her eleman bir kere geçer hem de indexlenebilir değildir. 
# Tekrar tekrar yazdırılırsa aynı setin elemanlarının değiştiği görülür






# kümenin elemanlarının yazım kuralı şudur: eleman birden fazla defa varsa bir kere yazılır. 
#Buradaki set'ler de bu şekilde hareket eder. elemanları yazılırken tekrar eden elemanlar bir defa yazılır.

#a = set('abracadabra')
#
#print(a) 




#s = set('unselfishness')
#
#print(s) 







#flower_list = ['rose', 'violet', 'carnation', 'rose', 'orchid', 'rose', 'orchid']
#flowerset = set(flower_list)
#flowerlist = list(flowerset)
#flowerlist1 = set(flowerlist)
#
#print(flowerset) 
#print(flowerlist)
#print(flowerlist1)
# Aynı eleman listeye eklenmeye çalışılırsa, liste içine alır ama set bunu göstermez
#zira bir eleman set de birden fazla geçmez









# union işlemi olarak tanımlanan işlemdir. Kümelerdeki birleşme özelliği gibi hareket eder.
#Bir elemanın birleşim kümesine girmesi için birleşime giren kümelerde en az bir defa bulunması yeter.


#a = set('abracadabra')
#b = set('alacazam')
#
#print(a)
#print(b)
#print(a | b)  # same as '.union()' method
#print(a.union(b)) # unification of a with b






#Kümelerdeki kesişim işlemidir burada uygulanan. her iki kümede ortak olan elemanları alır. Case sensitive dir.
#a = set('karaman')
#b = set('aydın')
#
#print(a & b)  # same as '.intersection()' method
#print(a.intersection(b)) # intersection of a and b






#x kümesinin içerisinden y kümesindeki elemanları çıkarır.
#x = {"apple", "banana", "cherry"}
#y = {"google", "microsoft", "apple"}
#
#z = x.difference(y) 
#
#print(z)






# isssubset bize dıştaki kümenin içte yazılan kümenin bir altkümesi olup olmadığını verir. Boolean olarak çalışır
#x = {"a", "b", "c"}
#y = {"f", "e", "d", "c", "b", "a"}
#
#z = y.issubset(x) 
#
#print(z)






#simetrik diffrence ortak olanların dışındaki elemanları küme halinde sunar
#setx = set(["apple", "mango"])
#sety = set(["mango", "orange"])
##Symmetric difference
#setc = setx ^ sety
#print(setc)






#ilk kümenin ikinci küme ile ortak elemanı varsa False basar
#yoksa true basar. ortak eleman var mı yok mu ona bakar

#x = {"z", "y", "x"}
#y = {"f", "e", "d", "c", "b", "a"}
#
#z = y.isdisjoint(x) 
#
#print(z)








# Küme elemanlarının içerisinden istenilen elemanı çıkarmaya yarar.
#Note: Eğer listeden çıkarılması istenen eleman listede yoksa remove error verir.
#a = set('abracadabra')
#a.remove('b') # 'c elemanını kümeden siler
#print(a)






# Küme elemanlarının içerisinden istenilen elemanı çıkarmaya yarar.
#Note: Eğer listeden çıkarılması istenen eleman listede yoksa discard error vermez.
#class_list = {"Salih", "Sibel", "mucahit", "Talha"}
#
#class_list.discard("mucahit")
#
#print(class_list)



#s = {'foo', 'bar', 'baz', 'qux'}
#s -= {'foo'}
#print(s)









# c elemanı halihazırda kümede bulunduğu için ekleseniz bile gözükmez.
# ama z elemanı küme elemanı olarak bulunmadığı için eklendiği output da gözükür.

#a = set('abracadabra')
#
#a.add('c') 
#a.add('z') 
#print(a)






#a = {True, 3.45,34}
#b = set([1,2,2,3,4,5])
#c = {1,2,3,4}
#d = set((1,2,3,4))
#print(a)
#print(b)
#print(c)
#print(d)
#
## Set'lerin tüm elemanları iterable olmak zorundadır. Hashable olan herşey yerleştirilebilir ama unhashable olanlar yerleştirilemez
#Unhashable      : List , Carray , sets , Dictionary , Collections.deque etc.
#hashable objects: integer ,float ,tupple ,frozen sets ,string, Boolean etc





# listeye çoklu eleman eklemek için update attribute u kullanılır
#class_list = {"Salih", "Sibel", "mucahit", "Talha"}
#
#
#class_list.update(["Aysun", "Henry", "Huseyin"])
#
#print(class_list)







#a = set('abracadabra')
#print(len(a))







#Bu şekilde bir yazım listenin içerisinde aranan elemanın var olup olmadığını kontrol eder.
#Bu yazım ayrıca conditions'lrda da kullanılabilir.

#shop_list = {"apple", "banana", "cherry"}
#
#print("cinnemon" in shop_list)
#print("banana" in shop_list)







# listeye çoklu eleman eklemek için update attribute u kullanılır
#shop_list = {"apple", "banana", "cherry"}
#
#shop_list.update(["orange", "mango", "grapes"])
#
#print(shop_list)








#DİKKAT: set'ler unordered oldukları için her run a bastığımda farklı bir elemanı çıkarıyor.
#hangi elemanı çıkaracağını bilemiyoruz
#
#bazaar = {"onion", "papato", "cucumber"}
#
#bazaar.pop()
#
#print(bazaar)








#clear attribute set'in içindeki herşeyi siler
#bazaar = {"onion", "papato", "cucumber"}
#
#bazaar.clear()
#print(bazaar)













#Exercise:

#Given a list of numbers, write a function that returns a list that...
#
#Has all duplicate elements removed.
#Is sorted from least to greatest value.
#Examples
#unique_sort([1, 2, 4, 3]) ➞ [1, 2, 3, 4]
#
#unique_sort([1, 4, 4, 4, 4, 4, 3, 2, 1, 2]) ➞ [1, 2, 3, 4]
#
#unique_sort([6, 7, 3, 2, 1]) ➞ [1, 2, 3, 6, 7]
#
#return sorted(list(set(lst)))


# def unique_sort(lst):
#   lst = set(lst)
#   lst = list(lst)
#   lst.sort()
#   return lst




