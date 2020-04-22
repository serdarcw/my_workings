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
Çift parantez yazımlarında içteki operasyonların sağında ve solunda whitespace
bırakmayı unutmayın.

-eq
is equal to
if [ "$a" -eq "$b" ]
if (("$a" == "$b"))
Not: İki değerieşitliğini kontrol eder. -eq: equal


-ne
is not equal to
if [ "$a" -ne "$b" ]
if (("$a" != "$b"))
Not: İki değerin birbirinden farklılığını kontrol eder, -ne:not equal



-gt
is greater than

if [ "$a" -gt "$b" ]
if [ "$a" > "$b" ]
Not: Sağdaki değerin soldaki değerden büyük olup olmadığına bakar
-gt:: Greater then




-ge
is greater than or equal to

if [ "$a" -ge "$b" ]
if (( "$a" >= "$b" ))
Not: Sağdaki değerin soldaki değerden büyük ya da eşit olup olmadığına bakar
-ge:Greater or equal



-lt
is less than

if [ "$a" -lt "$b" ]
if (( "$a" < "$b" ))
Not: Sağdaki değerin soldaki değerden küçük olup olmadığına bakar
-lt:: Less then




-le
is less than or equal to

if [ "$a" -le "$b" ]
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





Örnek


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
        echo "This two digit even number"
    else
        echo "This is two digit odd number"
    fi
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

if [[ ( $num -lt 10 ) && ( $num%2 -eq 0 ) ]]; then
echo "Even Number"
else
echo "Odd Number"
fi


Not: and operatorü için [ $var1 -a $var2 ] kullanımı da uygulanabilir







OR operatörü

#!/bin/bash

read -p "Enter any number : " num1
read -p "Enter your second number : " num2

if (( ( $num1 < $num2)  || (num1%2==0)))
then
echo "$num1 is less than $num2 or $num1 is even number"
elif (( ( $num1 > $num2)  || (num1%2!=0) ))
then
echo "$num1 is greater than $num2 or $num1 is odd number"
else
then
echo "Please try again"
fi


Not: or operatorü için [ $var1 -o $var2 ] kullanımı da uygulanabilir.


read -p "Enter any number : " num1
read -p "Enter your second number : " num2

if [ $num1 -lt $num2 -o num1%2 -ne 0 ]
then
echo "$num1 is less than $num2 or $num1 is even number"
elif [ $num1 -gt $num2 -o num1%2 -ne 0 ]
then
echo "$num1 is greater than $num2 or $num1 is odd number"
else
then
echo "Please try again"
fi









Soru:

1. Ask user to enter his/her name
2. Ask user to enter his/her age
3. Print user name with one of these messages regarding his/her age:
	a. age<18 : "Student"
	b. 18<=age<65 : "Worker"
	c. age>=65 : "Retired"























FOR LOOP

Örnek1:
for loop için aynı pythonda olduğu gibi for için loop için bir aralık 
vermemiz gerekir. sonrasında aralıkda dolaşacak number değerini for döngüsünün içerisinde 
dolaştırabilrz
for için aralık vermeye müteakip do yazılması gerekir ki komutlar işlemeye başlasın
bunun içine tek komut yazma zorunluluğu yoktur. Birden fazla komut yazılabilir. 
Bitimine de done koyulması gerekir. for satırının sonuna ; koymayı unutmayın


for number in {0..10};
do
	echo number is $number
done





Not: Burada space ler item ları ayırmak için kullanılır. comma koymaya gerek yoktur
ama eğer iki veya daha fazla kelime bir arada çıkarılacaksa bu durumda 

names="Serkan Bakır' Mucahit Robert Belkis Fatma"
for name in $names;
do
	echo "Welcome $name to Claruswy"
done

Not:Buraya araya bilgi alma satırı da eklemebilir
yani echo nun üzerine 

read -p "Please enter your number :  " num 
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


Burada i in {1..5} de kullanılabilir

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






















