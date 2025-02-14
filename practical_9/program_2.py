user_input = int(input("Display multiplication table of? "))
print(f"A multiplication table of {user_input} times 1 to 12.")
with open("TT2TXT.txt","w+") as f:
    for i in range(1,13):
        f.write(f"{user_input} x {i} = {user_input * i}\n")

with open("TT2TXT.txt","r") as f:
    print(f.read())
