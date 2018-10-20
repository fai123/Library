d = {'cat': 'tiger', 'bird': 'eagle'}

# By defualte the loop will loop over the keys.
for item in d:
    print(item)
print()

# To loop over the keys same as the above.
for item in d.keys():
    print(item)
print()

# To loop over the values.
for item in d.values():
    print(item)
print()

# To loop over the whole entry.
for item in d.items():
    print(item)
print()

# Stirung the keys in a (keys) variable and the values in (values) variable.
for keys, values in d.items():
    print(f"'{keys}' is the key, and '{values}' is the value")
