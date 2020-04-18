#a = input('lütfen sayı giriniz  : ')
#b = input('lütfen sayı giriniz  : ')
#c = input('lütfen sayı giriniz  : ')

#print('sayıların toplamı :', int(a)+int(b)+int(c))




print('oyuncu kaydetme programı')
isim    =input('Lütfen oyuncu ismini giriniz : ')
soyad   = input('Lütfen oyuncunun soyadını giriniz : ')
takim   =input('Oyuncuun takımını giriniz : ')

bilgiler =[isim, soyad, takim]
print("Bilgileriniz Database'e kaydediliyor.....")
# aşağıdaki iki metod kaydedilen bilgilerin farklı iki yazma şeklidir. ayrı ayrı denenebilir
#print('Oyuncunun adı :', isim, 'Oyuncunun soyadı :', soyad, 'Oyuncunun takımı :', takim, sep='  ')
print("Oyuncunun adı :{}\nOyuncunun soyadı :{}\nOyuncunun takımı {}".format(bilgiler[0],bilgiler[1],bilgiler[2]))