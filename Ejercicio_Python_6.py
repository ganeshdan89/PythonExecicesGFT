import numbers as n
list = [2, 6, 4, 1, 10]
list1 = [8, 13, 5, 10, 14, 9]

firstValue = list.__getitem__(0)
closestValue = firstValue-1
value = 0

if closestValue in list:
    value = closestValue
else:
    for n in list:

        if closestValue in list:
            value = closestValue
        else:
            closestValue -= 1


print(f'El numero mas cercano a el {firstValue} {value} ')

