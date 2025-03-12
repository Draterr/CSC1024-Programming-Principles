import helper

def add_course():
    print("Add a new course")
    file_name = "courses.txt"

    while True:
        course_id = input("Enter course id: ")
        if course_id.lower() == "back":
                return
        if helper.course_id_exists(course_id, file_name):
            print("Course ID already exists. Please enter a different course id.")
        else:
            break

    while True:
        course_name = input("Enter course name: ")
        if helper.course_name_exists(course_name, file_name):
            print("Course name already exists. Please enter a different course name.")
        else:
            break

    while True:
        available_seats = input("Enter available course seats: ")
        if not available_seats.isdigit():
            print("Please enter a valid number.")
        else:
            break

    while True:
        course_seats = input("Enter maximum course seats: ")
        if available_seats > course_seats:
            print("The amount of available seats can't be greaather than the maximum amount of seats.")
            continue
        if not course_seats.isdigit():
            print("Please enter a valid number.")
        else:
            break

    with open(file_name, "a", encoding="utf-8") as file:
        file.write(f"{course_id},{course_name},{available_seats},{course_seats}\n")

    print("Course added successfully.")

    user_continue = input("Do you want to add another course? (yes/no): ")
    if user_continue.lower() == "yes" or user_continue.lower() == "y":
        add_course()
    elif user_continue.lower() == "no" or user_continue.lower() == "n":
        return
    else:
        print("Invalid input. Returning to main menu.")
    
    return
