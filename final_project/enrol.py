import helper
import datetime

def enrol_in_course():
    """

    This function will enrol a student to a course if they are eligible to be enrolled.

    """
    while True:
        course_id = ""
        student_id = ""
        while True:
            try:
                with open("courses.txt","r") as file:
                    content = file.readlines()
                    #validate that courses.txt has records
                    if len(content) < 2:
                        print("courses.txt has no records!\n")
                        print("Please add a course to the system!")
                        return
                    print("\nCourse ID")
                    print("="*40)
                    #display the available courses to be enrolled
                    for i in content:
                        details = i.split(",")
                        course_id = details[0]
                        if course_id != "Course ID":
                            print(f"{course_id:<7}")
                    print("="*40)
            except:
                print("Failed to open courses.txt")
                return

            #Ask the user for the Course ID
            course_id = input("Which Course would you like to enroll in? Enter the Course ID or 'back' to exit: \n")
            if course_id.strip().lower() == 'back':
                return

            #Ensure that the course exists in the system
            if not helper.course_id_exists(course_id,"courses.txt"):
                print("Course ID is not recorded! Please add it to the system")
                continue
            #Ensure that the Course_ID is of a probable length
            if len(course_id) > 20 or len(course_id) <= 0 : 
                print("Invalid Course Id")
                continue
            else:
                break
        while True:
            #Ask the user for their studentID
            student_id = input("Enter your student ID or 'back' to exit: \n")
            if student_id.strip().lower() == 'back':
                return
            #ensure that the student id exists in our records
            if not helper.student_id_exists(student_id,"students.txt"):
                print("Student ID is not recorded! Please add it to the system")
                continue
            else:
                #Ensure that the student_ID is of a probable length
                if len(student_id) > 9 or len(student_id) <= 0 :
                    print("Invalid Student Id")
                    continue
                else:
                    break
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
                print(f"[+] Successfully Enrolled to {course_id}\n")
            #If update_status returns 0(Course is full), tell the user the course is full
            elif update_status == 0:
                print("[-] The Course is full\n")
                continue
            elif update_status == -1:
            #If update_status returns -1(Course not found), tell the user the course does not exist 
                print("[-] Courses not found\n")
                continue
            elif update_status == -2:
                print("[-] Failed to open enrollments.txt\n")
                continue
        #if the user is already enroll, tell the user they are already enrolled and exit the function
        else:
            print("[-] You are already enrolled\n")
            continue

        
