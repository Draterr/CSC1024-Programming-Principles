my_list = []
for i in range(5):
    data = input("Enter a data: ")
    my_list.append(data)
for j in range(5-1,0-1,-1):
    if j % 2 == 0:
        print(my_list)
        del my_list[j]

print(my_list)