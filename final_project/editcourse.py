import helper 

def edit_course():
    file_name = "courses.txt"
    with open(file_name, "r+", encoding="utf-8") as file:
        print("Edit a course")

        print("Available courses:")
        courses = []
        for line in file:
            if not line.startswith("Course ID"):
                parts = line.strip().split(",")
                if len(parts) == 4:
                    course_id, course_name, available_seats,maximum_seats = parts
                    courses.append(f"{course_id} - {course_name} ({available_seats}) ({maximum_seats})")
        
        if not courses:
            print("No courses available to edit.")
            return
        
        for course in courses:
            print(course)

        while True:
            course_id = input("Enter course id to edit or back to exit: ")
            if course_id.lower() == "back":
                return
            if not helper.course_id_exists(course_id, file_name):
                print("Course ID does not exist.")
                continue
            break

        with open(file_name, "r", encoding="utf-8") as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            if line.split(",")[0].strip().lower() == course_id.lower():
                parts = line.strip().split(",")
                original_course_id = parts[0]  # Store the original course ID
                course_name = parts[1]
                available_seats = parts[2]
                max_seats = parts[3]
                break

        print(f"Course ID: {original_course_id}")
        print(f"Course Name: {course_name}")
        print(f"Available Seats: {available_seats}")
        print(f"Maximum Seats: {max_seats}")

        while True:
            field_to_edit = input("Which field do you want to edit? (id/name/seats): ").strip().lower()
            if field_to_edit.lower() == "course id":
                while True:
                    new_course_id = input("Enter new course id: ")
                    if helper.course_id_exists(new_course_id, file_name):
                        print("Course ID already exists. Please enter a different course id.")
                    else:
                        break
                parts[0] = new_course_id
                break
            elif field_to_edit.lower() == "course name":
                while True:
                    new_course_name = input("Enter new course name: ")
                    if helper.course_name_exists(new_course_name, file_name):
                        print("Course name already exists. Please enter a different course name.")
                    else:
                        break
                parts[1] = new_course_name
                break
            elif field_to_edit.lower() == "available seats":
                while True:
                    new_course_seats = input("Enter new available seats: ")
                    if new_course_seats > max_seats:
                        print("Maximum seats can't be smaller than seats available")
                        continue
                    if not new_course_seats.isdigit():
                        print("Please enter a valid number.")
                    else:
                        break
                parts[2] = new_course_seats
                break
            elif field_to_edit.lower() == "maximum seats":
                while True:
                    new_course_seats = input("Enter new maximum seats: ")
                    if new_course_seats < available_seats:
                        print("Maximum seats can't be smaller than seats available")
                        continue
                    if not new_course_seats.isdigit():
                        print("Please enter a valid number.")
                    else:
                        break
                parts[3] = new_course_seats
                break
            else:
                print("Invalid field. Please enter 'id', 'name', 'seats' or 'max_seats'.")
                continue

        lines[i] = ",".join(parts) + "\n"

        with open(file_name, "w", encoding="utf-8") as file:
            file.writelines(lines)
#hi
        print("Course updated successfully.")