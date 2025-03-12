import helper

def edit_course():
    file_name = "courses.txt"

    # Read course file safely
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            print("Edit a course")
            print("Available courses:")

            courses = []
            lines = file.readlines()

            for line in lines:
                if not line.startswith("Course ID"):  #this is to skip the first line of the file which is the header
                    parts = line.strip().split(",")
                    if len(parts) == 4: #because have 4 fields in the courses.txt file so is parts == 4
                        course_id, course_name, available_seats, maximum_seats = parts #example: part[0] = course_id, part[1] = course_name, part[2] = available_seats, part[3] = maximum_seats
                        courses.append(f"{course_id} - {course_name} ({available_seats}) ({maximum_seats})")

    except FileNotFoundError:
        print("Failed to open courses.txt. File not found.")
        return
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return

    # If no courses available
    if not courses:
        print("No courses available to edit.")
        return

    for course in courses:
        print(course)

    # Select course to edit
    while True:
        course_id = input("Enter course ID to edit or 'back' to exit: ").strip()
        if course_id.lower() == "back":
            return
        if not helper.course_id_exists(course_id, file_name): #check course_id is inside the file or not
            print("Course ID does not exist. Try again.")
            continue
        break

    # Find the course in file
    for i, line in enumerate(lines):
        #this code is find which line is the course_id that user want to edit 
        #i is the index of the line
        #line is the content of the line
        parts = line.strip().split(",")
        '''
        if line = "MTH202,Mathematics,20,25\n"
        parts = line.strip().split(",")
        strip = "MTH202,Mathematics,20,25" delete the space in the front and back
        split = ["MTH202","Mathematics","20","25"] use , to split the string                example:
        parts[0] = "MTH202"
        parts[1] = "Mathematics"
        '''
        if parts[0].strip().lower() == course_id.lower():
            original_course_id = parts[0]
            course_name = parts[1]
            available_seats = parts[2]
            max_seats = parts[3]
            break

    print(f"Course ID: {original_course_id}")
    print(f"Course Name: {course_name}")
    print(f"Available Seats: {available_seats}")
    print(f"Maximum Seats: {max_seats}")

    # Editing options
    while True:
        print("-" * 40)
        print("[1] - Course ID")
        print("[2] - Course Name")
        print("[3] - Available Seats")
        print("[4] - Maximum Seats")
        print("[5] - Back")
        
        field_to_edit = input("Which field do you want to edit?: ").strip()

        if field_to_edit == "1":
            while True:
                new_course_id = input("Enter new course ID: ").strip()
                if helper.course_id_exists(new_course_id, file_name):
                    print("Course ID already exists. Please enter a different course ID.")
                else:
                    break
            parts[0] = new_course_id  
            break

        elif field_to_edit == "2":
            while True:
                new_course_name = input("Enter new course name: ").strip().lower()
                if helper.course_name_exists(new_course_name, file_name):
                    print("Course name already exists. Please enter a different course name.")
                else:
                    break
            parts[1] = new_course_name
            break

        elif field_to_edit == "3":
            while True:
                try:
                    new_course_seats = int(input("Enter new available seats: ").strip())
                    if new_course_seats > int(max_seats):
                        print("Available seats cannot be greater than maximum seats.")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid number.")
            parts[2] = str(new_course_seats)
            break

        elif field_to_edit == "4":
            while True:
                try:
                    new_max_seats = int(input("Enter new maximum seats: ").strip())
                    if new_max_seats < int(available_seats):
                        print("Maximum seats can't be smaller than available seats.")
                        continue
                    break
                except ValueError:
                    print("Enter a valid number.")
            parts[3] = str(new_max_seats)
            break

        elif field_to_edit == "5":
            return
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")
            continue

    # Update the file content
    lines[i] = ",".join(parts) + "\n"
    #parts = ["CS101", "Computer Science", "25", "30"]
    #",".join(parts)  output: "CS101,Computer Science,25,30"
    #save new data
    #let ["id","name","seats"] become "id,name,seats" and add a new line
    #if no this code then it will not update new data to the file

    try:
        with open(file_name, "w", encoding="utf-8") as file:
            file.writelines(lines) 
            #write the new data to the file
        print("Course updated successfully.")
    except Exception as e:
        print(f"Failed to update the course file: {e}")
