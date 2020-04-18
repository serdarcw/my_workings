
#empty_dict_1 = {}
#
#empty_dict_2 = dict()






#empty_dict_1 = {}
#
#print(type(empty_dict_1))






#my_dict = {'key1': 'value1',
#            'key2': 'value2',
#            'key3': 'value3'
#            }
#
#print(my_dict['key1'])





#state_capitals = {'Arkansas': 'Little Rock',
#                  'Colorado': 'Denver',
#                  'California': 'Sacramento',
#                  'Georgia': 'Atlanta' 
#                 }
#
#print(state_capitals['Arkansas']) # accessing method




#state_capitals = {'Arkansas': 'Little Rock',
#                  'Colorado': 'Denver',
#                  'California': 'Sacramento',
#                  'Georgia': 'Atlanta' 
#                 }
#
#state_capitals['Virginia'] = 'Richmond' # adding a new item
#
#print(state_capitals)




#state_capitals = {'Arkansas': 'Little Rock',
#                  'Colorado': 'Denver',
#                  'California': 'Sacramento',
#                  'Georgia': 'Atlanta' 
#                 }
#
#state_capitals['Virginia'] = 'Richmond' # adding a new item
#
#print(state_capitals)








#mix_dict = {'animal': ('dog', 'cat'),  # tuple type
#            'planet': ['Neptun', 'Saturn', 'Jupiter'],  # list type
#            'number': 40,  # int type
#            'pi': 3.14,  # float type
#            'is_good': True}  # bool type
#print(mix_dict)





#eğer dict() fonksiyonu ile dictionary oluşturuyorsanız key 'ler için tırnak kullanmayın 
# ama {} yazımınd kullanılabilir.

#dict_by_dict = dict(animal='dolphin', planet='mars', number=41, pi=3.14, is_good=False)
#
#print(dict_by_dict)
#
#
#Output : {'animal': 'dolphin', 'planet': 'mars', 'number': 41, 'pi': 3.14, 'is_good': False}




#dict_by_dict = {'animal': 'dolphin',
#                'planet': 'mars',
#                'number': 41,
#                'pi': 3.14,
#                'is_good': False}
#
#print(dict_by_dict.items(), '\n')
#print(dict_by_dict.keys(), '\n')
#print(dict_by_dict.values())
#
## dict_by_dict.items() komutu ile output alındığında type dict.type gosterir
## ondan dolayı outputu list, tuple, set vs içine almamız gerekir.
#ser = list(dict_by_dict.keys())
#print(ser)





#Output : 
#dict_items([('animal', 'dog'), ('planet', 'neptun'), 
#            ('number', 40), ('pi', 3.14), ('is_good', True)]) 
#
#dict_keys(['animal', 'planet', 'number', 'pi', 'is_good']) 
#
#dict_values(['dog', 'neptun', 40, 3.14, True]) 



#we can also add new items using the update method. 
#dict_by_dict = {'animal': 'dolphin',
#                'planet': 'mars',
#                'number': 41,
#                'pi': 3.14,
#                'is_good': True}
#
#dict_by_dict.update({'is bad': False})
#dict_by_dict.update({'dress': 'pants'})
#
#print(dict_by_dict)





#we can also remove an item using the del function:

#The formula syntax is : del dictionary_name['key'].

#dict_by_dict = {'animal': 'dolphin',
#                'planet': 'mars',
#                'number': 41,
#                'pi': 3.14,
#                'is_good': True}
#
#del dict_by_dict['is_good']
#print(dict_by_dict)









#Using the in and the not in operator, you can check if
# the key is in the dictionary.
#When we use the in operator; if the key 
#is in the dictionary, the result will be True otherwise False.
#When we use the not in; if the key is not in 
#the dictionary, the result will be True otherwise False.

#dict_by_dict = {'planet': 'neptun',
#               'number': 40,
#               'pi': 3.14,
#               'is_good': True,
#               'is_bad': False}
#
# 
#print('number' in dict_by_dict)
#print('serhat' in dict_by_dict)
#print('serhat' not in dict_by_dict)





#thisdict =	{
#  "brand": "Ford",
#  "model": "Mustang",
#  "year": 1964
#}
#
#print(len(thisdict))






#thisdict = {
#  "brand": "Ford",
#  "model": "Mustang",
#  "year": 1964
#}
#mydict = thisdict.copy()
#print(mydict)





#Nested Dictionaries
#In some cases, you need to work with the nested dict.
# When you decide to specialize in data science, we will 
# work very often with dictionaries in the future.

school_records = {
    "personal_info":
        {"kid":{"tom": {"class": "intermediate", "age": 10},
                "sue": {"class": "elementary", "age": 8}
               },
         "teen":{"joseph":{"class": "college", "age": 19},
                 "marry":{"class": "high school", "age": 16}
               },               
        },
        
    "grades_info":
        {"kid":{"tom": {"math": 88, "speech": 69},
                "sue": {"math": 90, "speech": 81}
               },
         "teen":{"joseph":{"coding": 80, "math": 89},
                 "marry":{"coding": 70, "math": 96}
               },               
        },        
}


##We can use square brackets to access internal dicts :
#
#print(school_records['personal_info']['kid']['sue']['class'])




customers = { 
'bank': 
{1: {'name': 'James', 'age': '27', 'sex': 'Male'}, 
 2: {'name': 'Nicole', 'age': '25', 'sex': 'Female'},  
 3: {'name': 'Andy', 'age': '38', 'sex': 'Male'}, 
 4: {'name': 'Alex', 'age': '19', 'sex': 'Male'}, 
 5: {'name': 'Linda', 'age': '33', 'sex': 'Female'}, 
},
'insurance':
{1: {'name': 'Jashua', 'age': '33', 'sex': 'Male'}, 
 2: {'name': 'Marry', 'age': '66', 'sex': 'Female'},  
 3: {'name': 'Adam', 'age': '56', 'sex': 'Male'}, 
 4: {'name': 'Samuel', 'age': '54', 'sex': 'Male'}, 
 5: {'name': 'Lisa', 'age': '22', 'sex': 'Female'},
},
}

#Lisa'nın yaşını bulalım
print(customers['insurance'][5]['age'])