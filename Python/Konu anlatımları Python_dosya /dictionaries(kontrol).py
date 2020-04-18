
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





#a dictonary can be created like below and Be careful Do not use quotes for 
# keys when using the dict() function to create a dictionary.

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








#school_records={
#    "personal_info":
#        {"kid":{"tom": {"class": "intermediate", "age": 10},
#                "sue": {"class": "elementary", "age": 8}
#               },
#         "teen":{"joseph":{"class": "college", "age": 19},
#                 "marry":{"class": "high school", "age": 16}
#               },               
#        },
#        
#    "grades_info":
#        {"kid":{"tom": {"math": 88, "speech": 69},
#                "sue": {"math": 90, "speech": 81}
#               },
#         "teen":{"joseph":{"coding": 80, "math": 89},
#                 "marry":{"coding": 70, "math": 96}
#               },               
#        },        
#}
