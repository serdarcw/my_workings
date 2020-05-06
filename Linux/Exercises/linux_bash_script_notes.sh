Örnek 1:
#!/bin/bash
echo "Hello World"

Not: Herhangibir script dosyası "$ bash hello-world.sh"
"$ ./hello-world.sh" yazarak çalıştırılabilir.





Örnek 2 :
Not: echo print etmek istediğimiz fade için kullanılır.,
The -e opsiyonu echo için içeride yazılan stringdeki özel karakterlerin fonksiyonlarını
geri kazandırır. 
 -n opsiyonu echo komutunda yeni bir line vermeden yazmayı sağlar



#! /bin/bash
echo "Printing text"
echo -n "Printing text without newline"
echo -e "\nRemoving \t special \t characters\n"







Receive Input from User
Getting user input is crucial to implement user interaction in your scripts. The below shell script example will demonstrate how to receive user input within a shell program.

#!/bin/bash

echo -n "Enter Something:"
read something

#read -p "Enter Something:" something

echo "You Entered: $something"







Arithmetic Expression

Aritmetik işlemlerin yazımında iki farklı yol uygulanır
1. let yazımı işlemlerin
Bu yazımda aritmetik işlemlerin olacağı satır let ile başlar.
Dolar işareti kullanılmaz

2. çift parantez kullanarak
Bu yolda dolar kullanılabilir ve aritmetik işlem çift parantezler içine alınır.

1.yol ile
#!/bin/bash

num1=3
num2=5

let total=num1+num2
let diff=num1-num2
let mult=num1*num2
let div=num1/num2

echo "Total = $total"
echo "Substution = $diff"
echo "Multiplication = $mult"
echo "Division= $div"




2. yol
#!/bin/bash

num1=15
num2=3

(( total = num1 + num2 ))
(( diff = num1 - num2 ))
(( mult = num1 * num2 ))
(( div = num1 / num2 ))

echo "Total = $total"
echo "Substution = $diff"
echo "Multiplication = $mult"
echo "Division= $div"


Not: Burada şuna dikkat edilmesi gerekir
Eğer aritmetik işleme hemen bir değer atanacaksa bu durumda
total =$((num1+num2))
ataması yapılır

total=$(( num1 + num2 ))
diff=$(( num1 - num2 ))
mult=$(( num1 * num2 ))
div=$(( num1 / num2 ))


eğer tanımlama parantez içinde yapılacaksa bu durumda parantez başlarında $ kullanılmaz

(( total = num1 + num2 ))
(( diff = num1 - num2 ))
(( mult = num1 * num2 ))
(( div = num1 / num2 ))








increment/decrement operations

#++ nın öncesinde ve sonrasında kullanılmasında fark vardır. Eğer yeni değer
#atanırken öncesine ++ konursa x'i bir arttırır ardından y yi atar. Böylelikle
#hem x hem de y artar. ama sonrasına ++ konursa o zaman x değişmez ama y bir artar

Örnek:
x=5
y=$((x++))
echo x: $x
echo y: $y




Örnek:
num1=14
num2=2

echo total=$((num1+(num2++)))
echo $num2

echo "$total"




num1=13
num2=3

echo total=$((num1*(num2--)))
echo $num2

echo "$total"






Örnek

#Ask user to enter two numbers to variables num1, num2
#Calculate the substution of 2 numbers
#Print the result and decrease it by 1
#Print the new value of the result
#find while finding the total of two, substitute 1 by num2 but
#total doesn't affect this summation




read -p "Please enter your 1st number : " num1
read -p "Please enter your 2nd number : " num2

let sub=$num1-$num2
echo sub=$((sub++))
echo son_toplam = $sub
echo $(( num1 + num2++ ))
echo $num2












Relation Pperators
Önemli not1: Çift parantez yazımlarında içteki operasyonların sağında ve solunda whitespace
bırakmayı unutmayın.

Önemli uyarı2: Çift köşeli parantez kullanımında içerideki variable ların başına $ koylaya gerek yoktur.



