my_list = []
for i in range(5):
    num = input("Enter a number: ")
    j = 0
    my_list.append(num)
for k in range(len(my_list)-1,0-1,-1):
    print(my_list)
    del my_list[k]
print(my_list)