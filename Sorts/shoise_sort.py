list_1 = [34, 22, 45, 44, 48]
sorted_list = []
while len(list_1) > 0:
    min = list_1[0]
    for i in range (0, len(list_1)):
        if list_1[i] < min:
            min = list_1[i]
    sorted_list.append(min)
    list_1.remove(min)
print(sorted_list)