list_1 = [18, 42, 23, 10, 66]
central = len(list_1) // 2
print(central)
# обернуть в ещё один цикл
for i in range(0, central):
    if list_1[i] > list_1[central]:
        list_1.append(list[i])
        list_1.remove(list[i])
for i in range(central + 1, len(list_1)):
    if list_1[i] < list_1[central]:
        list_1.insert(0, list[i])
        list_1.remove(list[i])
print(list_1)
