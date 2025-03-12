import helper

def delete_course():
    file_name = "courses.txt"
    courses = []

    try:
        with open(file_name, "r+", encoding="utf-8") as file:  #r+ means read and write
            print("Delete a course")

            print("Available courses:")
            for line in file:
                if not line.startswith("Course ID"): #same as edit_course, delete the first line
                    parts = line.strip().split(",") #split id,name,available seats and maximum seats into 4 parts. 
                    if len(parts) == 4:
                        course_id, course_name, available_seats, course_seats = parts
                        courses.append(f"{course_id} - {course_name} ({available_seats}) ({course_seats})")

    except FileNotFoundError:
        print("Error: courses.txt not found.") #if user no courses.txt then will output this
        return
    except:
        print("Failed to open this file")
        return

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
            #if user input exists course id then it will print Course ID does not exist and let user input again until id is not exists
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