# define view_available_courses functionality that will show the avaialable courses.
def view_available_courses():
    
#try block is used to handle errors such as inproper format for data in files and missing files.
    try:
#open the courses.txt file in read mode so that it is readable
        file = open("courses.txt", "r")
        courses = file.readlines()
        file.close()
        
#no courses available is printed if the file is empty
        if not courses:
            print("No courses available.")
            return
        
#print the title Available Courses.
        print("Available Courses:")
        
#print separator line to separate the details neatly and insert the column headers
        print("-" * 70)
        print(f"{'Course ID':<10}{'Course Name':<30}{'Available Seats':<16}{'Maximum Seats':<20}")
        print("-" * 70)
        
#.strip() is used to avoid any unnecessary spaces or newline characters
        for course in courses:
            course_data = course.strip().split(",")
            
            if course_data[0] == 'Course ID':
                continue
#Check if the course data contains exactly three elements (Course ID, Course Name, Available Seats) and then assign them to separate variables.
            if len(course_data) == 4:
                course_id = course_data[0]  
                course_name = course_data[1]  
                available_seats = course_data[2]  
                maximum_seats = course_data[3]  
                print(f"{course_id:<10}{course_name:<30}{available_seats:<16}{maximum_seats:<20}")  
            else:
                print("ERROR:Invalid format for course data in 'courses.txt'.")#print error when the course data format is wrong
    except FileNotFoundError:
        print("ERROR: 'courses.txt' file not found.")#print error whe the file cannot be found
    except Exception as e:
        print(f"An error occurred: {e}")
