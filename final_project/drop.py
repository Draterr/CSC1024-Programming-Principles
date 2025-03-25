import helper
import datetime

def drop_course():
    """

    This function will drop a course for a student if they are eligible to be dropped.

    """
    while True:
            #Ask the user for the Course ID
            try:
                with open("courses.txt","r") as file:
                    content = file.readlines()
                    if len(content) < 2:
                        print("[-] courses.txt has no records!\n")
                        print("[-] Please add a course to the system!")
                        return
                    print("\nCourse ID")
                    print("="*40)
                    #display the available courses to be dropped
                    for i in content:
                        details = i.split(",")
                        course_id = details[0]
                        if course_id != "Course ID":
                            print(f"{course_id:<7}")
                    print("="*40)
            except:
                print("[-] Failed to open courses.txt")
                return
            while True:
                course_id = input("\nWhich Course would you like to drop? Enter the Course ID or 'back' to back: \n").upper()
                if course_id.strip().lower() == 'back':
                    return
                #Ensure that the Course_ID is of a probable length
                if len(course_id) > 20 or len(course_id) <= 0 :
                    print("[-] Invalid Course Id")
                    continue

                #ensure that the course exists in our system
                if not helper.course_id_exists(course_id,"courses.txt"):
                    print("[-] Course is not recorded! Please add it to the system!")
                    continue
                else:
                    break

            #Ask the user for their studentID
            while True:
                student_id = input("Enter your student ID or 'back' to back: \n")
                if student_id.strip().lower() == 'back':
                    return
                #Ensure that the student_id is of a probable length
                if len(student_id) > 9 or len(course_id) <= 0:
                    print("[-] Invalid Student Id")
                    continue
                #ensure that the student id exists in our system
                if not helper.student_id_exists(student_id,"students.txt"):
                    print("[-] Student ID is not recorded! Please add it to the system!")
                    continue
                else:
                    break

            #first check if the student is enrolled in the course
            enroll_status = helper.check_if_student_is_enrolled(student_id,course_id)
            #if they are enrolled in that course, then we can proceed with dropping
            if enroll_status:
                #we check if the course exists and free up one seat for the course
                update_status = helper.update_course_availability(course_id,1)
                #if update_status returns 1(success), we find the student's Active record in enrollments.txt for this course,
                #then we change the status from "Active" to "Dropped" and update the date to the current day
                if update_status == 1:
                    #Read all the data from enrollments.txt into the temp_memory list 
                    try:
                        with open("enrollments.txt","r") as old_file_handler:
                            temp_memory = old_file_handler.readlines()

                            #validate that enrollments.txt has data
                            if len(temp_memory) < 2:
                                print("[-] There are no enrollment data")
                                continue

                        #iterate over each line in the enrollments.txt file, skipping over the header(temp_memory[0])
                        for line in range(1,len(temp_memory)):
                                #the information are stored in a csv format so we delimit each line by ","
                                details = temp_memory[line].split(",")

                                #Define variables for information we need
                                current_student_id = details[0]
                                current_course_id = details[1]
                                #Remove the trailing "/-" placeholder previously for non existent dropped date
                                enrollment_date = details[2].strip().rstrip("/ -")
                                enrollment_status = details[3]

                                #check if the current line's course_id,student_id is the same as the user provided one,
                                #and check if that record is currently Active,
                                #if so we change the status from Active to Dropped, signfying that the user has dropped the course 
                                if current_course_id == course_id and current_student_id == student_id and enrollment_status.strip() == "Active":
                                    enrollment_status = "Dropped"

                                    #Reconstruct the line with the new status
                                    print(enrollment_date)
                                    new_info = f"{current_student_id},{current_course_id},{enrollment_date} / {datetime.date.today()},{enrollment_status}\n" 

                                    #update the old file contents with the new line
                                    temp_memory[line] = new_info 

                                    #overwrite enrollments.txt with the new file contents containing the new line
                                    try:
                                        with open("enrollments.txt","w") as new_file_handler:
                                            new_file_handler.writelines(temp_memory)
                                        print(f"[+] Successfully Dropped Course {course_id}")
                                        continue
                                    except:
                                        print("[-] Failed to open enrollments.txt file")
                                        continue
                    except:
                            print("[-] Failed to open enrollments.txt file")
                            continue
                #If the course is not found
                elif update_status == -1:
                    print("[-] Courses not found")
                    continue
                elif update_status == -2:
                    print("[-] Failed to open enrollments.txt file")
                    continue
            else:
                print("[-] You are not currently enrolled")
                continue
