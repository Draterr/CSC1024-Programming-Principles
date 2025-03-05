my_list = []
for i in range(5):
    num = float(input("Enter a number: "))
    j = 0
    while j < len(my_list):
        if my_list[j] > num:
            my_list.insert(j,num)
            break
        j+=1
    else:
        my_list.append(num)
print(my_list)
for k in range(len(my_list)-1,0-1,-1):
    del my_list[k]
print(my_list)