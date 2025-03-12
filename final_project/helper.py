def check_if_student_is_enrolled(student_id,course_id):
    """

    This function checks if a student is currently enrolled in a subject.

    """
    #Open the enrollments file 
    with open("enrollments.txt","r") as enrollment_file_handler:
        enrollment_data = enrollment_file_handler.readlines()
        #iterate over each line in the enrollments.txt file except for the header
        for enrollment_info_index in range(1,len(enrollment_data)):
            #The fields are comma separated so we can delimit them by ","
            enrollment_info = enrollment_data[enrollment_info_index].split(",")
            #Create variables for the required information
            enrolled_student_id = enrollment_info[0]
            current_course_id = enrollment_info[1]
            enrollment_status = enrollment_info[3]
            #If we find a row with the same student_id,course_id and enrollment_status is active,
            #then we've identified that the student is currently enrolled
            if enrolled_student_id == student_id and current_course_id == course_id and enrollment_status.strip() == "Active":
                return True
        #No record found return False
        return False

def update_course_availability(course_id,number):
    """

    This function updates the number of available seats in the courses.txt file.

    """
    #We first open the courses.txt file in read mode to read out all the lines
    with open("courses.txt","r") as old_file_handler:
        temp_memory = old_file_handler.readlines()
        if len(temp_memory) <  2:
            print("[-] There are no course data")
            return -1
        
        #Iterate over each lines,skipping through the header(temp_memory[0]) to look for a matching course ID 
        for course_information in range(1,len(temp_memory)):

            #the information are stored in a csv format so we delimit each line by ","
            details = temp_memory[course_information].split(",")
            current_course_id = details[0]
            course_name = details[1]
            available_seats = int(details[2])
            maximum_seats = int(details[3])

            #Check if the course exists by checking if that course_id exists
            #if we find a match we will either increment the available seats(add +1) or decrement(add -1)
            #We need to ensure that we don't decrement till negative and we don't increment above the maximum amount of seats
            if course_id == current_course_id:
                    if (number == -1 and available_seats != 0) or (number == 1 and available_seats < maximum_seats):
                        available_seats += number
                        #Update the temp_memory list with the new amount of available seats
                        new_info = f"{current_course_id},{course_name},{available_seats},{maximum_seats}\n"
                        temp_memory[course_information] = new_info
                        #Overwrite the old courses.txt with a new courses.txt file with the update available seats information for that course
                        with open("courses.txt","w") as new_file_handler:
                            new_file_handler.writelines(temp_memory)
                        return 1 #"Successfully Enrolled to {course_id}/Successfully Dropped course"
                    else:
                        return 0 #"The course is full"

        return -1 #"Courses not found"

def course_id_exists(course_id, file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            if line.split(",")[0].strip().lower() == course_id.lower():
                return True
    return False

def course_name_exists(course_name, file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            if len(line.split(",")) > 1 and course_name == line.split(",")[1].strip():
                return True
    return False
