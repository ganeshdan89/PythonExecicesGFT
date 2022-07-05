list = []
listPair = []
listImpair = []


for i in range(10):
    x = int(input('Ingrese un valor: -->  '))
    list.append(x)



for number in list:
    if number % 2 == 0:
        listPair.append(number)

    else:
        listImpair.append(number)

print(f'Random list {list}')
print(f'Pair list {listPair}')
print(f'Impair list {listImpair}')
