#word =input("Please enter your word : ")
#
#word_1 =set(word)
#
#right = {'y', 'Y','h', 'H', 'n', 'N', 'u','U', 'j','J', 'm', 'M', 'i','I','k','K', ',', 'o', 'O', 'l', 'L', '.', 'p', 'P', ';', '/'}
#left = {'q', 'Q', 'a', 'A', 'z', 'Z', 'w', 'W', 's', 'S', 'x', 'X', 'e', 'E', 'd', 'D', 'c', 'r', 'f', 'v', 'V', 't', 'T', 'g', 'G', 'b', 'B'}  
#
#
## Burada girilen kelimeyi küme elemalarına ayırdım. Sonrasından sağ el ve sol el in eriştiği harflarin kümesini oluşturdum
## Şu kontrolü yaptım sonrasında; eğer word_1 in left ile arakesitinden word_1 kümesi geliyorsa demek ki word_1 tamamen
## left'in harfleri ile oluşturulabiliyor. Benzer şekilde right için de düşünülebilir. Buna göre word_1 ile right in arakesiti 
## ile word_1 ile left in arakesiti tamamen word_1 olmaması durumunda demek ki kelime her iki harf grubu ile yzılabiliyor demektir.
## o zaman aşağıdaki kontrol meseleyi çözer.
#print("Is this comfortable words    : ", word_1 & right != word_1 and word_1 & left != word_1)








word =input("Please enter your word : ")

word_1 =set(word.lower())

right = {'y','h', 'n', 'u', 'j', 'm', 'i','k', ',', 'o', 'l', '.', 'p', ';', '/'}
left = {'q', 'a', 'z', 'w', 's', 'x', 'e', 'd', 'c', 'r', 'f', 'v', 't', 'g', 'b'}  


# Burada girilen kelimeyi küme elemalarına ayırdım. Sonrasından sağ el ve sol el in eriştiği harflarin kümesini oluşturdum
# Şu kontrolü yaptım sonrasında; eğer word_1 in left ile arakesitinden word_1 kümesi geliyorsa demek ki word_1 tamamen
# left'in harfleri ile oluşturulabiliyor. Benzer şekilde right için de düşünülebilir. Buna göre word_1 ile right in arakesiti 
# ile word_1 ile left in arakesiti tamamen word_1 olmaması durumunda demek ki kelime her iki harf grubu ile yzılabiliyor demektir.
# o zaman aşağıdaki kontrol meseleyi çözer.
print("Is this comfortable words    : ", word_1 & right != word_1 and word_1 & left != word_1)
