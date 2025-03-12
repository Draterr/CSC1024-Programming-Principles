import helper
import datetime

def enrol_in_course(student_id,course_id):
    """

    This function will enrol a student to a course if they are eligible to be enrolled.

    """
    #first check whether the student is already enrolled to this course
    enroll_status = helper.check_if_student_is_enrolled(student_id,course_id)

    #if not already enrolled, we can proceed with the enrollment
    if not enroll_status:
        #we first check if there are still available seats in the course,
        #if we do, then update the number of available seats in courses.txt
        update_status = helper.update_course_availability(course_id,-1)

        #If update_status returns 1(success), inset a record to the enrollments.txt 
        if update_status == 1:
            with open("enrollments.txt","a") as enrollment_file_handler:
                #define the infromation 
                status = "Active"
                #Get Current date
                enrollment_date = datetime.date.today()
                #Concantenate the infromation together to form the record
                enrollment_information = f"{student_id},{course_id},{enrollment_date} / -,{status}\n"
                #insert the record to the end of the file
                enrollment_file_handler.write(enrollment_information)
            return f"[+] Successfully Enrolled to {course_id}"
        #If update_status returns 0(Course is full), tell the user the course is full
        elif update_status == 0:
            return "[-] The Course is full"
        elif update_status == -1:
        #If update_status returns -1(Course not found), tell the user the course does not exist 
            return "[-] Courses not found"
    #if the user is already enroll, tell the user they are already enrolled and exit the function
    else:
        return "[-] You are already enrolled"
    
if __name__ == "__main__":
    print(enrol_in_course("s24134156","CSC1024"))