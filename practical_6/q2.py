i = 0
my_list = []
while i < 5:
    j = 0
    num = float(input("Enter a number: "))
    while j < len(my_list):
        if my_list[j] > num:
            my_list.insert(j,num)
            break
        j+=1
    else:
        my_list.append(num)
    i+=1
print(my_list)