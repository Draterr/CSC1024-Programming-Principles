import helper
def delete_course():
    file_name = "courses.txt"
    with open(file_name, "r+", encoding="utf-8") as file:
        print("Delete a course")

        print("Available courses:")
        courses = []
        for line in file:
            if not line.startswith("Course ID"):
                parts = line.strip().split(",")
                if len(parts) == 4:
                    course_id, course_name, available_seats, course_seats = parts
                    courses.append(f"{course_id} - {course_name} ({available_seats}) ({course_seats})")

        if not courses:
            print("No courses available to delete.")
            return
        
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

        with open(file_name, "r", encoding="utf-8") as file:
            lines = file.readlines()

        with open(file_name, "w", encoding="utf-8") as file:
            for line in lines:
                if not line.split(",")[0].strip().lower() == course_id.lower():
                    file.write(line)

        print("Course deleted successfully.")