Create a function that takes two parameters and, if both parameters are strings, add them as if they were integers or if the two parameters are integers, concatenate them.

Examples
stupid_addition(1, 2) ➞ "12"

stupid_addition("1", "2") ➞ 3

stupid_addition("1", 2) ➞ None



def stupid_addition(a, b):
    if type(a) == type(b):
        if type(a) == int:
            return str(a) + str(b)
        return int(a)+int(b)




def stupid_addition(a, b):
	if type(a) == int and type(b) == int:
		return str(a) + str(b)
	elif type(a) == str and type(b) == str:
		return int(a) + int(b)



def stupid_addition(a, b):
	if type(a)==int and type(b) ==int:
		return str(a)+str(b)
	elif type(a)==str and type(b) ==str:
		return int(a)+int(b)
	else:
		return None



def stupid_addition(a, b):
	if isinstance(a, str) and isinstance(b,str):
		return eval(a+'+'+b)
	elif isinstance(a,int) and isinstance(b,int):
		return '{}{}'.format(a,b)
	else:
		return None





def stupid_addition(a, b):
	if type(a) == type(b):
		if type(a) is str:
			return int(a) + int(b)
		if type(b) is int:
			return '{}{}'.format(a, b)
	return None





def stupid_addition(a, b):
    if type(a) != type(b):
        return None 
    return str(a) + str(b) if isinstance(a, int) else int(a) + int(b)




def stupid_addition(a, b):
	if type(a)!=type(b):
		return None
	if type(a)==type(b):
		if type(a)==int:
			return str(a)+str(b)
		if type(a)==str:
			return int(a)+int(b)