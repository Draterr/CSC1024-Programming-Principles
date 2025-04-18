import helper

def edit_course():
    file_name = "courses.txt"
    enrollment_file = "enrollments.txt"

    # Read course file safely
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            print("Edit a course")
            print("Available courses:")

            courses = []
            lines = file.readlines()

            for line in lines:
                if not line.startswith("Course ID"):  #this is to skip the first line of the file which is the header
                    parts = line.strip().split(",") #split the details inside course.txt into 4 parts.
                    if len(parts) == 4: #because have 4 fields in the courses.txt file so is parts == 4
                        course_id, course_name, available_seats, maximum_seats = parts #example: part[0] = course_id, part[1] = course_name, part[2] = available_seats, part[3] = maximum_seats
                        courses.append(f"{course_id} - {course_name} ({available_seats}) ({maximum_seats})")

    except FileNotFoundError:
        print("[-] Failed to open courses.txt. File not found.")
        return
    except:
        print("[-] Failed to open enrollments.txt")
        return

    # If no courses available
    if not courses:
        print("[-] No courses available to edit.")
        return

    for course in courses: #if course available then print out
        print(course)

    # Select course to edit
    while True:
        course_id = input("Enter course ID to edit or 'back' to exit: ").strip()
        if not course_id.strip().isalnum():
            print("[-] course ID cannot contain special characters! Please Try Again!")
            continue
        if not course_id:
                print("[-] Invalid ID,Please enter again.")
        if course_id.lower() == "back": #user enter back can back to main menu.
            return
        if not helper.course_id_exists(course_id, file_name): #check course_id is inside the file or not
            print("[-] Course ID does not exist. Try again.")
            continue
        break

    enrolled_students = 0
    try:
        with open(enrollment_file, "r", encoding="utf-8") as file:
            for line in file:
                if not line.startswith("Student ID"):
                    data = line.strip().split(",")
                    if len(data) >= 4:
                        enrolled_course_id = data[1].strip().lower() #check course id and enrolled course id is same or not
                        enrollment_status = data[3].strip().lower() #check status is active or not.
                        if enrolled_course_id.lower() == course_id.lower() and enrollment_status == "active":
                            enrolled_students += 1 
                        #check how many students are enrolled this course.
    except FileNotFoundError:
        print("[-] Warning: enrollments.txt not found. Cannot check enrollments.")

    # Find the course in file
    for i, line in enumerate(lines):
        #this code is find which line is the course_id that user want to edit 
        #i is the index of the line
        #line is the content of the line
        parts = line.strip().split(",")
        if parts[0].strip().lower() == course_id.lower():
            original_course_id = parts[0]
            course_name = parts[1]
            available_seats = parts[2]
            max_seats = parts[3]
            break
    print('-' * 40)
    print(f"Course ID: {original_course_id}")
    print(f"Course Name: {course_name}")
    print(f"Available Seats: {available_seats}")
    print(f"Maximum Seats: {max_seats}")
    print(f"Currently Enrolled Students: {enrolled_students}")

    # Editing options
    while True:
        print("-" * 40)
        print("[1] - Course ID")
        print("[2] - Course Name")
        print("[3] - Maximum Seats")
        print("[4] - Back")
        
        field_to_edit = input("Which field do you want to edit?: ").strip()

        if field_to_edit == "1":
            while True:
                new_course_id = input("Enter new course ID: ").strip().upper()
                if not new_course_id.strip().isalnum():
                    print("[-] course ID cannot contain special characters! Please Try Again!")
                    continue
                if not new_course_id: #if user not enter anything then it will run this code
                    print("[-] Invalid ID,Please enter again.")
                    continue
                if helper.course_id_exists(new_course_id, file_name): #check if the course id that user input is exist or not.
                    print("[-] Course ID already exists. Please enter a different course ID.")
                else:
                    break
            parts[0] = new_course_id  #save new id into parts[0]
            while True:
                if_update = input("This action will update all enrollment records with the same course ID to the new course ID? (Y/N): ")
                if_update = if_update.strip().upper()
                if  if_update == 'Y':
                    helper.update_course_id(course_id,new_course_id)
                    break
                elif if_update == 'N':
                    print("[-] The course ID was not updated!")
                    return
                else:
                    print("[-] Invalid Input! Please input Y or N")

            break

        elif field_to_edit == "2":
            while True:
                new_course_name = input("Enter new course name: ").strip()
                if not new_course_name.strip().replace(" ","").isalnum():
                    print("[-] course ID cannot contain special characters! Please Try Again!")
                    continue
                if not new_course_name: #same as course id
                    print("[-] Invalid Name,Please enter again.")
                    continue
                if helper.course_name_exists(new_course_name, file_name):
                    print("[-] Course name already exists. Please enter a different course name.")
                else:
                    break
            parts[1] = new_course_name
            break

        elif field_to_edit == "3":
            while True:
                try:
                    new_max_seats = int(input("Enter new maximum seats: ").strip())

                    if new_max_seats < enrolled_students:
                        print(f"[-] Error: Maximum seats cannot be lower than {enrolled_students} (currently enrolled students).") #check maximum seats is greater then enrolled student or not.
                        continue 

                    if enrolled_students != 0 and new_max_seats < int(available_seats): #check maximum seats is smaller than available seats or not
                        print("[-] Maximum seats can't be smaller than available seats.") #if yes then print this
                        continue
                    break
                except ValueError: #same as available seats.
                    print("[-] Enter a valid number.")
            new_course_seats = (int(new_max_seats) - int(enrolled_students)) #new max seats will also change new available seats so if enrolled student = 2 maximum = 2 then available = 0
            parts[2] = str(new_course_seats)
            parts[3] = str(new_max_seats) 
            break

        elif field_to_edit == "4": #user choose back so return to main menu.
            return
        else:
            print("[-] Invalid choice. Please enter 1, 2, 3 or 4.") #if user not input 1-4 then will print this.
            continue

    # Update the file content
    lines[i] = ",".join(parts) + "\n"

    try:
        with open(file_name, "w", encoding="utf-8") as file: 
            file.writelines(lines) 
            #write the new data to the file
        print("[+] Course updated successfully.")
    except:
        print("[-] Failed to open this file")