-eq
is equal to
if [ $a -eq $b ]
if [[ a -eq b ]]
if (("$a" == "$b"))
Not: İki değerieşitliğini kontrol eder. -eq: equal


-ne
is not equal to
if [ $a -ne $b ]
if [[ a -ne b ]]
if (("$a" != "$b"))
Not: İki değerin birbirinden farklılığını kontrol eder, -ne:not equal



-gt
is greater than

if [[ a -gt b ]] 
if [ $a -gt $b ]
if (( $a > $b ))
Not: Sağdaki değerin soldaki değerden büyük olup olmadığına bakar
-gt:: Greater then




-ge
is greater than or equal to

if [ $a -ge $b ]
if [[ a -ge b ]]
if (( "$a" >= "$b" ))
Not: Sağdaki değerin soldaki değerden büyük ya da eşit olup olmadığına bakar
-ge:Greater or equal



-lt
is less than

if [ $a -lt $b ]
if [[ a -lt b ]]
if (( "$a" < "$b" ))
Not: Sağdaki değerin soldaki değerden küçük olup olmadığına bakar
-lt:: Less then




-le
is less than or equal to

if [ $a -le $b ]
if [[ a -le b ]]
if (("$a" <= "$b" ))
Not: Sağdaki değerin soldaki değerden küçük ya da eşit olup olmadığına bakar
-le:: Less or equal then






IF CONDITIONS
Pythondaki if, elif, else konsepti ile benzerlik gösterir.
farklı şartların kontrol edilip incelenmesini sağlar.

if CONDITION 
then
STATEMENTS
fi





Örnek: 

#!/bin/bash

echo -n "Enter a number: "
read num

if [[ $num -gt 10 ]]
then
echo "Number is greater than 10."
fi







Örnek 1:

verilen sayının bir ya da iki basamaklı olup olmadığını kontrol edelim

read -p "Please enter your number : " n

if [ $n -lt 10 ];
then
echo "It is a one digit number"
else
echo "It is a two digit number"
fi




Örnek 2:

yukarıdaki problemde verilen sayının bir ya da iki basamaklı
çift ya da tek sayı olduğunu kontrol eder

read -p "Please enter your number : " n

if [ $n -lt 10 ];
then
    if (($n%2==0))
    then
        echo "This one digit even number"
    else
        echo "This is one digit odd number"
    fi
else
    if (($n%2==0))
    then
        echo "This is one than more digits and even number"
    else
        echo "This is one than more digits and odd number"
    fi
fi



2. Extended integer test
 	#!/bin/bash
 	
 	read -p "Enter a number : " num
 	
 	if ((num == 10)); then
 		echo "Your number equals 10"
 	
 	elif ((num > 10)); then
 		echo "It is greater then 10"
 	else
 		echo "It is less then 10"
 	fi
 	
 	if (( ((num % 2)) == 0 )); then
 		echo " It is even"
 	fi
 	



#! /bin/bash

if [ -d "/home" ] 
then
    echo "Home directory exists." 
else
    echo "Home Directory does not exists."
fi












AND operatörü

Örnek 3:
Aynı problemi && operatörü kullanarak yapmaya çalışalım: 


#!/bin/bash

echo -n "Enter Number:"
read num

if [[ $num -lt 10  && $num%2 -eq 0 ]]
then
    echo "This number one digit and Even Number"
elif [[ $num -lt 10  && $num%2 -ne 0 ]]
then
    echo "This number one digit and odd Number"
elif [[ $num -ge 10  && $num%2 -eq 0 ]]
then
     echo "This number more digits and Even Number"
elif [[ $num -ge 10  && $num%2 -ne 0 ]]
then
     echo "This number more digits and odd Number"
fi



yukarıdaki yazımın yanında aşağıdaki yazım şeklide kullanılabilir
echo -n "Enter Number : "
read num

if (( $num < 10  && $num%2 == 0 ))
then
    echo "This number one digit and Even Number"
elif (( $num < 10  && $num%2 != 0 ))
then
    echo "This number one digit and odd Number"
elif (( $num >= 10  && $num%2 == 0 ))
then
     echo "This number more digits and Even Number"
