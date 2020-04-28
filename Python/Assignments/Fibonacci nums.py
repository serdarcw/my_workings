A=[1,1]
i=2
while A[-1]<55:
	A.append(A[i-2]+A[i-1])
	i+=1
print(A)
