
list1 = []
list2 = [number for number in range(1, 6, 2)]
list3 = list(range(1, 6, 2))

for number in range(1, 6):
    print(number)
    list1.append(number)

print(list1)
print(list2)
print(list3)