elif (( $num >= 10  && $num%2 != 0 ))
then
     echo "This number more digits and odd Number"
fi







OR operatörü

#!/bin/bash

read -p "Enter any number : " num1
read -p "Enter your second number : " num2

if (( $num1 < $num2  || $num1%2== 0 ))
then
    echo "$num1 is less than $num2 or $num1 is even number"
elif (( $num1 > $num2  || $num1%2 != 0 ))
then
    echo "$num1 is greater than $num2 or $num1 is odd number"
else
echo "Please try again"
fi

İkinci yazım şekli aşağıdaki gibidir


read -p "Enter any number : " num1
read -p "Enter your second number : " num2

if [[ $num1 -lt $num2 || $num1%2 -eq 0 ]]
then
    echo "$num1 is less than $num2 or $num1 is even number"
elif [[ $num1 -gt $num2 || $num1%2 -ne 0 ]]
then
    echo "$num1 is greater than $num2 or $num1 is odd number"
else
    echo "Please try again"
fi









Soru:

1. Ask user to enter his/her name
2. Ask user to enter his/her age
3. Print user name with one of these messages regarding his/her age:
	a. 0<age<1: "Infant"
    b. 1<=1age<12: "Toddler"
	c. 12<=age<18 : "Teen"
	d. 18<=age<65 : "Adult"
    e. age>=65: "Elderly"
























FOR LOOP

Örnek1:
for loop için aynı pythonda olduğu gibi; for loop için işlemin yürütüleceği 
bir aralık vermemiz gerekir. sonrasında aralıkda dolaşacak variable(değişken) değerini for döngüsünün içerisinde 
dolaştırabiliriz
for için aralık vermeye müteakip do yazılması gerekir ki komutlar işlemeye başlasın
for loop un içine tek komut yazma zorunluluğu yoktur. Birden fazla komut yazılabilir. 
Bitimine de done koyulması gerekir. for satırının sonuna ; koyulmasa da olur. Pythondaki
gibi koyma zorunluluğu burada yoktur

for number in {0..10};
do
	echo number is $number
done





Not: Burada space ler item ları ayırmak için kullanılır. comma koymaya gerek yoktur
ama eğer iki veya daha fazla kelime bir arada çıkarılacaksa bu durumda 

names="Serkan Bakır Mucahit Robert Belkis Fatma"
for name in $names;
do
	echo "Welcome $name to Claruswy"
done

Not:Buraya araya bilgi alma satırı da eklenebilir
yani echo nun üzerine 

read -p "Please enter your number : " num 
echo "Welcome $name to Clarusway, your number is $num"











Not: Eğer birden fazla kelime için yazdırmak istiyorsak o durumda şu kullanım uygulanır.

declare -a names=("Serkan Bakır" "Mucahit" "Robert" "Belkis ve Fatma")
for name in "${names[@]}";
do
	echo "Welcome $name to Clarusway"
done









matematiksel gösterimlerde şu şekilde yapılır
for ((initialization; test; step))
do
	commands
done



Örnek 
#!/bin/bash

for (( counter=1; counter<=10; counter++ ))
do
echo -n "$counter "
done

printf "\n"





Örnek 3
Not: Burada her üç ifadeyi de yazmak zorundayız


for (( var=1; var<=10; var++ ));
do
    read -p "Enter your number : " name
    echo "Welcome to Clarusway $name, your number is $var"

    if [ $var -eq 3 ];
    then
        break
    fi
done






Örnek 
5 ve 5 den önceki sayıların çift ya da tek olmalarına bakalım


Burada i in {1..5} de kullanılabilir. 

for (( n=1; n<=5; n++ ))
do
if (( $n%2==0 ))
then
echo "$n is even"
else
echo "$n is odd"
fi
done





Örnek

#içerikden okuma, path'i tanımlanan herhangi bir dosya içerisindeki verileri okutabiliriz
#bu durumda aşağıdaki örnek faydalı olacaktır.

i=1
for var in `cat ./weekday.txt`
do

echo "Weekday $i: $var"
((i++))
done





