subject = ""
while True:
    user_input = int(input("[1] Create a new file.\n[2] Display the file.\n[3] Add a new item to the file.\nEnter 1, 2, or 3: "))
    if user_input == 1:
        subject = input("Enter a subject: ") + ".txt"
        f = open(subject,"w+")
        f.close()
    elif user_input == 2:
        f = open(subject,"r")
        contents = f.read()
        f.close()
        print(contents)
    elif user_input == 3:
        new_subject = input("Enter a new subject: ")
        f = open(subject,"a")
        f.write(new_subject+"\n")
        f.close()
    else:
        print(f"\nInvalid option {user_input}\nPlease choose between 1,2,3\n")
