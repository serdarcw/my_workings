
n = 50
if n>48:
    top =7000+(n%48)*600
elif n>41:
    top =2600+(n%32)*550
elif n>32:
    top =(n%32)*325
print(top)
