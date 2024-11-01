list_1 = [34, 22, 45, 44, 48]
stop_flag = False
while (stop_flag is False):
    stop_flag = True
    for i in range (0, len(list_1) - 1):
        if list_1[i] > list_1[i+1]:
            a = list_1[i]
            list_1[i] = list_1[i+1]
            list_1[i+1] = a
            stop_flag = False
print(list_1)
