import helper
# function to register new student
def register_student():
    print("Register a new student.\n")
    # try block to make sure student ID entered is numeric and is a positive number that is exactly 8 digits long
    while True:
        try:
            student_id = input("Enter student ID (8 digits) or 'back' to exit: ")
            if student_id.lower() == 'back':
                return
            if not student_id.isdigit(): # numeric check
                print("[-] Invalid input: Student ID can only be in numbers. Please try again.")
                continue
            if student_id.startswith("-"): # positive number check
                print("[-] Invalid input: Student ID can only be a positive number. Please try again.")
                continue
            if len(str(student_id)) != 8: # digit length check
                print("[-] Invalid input: Student ID must be exactly 8 digits. Please try again.")
                continue
            if helper.student_id_exists(student_id,"students.txt"):
                print("[-] Invalid Student ID: Student ID already exists. Please try again.")
                continue
            break # exit loop if entered format is valid
        except Exception as e:
            print(f"[-] An unexpected error has occurred: {e}. Please try again.")

    # try block to make sure student name entered only contains alphabets and spaces
    while True:
        try:
            student_name = input("Enter student name or 'back' to exit: ")
            if student_name.lower() == 'back':
                return
            if not student_name.replace(" ", "").isalpha(): # alphabet check
                print("[-] Invalid input: Student name can only contain alphabets and spaces. Please try again.")
                continue
            break # exit loop if entered format is valid
        except Exception as e:
            print(f"[-] An unexpected error has occurred: {e}. Please try again.")

    # try block to make sure student contact number is numeric and is a positive number between 10-11 digits long
    while True:
        try:
            student_contact = input("Enter student contact number (10-11 digits) or 'back' to exit: ")
            if student_contact.lower() == 'back':
                return
            if not student_contact.isdigit(): # numeric check
                print("[-] Invalid input: Student contact can only be in numbers. Please try again.")
                continue
            if student_contact.startswith("-"): # positive number check
                print("[-] Invalid input: Student contact can only be a positive number. Please try again.")
                continue
            if len(str(student_contact)) not in {10, 11}: # digit length check
                print("[-] Invalid input: Student contact must be exactly 10 or 11 digits. Please try again.")
                continue
            break # exit loop if entered format is valid
        except Exception as e:
            print(f"[-] An unexpected error has occurred: {e}. Please try again.")

    # stores student details entered by the user
    # student = f{"ID": student_id, "Name": student_name, "Contact": student_contact}
    student = f"{student_id},{student_name},{student_contact}\n"

    try:
        #open students.txt file in "append mode"(anything we write to the file will be added to the end of the file)
        with open("students.txt","a") as file:
            #write the new students infromation from the user into the file
            file.write(student)
            print("[+] Successfully added student!")
            return
    except Exception as e:
        print(f"[-] an unexpected error has occured: {e}. Please try again.")
    return