WHILE Loops:


while loop\'ları da Pthon dakine benzer şekilde sonrasında koyduğumuz şart sağlanana 
kadar uygulanacaktır.

while için koşul vermeye müteakip do yazılması gerekir ki komutlar işlemeye başlasın
while loop un içine tek komut yazma zorunluluğu yoktur. Birden fazla komut yazılabilir. 
Bitimine de done koyulması gerekir. for satırının sonuna ; koyulmasa da olur. Pythondaki
gibi koyma zorunluluğu burada yoktur

while CONDITION
do
    command1
    command2
    command3
done

while [ condition ]; do commands; done
while control-command; do COMMANDS; done



Örnek 

i=1

while [ $i -le 10 ]
do 
    echo $i
    ((++i))
done



Not: break komutu da aynı python da olduğu gibi bizi, kuşulun sağlandığı yerde 
loopun dışına atar.


Örnek: 5 e kadar olan sayılar içinde döngü 2ye eşit olduğunda dursun.

#! /bin/bash/
clear

i=0

while [ $i -lt 5 ]
do
  echo "Number: $i"
  ((i++))
  if (( $i == 2 )); then
    break
  fi
done

echo 'All Done!'






Örnek: şimdi 20 ve 20 den küçük sayılar için çift ve 15 den büyük ve eşit
olanları basmayalım.  


#!/bin/bash
	
	num=1
	
	while [ $num -le 20 ]; do
	
		# Don't print evens
		if (( ((num % 2)) == 0 )); then
 			num=$((num + 1))
 			continue
 		fi
 		
 		# Jump out of the loop with break
 		if ((num >= 15)); then
 			break
 		fi
 		
		echo $num
		num=$((num + 1))
	done


UNTIL
Until de while loop gibi hareket eder.
 Önündeki koşul sağlanana kadaraşağıda verilen komut çalışacaktır


#!/bin/bash
	
	num=1
	
	until [ $num -gt 10 ]; do
		echo $num
		num=$((num + 1))
	done


















HERE DOCUMENT/script

Scriptimizin içine block da ekleyebiliriz ve bu block ile multiple line bir 
ifadeyi bir script olarak da tanıtabiliriz. Bunun için ifadeye >> ile başlanır
blok ismi verilir, sonrasında blok yazılır ve en sonda block name ile bitirilir
şöyle ki:


#! /bin/bash/ 

cat<<END
this is a block
that we a want to
add inside script
END


Not: Blok isminden sonra yazılacak olanlar bir enter verilerek
alttn başlayarak yazılmalıdır. en sonda da yine blok ismi 


myblock=$(cat<<SERKAN 
bloğun
içine istediğimi yazabilirim
bu konuda herhangi bir 
kısıtlama yoktur
ve yazdığım herşey single script haline gelir
SERKAN
)

echo $myblock




HOW TO BURRY PYTHON COMMAND INSIDE SCRIpT

bash script in içine single line ve multiline commands
gömebiliriz. Öncelikle single line nasıl yapılır onu görelim;

Single line command:
Örnek:
python3 -c 'print("123 is your number")'





Multi line command:

Bunun için az önce gördüğümüz blok yapısı kullanılır:


PYTHON_CODE

#!/bin/bash
clear

PYTHON_CODE=$(cat <<END
#Python code starts here
num=int(input("please enter your number : "))
count=0
if num==2:
    print(f"{num} is a prime number")
elif num==1:
    print(f"{num} isn't a prime number")
else:
    for i in range(2,num):
        if num%i==0:
            count+=1
    if count>1:
        print(f"{num} isn't a prime number")
    else:
        print(f"{num} is a prime number")
END
)

#you should use this;

python3 -c "$PYTHON_CODE"

#now you can continue with bash script






Ayrıca bir dosyada olan bir python dosyasını da buradan çalıştırabiliz:
Şöyle ki:

komut satırına aşağıdaki ifade yazısa yeterli olacaktır.

python3 /Users/ODG/Desktop/True.py












Float sayılarda aritmetik işlemler

