name = input('Please enter your first name : ')
dict_1 = {'name': 'Serkan', 'passwd':'@12'}

if name == dict_1['name']:
    print(f"Hello, {dict_1['name']} The password is : {dict_1['passwd']}")
else:
    print("Hello "+name+"!"+"See you later.")

