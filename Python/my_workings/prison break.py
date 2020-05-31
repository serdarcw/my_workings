https://edabit.com/challenge/SHdu4GwBQehhDm4xT

Prison Break
A prison can be represented as a list of cells. Each cell contains exactly one prisoner. A 1 represents an unlocked cell and a 0 represents a locked cell.

[1, 1, 0, 0, 0, 1, 0]
Starting from the leftmost cell, you are tasked with seeing how many prisoners you can set free, with a catch. Each time you free a prisoner, the locked cells become unlocked, and the unlocked cells become locked again.

So, if we use the example above:

[1, 1, 0, 0, 0, 1, 0] 
# You free the prisoner in the 1st cell.

[0, 0, 1, 1, 1, 0, 1] 
# You free the prisoner in the 3rd cell (2nd one locked).

[1, 1, 0, 0, 0, 1, 0]
# You free the prisoner in the 6th cell (3rd, 4th and 5th locked).

[0, 0, 1, 1, 1, 0, 1]
# You free the prisoner in the 7th cell - and you are done!
Here, we have freed 4 prisoners in total.

Create a function that, given this unique prison arrangement, returns the number of freed prisoners.

Examples
freed_prisoners([1, 1, 0, 0, 0, 1, 0]) ➞ 4

freed_prisoners([1, 1, 1]) ➞ 1

freed_prisoners([0, 0, 0]) ➞ 0

freed_prisoners([0, 1, 1, 1]) ➞ 0
Notes
You must free a prisoner in order for the locks to switch. So in second example where the input is [1, 1, 1], after you release the first prisoner, the locks change to [0, 0, 0]. Since all cells are locked, you can release no more prisoners.
You always start with the leftmost element in the list (the first prison cell). If all the prison cells to your right are zeroes, you cannot free any more prisoners.


mine:
A=[1, 0, 1, 0, 1, 0]
count = 0
if A[0]==0:
    print(0)
else:
    k=1
    for i in A:
        if i==k:
            count+=1
            k=1-k

    print(count)


def freed_prisoners(prsn):
    return prsn[0] and sum(1 if prsn[i-1] != prsn[i] else 0 for i in range(1, len(prsn))) +1

def freed_prisoners(prison):
	if prison[0] == 0:
		return(0)
	count = 1
	for i in range(1, len(prison)):
		if prison[i] != prison[i-1]:
			count+=1
	return(count)




def freed_prisoners(prison):
	saved = 0
	tempPrison = prison
	
	if not tempPrison[0]: return 0
	
	for i in range(len(tempPrison)):
		if tempPrison[i]%2==1:
			saved += 1
			tempPrison = [n+1 for n in tempPrison]
	return saved




def freed_prisoners(prison):
	def _freed_prisoners(prison):
		if not prison:
			return 0
		current_cell,*rest = prison
		if current_cell == 1:
			rest = [(x*-1)+1 for x in rest]
			return 1 + _freed_prisoners(rest)
		return _freed_prisoners(rest)
	return 0 if prison[0] == 0 else _freed_prisoners(prison)
