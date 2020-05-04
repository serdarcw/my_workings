n = int(input("Please enter number : "))
C=[]
for i in range(2,n+1):
    count=0
    for m in range(2,i//2+1):
        if i%m==0: 
            count+=1
    if count<1: 
        C.append(i)
print(C)
