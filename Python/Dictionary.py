# To creaete an empty dictionary.
d = {}
# Assign a key and a value.
# A key and a value are called an entery.
# key               value
d['python'] = 'A kind of snake'

print(d['python'])

# To modify the dictionary.
d['python'] += ', or a programing language'
print(d['python'])

# You can add another key and value.
d['scorpions'] = 'Are predatory arachnids, or the pand'
print(d['scorpions'])

# To pint the whole dictionary.
print(d)

# Atother way to make a dictionary.
d2 = {'c++': 'A programing language', 'network': 'A punch of devices connecting together'}
print(d2['c++'])
print(d2)
# To delete an entery.
del d2['network']
print(d2)
