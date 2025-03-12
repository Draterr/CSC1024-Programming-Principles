import helper
import datetime

def drop_course(student_id,course_id):
    """

    This function will drop a course for a student if they are eligible to be dropped.

    """
    
    #first check if the student is enrolled in the course
    enroll_status = helper.check_if_student_is_enrolled(student_id,course_id)
    #if they are enrolled in that course, then we can proceed with dropping
    if enroll_status:
        #we check if the course exists and reduce one seat for the course
        update_status = helper.update_course_availability(course_id,1)
        #if update_status returns 1(success), we find the student's Active record in enrollments.txt for this course,
        #then we change the status from "Active" to "Dropped" and update the date to the current day
        if update_status == 1:
            #Read all the data from enrollments.txt into the temp_memory list 
            with open("enrollments.txt","r") as old_file_handler:
                temp_memory = old_file_handler.readlines()

                #validate that enrollments.txt has data
                if len(temp_memory) < 2:
                    return "[-] There are no enrollment data"

                #iterate over each line in the enrollments.txt file, skipping over the header(temp_memory[0])
                for line in range(1,len(temp_memory)):
                    #the information are stored in a csv format so we delimit each line by ","
                    details = temp_memory[line].split(",")

                    #Define variables for information we need
                    current_student_id = details[0]
                    current_course_id = details[1]
                    #Remove the trailing "/-" placeholder previously for non existent dropped date
                    enrollment_date = details[2].rstrip("/-")
                    enrollment_status = details[3]

                    #check if the current line's course_id,student_id is the same as the user provided one,
                    #and check if that record is currently Active,
                    #if so we change the status from Active to Dropped, signfying that the user has dropped the course 
                    if current_course_id == course_id and current_student_id == student_id and enrollment_status.strip() == "Active":
                        enrollment_status = "Dropped"

                        #Reconstruct the line with the new status
                        new_info = f"{current_student_id},{current_course_id},{enrollment_date} / {datetime.date.today()},{enrollment_status}\n" 

                        #update the old file contents with the new line
                        temp_memory[line] = new_info 

                        #overwrite enrollments.txt with the new file contents containing the new line
                        with open("enrollments.txt","w") as new_file_handler:
                            new_file_handler.writelines(temp_memory)
                        return f"[+] Successfully Dropped Course {course_id}"
        #If the course is not found
        elif update_status == -1:
            return "[-] Courses not found"