num_to_print = int(input("Which multiplication table would you like to print? "))
how_high = int(input("How high would you like it to go? "))

i = 1
print("Here is your multiplication table: ")
while i <= how_high:
    print(f"{num_to_print} times {i:<2} = {num_to_print * i:>2}")
    i+=1
