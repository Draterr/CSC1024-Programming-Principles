import helper

def delete_course():
    file_name = "courses.txt"
    try:
        with open(file_name, "r+", encoding="utf-8") as file:  #r+ means read and write
            print("Delete a course")

            print("Available courses:")
            courses = []
            for line in file:
                if not line.startswith("Course ID"): #same as edit_course, delete the first line
                    parts = line.strip().split(",")
                    if len(parts) == 4:
                        course_id, course_name, available_seats, course_seats = parts
                        courses.append(f"{course_id} - {course_name} ({available_seats}) ({course_seats})")
    except:
        print("Failed to open courses.txt")

        if not courses:
            print("No courses available to delete.")
            return     #if no courses to delete then go to the main menu
        
        for course in courses:
            print(course)

        while True:
            course_id = input("Enter course id to delete or back to exit: ")
            if course_id.lower() == "back":
                return
            if not helper.course_id_exists(course_id, file_name):
                print("Course ID does not exist.")
                continue
            break

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except:
        print("Failed to open courses.txt")

    try:
        with open(file_name, "w", encoding="utf-8") as file: #this will empty the line
            for line in lines:
                if not line.split(",")[0].strip().lower() == course_id.lower(): 
                    #if the course_id is not the same as the user input then write the line to the file
                    #if the course id is the same as the user input then it will not write the line to the file thats means delete the line
                    file.write(line)
    except:
        print("Failed to open courses.txt")

    print("Course deleted successfully.")