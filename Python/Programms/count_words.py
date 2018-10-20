user = input("Enter a sentence: ")

list = user.split(" ")
d = {}

for word in list:
    if not word in d:
        d[word] = 1
    else:
        d[word] += 1

print(d)

for keys, values in d.items():
    print(f"'{keys}' appeared {values} time(s)")
