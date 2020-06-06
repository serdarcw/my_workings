https://edabit.com/challenge/Fpymv2HieqEd7ptAq

Parentheses Clusters
Write a function that groups a string into parentheses cluster. Each cluster should be balanced.

Examples
split("()()()") ➞ ["()", "()", "()"]

split("((()))") ➞ ["((()))"]

split("((()))(())()()(()())") ➞ ["((()))", "(())", "()", "()", "(()())"]

split("((())())(()(()()))") ➞ ["((())())", "(()(()()))"]
Notes
All input strings will only contain parentheses.
Balanced: Every opening parens ( must exist with its matching closing parens ) in the same cluster.

var = '(()(()()))()(((()))()(()))(()((()))(())())'
A=[]
b=""
for i in var:
    b+=i
    if b.count('(')==b.count(')'):
        A.append(b)
        b=''
print(A)



def split(txt):
	stack = []
	r = []
	s = ''
	for i in txt:
		if i == '(':
			stack.append(i)
			s = s + i
		else:
			stack.pop()
			s = s + i
			if not stack:
				r.append(s)
				s = ''
	if s:
		r.append(s)
	return r




def split(txt):
	balance = 0
	answer = []
	start = 0
	for i, n in enumerate(txt):
		if n == '(':
			balance -= 1
		else:
			balance += 1
		if balance == 0:
			answer.append(txt[start:i + 1])
			start = i + 1
	return answer