list = []
list += [i for i in range(100)]
print(list)
for i in range(100):
    list[i] = -list[i]
print(list)