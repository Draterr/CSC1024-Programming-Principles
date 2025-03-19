import helper

def add_course():
    """
    This function adds a course to the system
    """
    print("Add a new course")
    file_name = "courses.txt"

    while True:
        course_id = input("Enter course id or 'back' to exit: ")
        if course_id.lower() == "back": #allow user to exit when enter 'back'
                return
        if not course_id.strip().isalnum():
            print("course id cannot contain special characters! Please Try Again!")
            continue
        if len(course_id) > 10:
            print("Course ID must be with in 10 characters")
            continue
        if not course_id: #if the input is empty then print invalid id and let user enter again.
            print("Invalid ID,Please enter a valid course id")
            continue
        if helper.course_id_exists(course_id, file_name): #check course id is exists or not. 
            print("Course ID already exists. Please enter a different course id.")
        else:
            break #valid input and not exist then exit loop

    while True: #second loop 
        course_name = input("Enter course name or 'back' to exit: ")
        if course_name.lower() == 'back':
            return
        if not course_name: #if input is empty then print invalid name then let user enter again.
            print("Invalid name, Please enter a valid course name.")
            continue
        if not course_name.strip().replace(" ","").isalnum():
            print("Input cannot contain special characters! Please Try Again!")
            continue
        if helper.course_name_exists(course_name, file_name): #check course name is exists or not.
            print("Course name already exists. Please enter a different course name.")
        else:
            break #if input is valid and not exist then exit the loop

    while True: #third loop
        available_seats = input("Enter available course seats or 'back' to exit: ")
        if available_seats.lower() == 'back':
            return
        if not available_seats.isdigit() or int(available_seats) <= 0: #if input is not digit then is invalid input,let user enter again.
            print("Please enter a valid number.")
        else:
            break #if input is a digit then exit the loop

    while True: #fourth loop
        course_seats = input("Enter maximum course seats: ") 
        if course_seats.lower() == 'back':
            return
        if not course_seats.isdigit() or int(available_seats) <= 0: #input not a digit then print invalid number then let user enter again.
            print("Please enter a valid number.")
            continue
        if int(available_seats) > int(course_seats): #max seats must be greater or equal to available seats.
            print("The amount of available seats can't be greater than the maximum amount of seats.")
            continue #if max seats not greater or equal to availble seats then let user enter input again.
        else:
            break #if input is digit and max seats is greater or equal to availble seats then exit the loop.

    try:
        with open(file_name, "a", encoding="utf-8") as file: #add file
            file.write(f"{course_id},{course_name},{available_seats},{course_seats}\n") #write course id,name,available seat and maximum seats into file(course.txt)
    except: #if file not exist or no permission to open then print this
        print("Failed to open courses.txt file")

    print("Course added successfully.")

    user_continue = input("Do you want to add another course? (yes/no): ") #ask user want to add another course or not 
    if user_continue.lower() == "yes" or user_continue.lower() == "y":     #if yes then run this function again
        add_course()
    elif user_continue.lower() == "no" or user_continue.lower() == "n":    #if no then back to main menu.
        return
    else:                                                                  #if user not enter 'yes' or 'not' then print invalid input then send user back to main menu.
        print("Invalid input. Returning to main menu.")
    
    return
