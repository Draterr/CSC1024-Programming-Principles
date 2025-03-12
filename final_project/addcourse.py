import os

file_name = "courses.txt"

if not os.path.exists(file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        file.write("Course ID,Course Name,Available Seats\n")

def course_id_exists(course_id, file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            if line.startswith(course_id + ","):
                return True
    return False

def course_name_exists(course_name, file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            if len(line.split(",")) > 1 and course_name == line.split(",")[1].strip():
                return True
    return False

def add_course():
    print("=" * 40)
    print("Add a new course")
    print("=" * 40)

    while True:
        course_id = input("Enter course id: ")
        if course_id.lower() == "back":
                return
        if course_id_exists(course_id, file_name):
            print("Course ID already exists. Please enter a different course id.")
        else:
            break

    while True:
        course_name = input("Enter course name: ")
        if course_name_exists(course_name, file_name):
            print("Course name already exists. Please enter a different course name.")
        else:
            break

    while True:
        course_seats = input("Enter maximum course seats: ")
        if not course_seats.isdigit():
            print("Please enter a valid number.")
        else:
            break

    with open(file_name, "a", encoding="utf-8") as file:
        file.write(f"{course_id},{course_name},{course_seats}\n")

    print("Course added successfully.")

    user_continue = input("Do you want to add another course? (yes/no): ")
    if user_continue.lower() == "yes" or user_continue.lower() == "y":
        add_course()
    elif user_continue.lower() == "no" or user_continue.lower() == "n":
        main()
    else:
        print("Invalid input. Returning to main menu.")
    
    return

def edit_course():
    with open(file_name, "r+", encoding="utf-8") as file:
        print("=" * 40)
        print("Edit a course")
        print("=" * 40)

        print("Available courses:")
        courses = []
        for line in file:
            if not line.startswith("Course ID"):
                parts = line.strip().split(",")
                if len(parts) == 3:
                    course_id, course_name, course_seats = parts
                    courses.append(f"{course_id} - {course_name} ({course_seats})")
        
        if not courses:
            print("No courses available to edit.")
            return
        
        for course in courses:
            print(course)

        while True:
            course_id = input("Enter course id to edit or back to exit: ")
            if course_id.lower() == "back":
                return
            if not course_id_exists(course_id, file_name):
                print("Course ID does not exist.")
                continue
            break

        with open(file_name, "r", encoding="utf-8") as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            if line.startswith(course_id + ","):
                parts = line.strip().split(",")
                course_name = parts[1]
                course_seats = parts[2]
                break

        print(f"Course ID: {course_id}")
        print(f"Course Name: {course_name}")
        print(f"Available Seats: {course_seats}")

        while True:
            field_to_edit = input("Which field do you want to edit? (id/name/seats): ").strip().lower()
            if field_to_edit == "id":
                while True:
                    new_course_id = input("Enter new course id: ")
                    if course_id_exists(new_course_id, file_name):
                        print("Course ID already exists. Please enter a different course id.")
                    else:
                        break
                parts[0] = new_course_id
                break
            elif field_to_edit == "name":
                while True:
                    new_course_name = input("Enter new course name: ")
                    if course_name_exists(new_course_name, file_name):
                        print("Course name already exists. Please enter a different course name.")
                    else:
                        break
                parts[1] = new_course_name
                break
            elif field_to_edit == "seats":
                while True:
                    new_course_seats = input("Enter new available seats: ")
                    if not new_course_seats.isdigit():
                        print("Please enter a valid number.")
                    else:
                        break
                parts[2] = new_course_seats
                break
            else:
                print("Invalid field. Please enter 'id', 'name', or 'seats'.")
                continue

        lines[i] = ",".join(parts) + "\n"

        with open(file_name, "w", encoding="utf-8") as file:
            file.writelines(lines)

        print("Course updated successfully.")

def delete_course():
    with open(file_name, "r+", encoding="utf-8") as file:
        print("=" * 40)
        print("Delete a course")
        print("=" * 40)

        print("Available courses:")
        courses = []
        for line in file:
            if not line.startswith("Course ID"):
                parts = line.strip().split(",")
                if len(parts) == 3:
                    course_id, course_name, course_seats = parts
                    courses.append(f"{course_id} - {course_name} ({course_seats})")

        if not courses:
            print("No courses available to delete.")
            return
        
        for course in courses:
            print(course)

        while True:
            course_id = input("Enter course id to delete or back to exit: ")
            if course_id.lower() == "back":
                return
            if not course_id_exists(course_id, file_name):
                print("Course ID does not exist.")
                continue
            break

        with open(file_name, "r", encoding="utf-8") as file:
            lines = file.readlines()

        with open(file_name, "w", encoding="utf-8") as file:
            for line in lines:
                if not line.startswith(course_id + ","):
                    file.write(line)

        print("Course deleted successfully.")

def main():
    while True:
        print("=" * 40)
        print("[1] Add a new course")
        print("[2] Edit a course")
        print("[3] Delete a course")
        print("[4] Back")
        print("=" * 40)
        user_input = input("Enter your choice: ")
        if not user_input.isdigit() or int(user_input) < 1 or int(user_input) > 4:
            print("Invalid choice. Please try again.")
            continue
        if user_input == "1":
            add_course()
        elif user_input == "2":
            edit_course()
        elif user_input == "3":
            delete_course()
        elif user_input == "4":
            exit()
            

if __name__ == "__main__":
    main()