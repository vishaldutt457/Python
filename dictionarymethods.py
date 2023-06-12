dict={
    "name":"vishal",
    "place":"Lucknow",
    "profession":"developer",
    234:False
}

print(dict['name'])
#result--------------------------vishal

print(dict.get('name'))
#result--------------------------vishal

print(dict.keys())
#result--------------------------dict_keys(['name', 'place', 'profession', 234])

print(dict.values())
#result--------------------------dict_values(['vishal', 'Lucknow', 'developer', False])

for item in dict.keys():
    print(item)

#result--------------------------    name
#                                    place
#                                    profession
#                                    234

for key,value in dict.items():
    print(f"The value corresponding to the {key} is {value}")

#result--------------------------   The value corresponding to the name is vishal
#                                   The value corresponding to the place is Lucknow
#                                   The value corresponding to the profession is developer
#                                   The value corresponding to the 234 is False



################## update Method------

info={"name":"Vishal","LName":"Dutt","place":"lucknow"}
info2={"value":True}

info.update(info2)
print(info)

#result--------------------------   {'name': 'Vishal', 'LName': 'Dutt', 'place': 'lucknow', 'value': True}


################## clear Method------


# info.clear()
# print(info)

#result--------------------------   {}


################## pop Method------


info.pop('value')
print(info)

#result--------------------------   {'name': 'Vishal', 'LName': 'Dutt', 'place': 'lucknow'}



################## popitem Method------

#removes the last item from dictionary
info.popitem('value')
print(info)

#result--------------------------   {'name': 'Vishal', 'LName': 'Dutt', 'place': 'lucknow'}


################## del Method------

del info(['name'])
print(info)

#result--------------------------   {'LName': 'Dutt', 'place': 'lucknow'}