man bc yaparak bc için tüm açıklamalar görülebilir. 
bc aritmetik işlemlerin uygulanabilirliğini sağlıyor.  

#! /bin/bash
clear
sayi1=20.5
sayi2=5

echo "20.34+5" | bc
echo "20.5-5" | bc
echo "20.5*5" | bc
echo "20.5/5" | bc
echo "20.5%5" | bc
#görüldüğü gibi bölme tam olmuyor ama tam olabilmesi için
#scale özelliği kullanılır


echo "scale=2;20.5/5" | bc

echo "scale=2;$sayi1/$sayi2" | bc
echo "$sayi1+$sayi2" | bc

echo "scale=10; sqrt($sayi2)" | bc -l
echo "scale=2; $sayi1^3" | bc -l








Functions

Fonksiyon özellikle bash script de komut tekrarını önlemek amacı ile
ya da programın farklı yerlerinde kullanılacak komut tekrarlarından  
kaçınmak için kullanılır. Önce fonksiyonu oluşturur sonrasında da aynı 
komutları tekrar tekrar yazma zahmetinden fonksiyonu çağararak kurtuluruz.
İki tür fonksiyon yazma şekli vardır.

1)Başına function yazılır, sonra function ismi yazılır 
() parantezi yazılır ardından { } ler arasına fonksiyon yazıldığında 
uygulanacak komut yazılır

2) İkinci yolda ise başta fonksiyon yazmadan fonksiyon ismi yazarak başlanır
ve sorasında, ilk kısımdaki yazım uygulanır

Örnek:

function Merhaba(){

    echo "Merhaba Dsotlar"


}

#Bu fonksiyon yazıldıktan sonra fonksiyonu çağırmanız gerekir. Eğer fonksiyonu çağırmaz iseniz
#fonksiyon cevap vermeyecektir. 

Merhaba


2)
#! /bin/bash/
clear
liste(){

    tail -4 /etc/group
    return

}

liste



örnek 
Bir sayının küpünü alan bir fonksiyon yazalım

#! /bin/bash/

i=1
function third_deg(){
read -p "Please enter a number : " num

let num$i=num**3

echo "Third degree of you number is $((num$i))"

let i++

}

third_deg 

echo $num1

third_deg

echo $num2






Local variable
Scriptler içerisinde global variablelar olduğu gibi local variablelar da 
mevcuttur. Global variablelar scriptin herhangibiryerinde kullanılabilirlen
local variablelar local bölgelerde sadece kullanılır. Bu local variableları
kullanabilmek için önüne local ibaresi yazılmalıdır.


Örnek:
#! /bin/bash/
ame="Serkan"
function appl(){
       local proces="application"
       echo "Dear $name! Welcome to $proces of SSN!"
       
}
name="Serkan"
function review(){
       local proces="further review"
       echo "Dear $name! Welcome to $proces of SSN!"
       
}
appl
review
echo "Name    : $name"
echo "Process : $proces"



 2. Passing Argument

 Fonksiyon içerisinde ardı ardına variable lar tanımlanabilir
 bunlar için fonksiyon içerisinde 1 den başlamak sureti ile
 ardışık rakanlar variablelara atanacaktır.

Örnek 

 #! /bin/bash/
clear

 function mult(){
        echo "Multiplication $(( $1*$2*$3 ))"
        

 }

 mult 3 4 5





Örnek 2:

#! /bin/bash/
lear
function mult(){
       echo "Multiplication of these is $(( $1*$2*$3 ))"
       
}
read -p "Please of your first number : " num1
read -p "Please of your first number : " num2
read -p "Please of your first number : " num3
mult $num1 $num2 $num3



Örnek:
Create a function named retire_age that accepts one argument 
ask user to input hıs/her year of birth and store it to local bırth_year variable 
prınt age with a messages

call prınt_age function with 2020



#! /bin/bash/
clear

function print_age(){
        local birth_year
        read -p "Please enter your year of birth : " birth_year
        let age=$1-$birth_year
        echo "Your age is $age. Thank you!"

}

print_age 2020
echo "$birth_year" 


