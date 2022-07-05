list = []
list2 = []
for i in range(1, 5):
    list.append(i)
print(f'{list}')

for n in list:
    n *= n
    list2.append(n)
print(f'{list2}')

