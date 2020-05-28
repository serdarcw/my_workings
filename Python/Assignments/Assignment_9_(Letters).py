A="hippo runs to us!"
B={}
alphaDict = dict.fromkeys(A,0)
for i in A:
	for j in alphaDict.keys():
		if i==j:
			alphaDict[i]+=1
print(alphaDict)	
