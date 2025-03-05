forward_list = []
reverse_list = []

for i in range(5):
    j = 0
    num = float(input("Enter a number: "))
    while j < len(forward_list):
        if forward_list[j] > num:
            forward_list.insert(j,num)
            break
        j+=1
    else:
        forward_list.append(num)
print(forward_list)
reverse_list = forward_list[::-1]
print(reverse_list)