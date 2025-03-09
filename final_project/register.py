import os 
import datetime

"""

Course Registration System

This program allows students to:
- Enroll in courses
- Drop courses
- View their enrollment history
- View available courses
- Add new students to the system
- Add new course to the system
- View Student Information

The system maintains records of students, courses, and enrollments.

"""
def initial_data_preparation(files):
    """
    Creates Initial Files.

    Create the students record file, courses file and enrollment file and initialize them with csv format headers.

    """

    # Create required files if they don’t exist
    for individual_file_properties in files:
        file_name = individual_file_properties[0]
        file_header = individual_file_properties[1]
        #we check if the file already exists to prevent writing extra headers
        if not os.path.isfile(file_name):
            with open(file_name,"w+") as file_handle:
                file_handle.write(file_header)

def display_menu(title,options):
    """
    Create Help Menu.

    This function creates the initial menu displayed to the user.

    """
    #print the initial title, center it to the middle, add "=" to prettify the output 
    #prompt user for selection, the number of options is dynamic, it changes depending on the size of the options argument
    print(f"\n{title.center(50)}")
    print("=" * 50)
    print(f"Choose Between 1 - {len(options)},")

    #iterate over the options list to retrieve the option_number and option_text
    for option in options:
        option_number = option[0]
        option_text = option[1]

        #Left-Just option_number by 5 to keep alignment consistent incase we get to double digit option numbers.
        #Ex: [10]\t = 5 characters
        print(f"{option_number:<5} {option_text}")

    #more "=" to contain the output
    print("="*50)


def add_new_student():
    return

def add_new_course():
    return

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


def enrol_in_course(student_id,course_id):
    """

    This function will enrol a student to a course if they are eligible to be enrolled.

    """
    #first check whether the student is already enrolled to this course
    enroll_status = check_if_student_is_enrolled(student_id,course_id)

    #if not already enrolled, we can proceed with the enrollment
    if not enroll_status:
        #we first check if there are still available seats in the course,
        #if we do, then update the number of available seats in courses.txt
        update_status = update_course_availability(course_id,-1)

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

def drop_course(student_id,course_id):
    """

    This function will drop a course for a student if they are eligible to be dropped.

    """
    
    #first check if the student is enrolled in the course
    enroll_status = check_if_student_is_enrolled(student_id,course_id)
    #if they are enrolled in that course, then we can proceed with dropping
    if enroll_status:
        #we check if the course exists and reduce one seat for the course
        update_status = update_course_availability(course_id,1)
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

    #if they are not enrolled, we inform the user that they are not enrolled in that course and are not permitted to drop it
    else:
        return "[-] You are not currently Enrolled in this Course"

def view_enrollment_history(student_id):
    enrollment_sum = 0
    with open("enrollments.txt","r") as file_handler:
        file_contents = file_handler.readlines()
        for lines in range(1,len(file_contents)):
            current_line = file_contents[lines]
            details = current_line.split(",")
            current_student_id = details[0]
            current_course_id = details[1]
            current_enrollment_or_drop_date = details[2]
            current_status = details[3]
            if current_student_id == student_id:
                enrollment_sum += 1
                print(f"- {current_course_id:<11} {current_enrollment_or_drop_date:<24} {current_status:<8}")
        if enrollment_sum == 0:
            return "This Student has no enrollment history"
        else:
            return f"This student has enrolled {enrollment_sum} times"

def view_available_course():
    return

def view_student_information():
    return


def main():
    """
    A main function to encapsulate the whole program into one function.

    By encapsulating all the functions into the main function, the execution flow is easier to follow and functions can be sepearated easily,
    easing the debugging process.

    By centralising all the variables definition, all the variables are visible within the main function,the code can be modified easily,
    and by defining variables in the main function and passing it as an arugment to the function, we improve the reusability of the functions.
    """

    #nested list for the filename of the file to be created and the header of that file
    #inner list consists of [{filename},{file_header}]
    files = [["students.txt","Student ID,Name,Contact\n"],
             ["courses.txt","Course ID,Course name, Seats Available,Maximum Seats\n"],
             ["enrollments.txt","Student ID,Course ID,Enrollment date/Dropped Date,Status\n"]]
    initial_data_preparation(files)


    #nested list for the option numbers and option text to allow for better text alignment
    #inner list consists of [{option_numbers},{option_text}]
    options = [["[1]","Add a Student"],
               ["[2]","Add a New Course"],
               ["[3]","Enrol in a Course"],
               ["[4]","Drop a Course"],
               ["[5]","View Available Courses"],
               ["[6]","View Student information"],
               ["[7]","View Enrollment History"],
               ["[8]","Exit"]]
    title = "Course Registration System"
    display_menu(title,options)

    #define user_selection to be an empty string to ensure the while loop's condition is true
    user_selection = ""

    #The main while loop to keep the program running until the user chooses the exit option
    while user_selection != "8":
        #prompt user for selection, the number of options is dynamic, it changes depending on the size of the options nested list
        user_selection = input(f"Select an Option Between 1 - {len(options)}: ")
        match user_selection:
            case "1":
                print("Please Enter the information in the following order: StudentID,Name,Contact")
                add_new_student() 
            case "2":
                print("Please Enter the information in the following order:Course ID,Course name, Seats Available,Maximum Seats")
                add_new_course()
            #If the user chooses to enroll in a course(Option  3)
            case "3":
                #Ask the user for the Course ID
                course_id = input("Which Course would you like to enroll in? Enter the Course ID: \n")

                #Ensure that the Course_ID is of a probable length
                if len(course_id) > 20:
                    print("Invalid Course Id")
                    continue

                #Ask the user for their studentID
                student_id = input("Enter your student ID: \n")

                #Ensure that the student_ID is of a probable length
                if len(student_id) > 9:
                    print("Invalid Student Id")
                    continue

                #Invoke the enrol_in_course function with the user input
                enrollment_status = enrol_in_course(student_id,course_id)
                
                #display the result
                print(enrollment_status)
                continue
            case "4":
                #Ask the user for the Course ID
                course_id = input("Which Course would you like to drop? Enter the Course ID: \n")

                #Ensure that the Course_ID is of a probable length
                if len(course_id) > 20:
                    print("Invalid Course Id")
                    continue

                #Ask the user for their studentID
                student_id = input("Enter your student ID: \n")
                #Ensure that the student_id is of a probable length
                if len(student_id) > 9:
                    print("Invalid Student Id")
                    continue

                #Invoke the drop_course function with the user input
                enrollment_status = drop_course(student_id,course_id)

                #display the result
                print(enrollment_status)
                continue
            case "5":
                view_available_course()
            case "6":
                view_student_information()
            case "7":
                #Ask the user for their studentID
                student_id = input("Enter Student ID: \n")

                #Ensure that the student_id is of a probable length
                if len(student_id) > 9:
                    print("Invalid Student Id")
                    continue
                histories = view_enrollment_history(student_id)
                print(histories)
                continue
            #Exits If the user chooses option 7 or type "Exit"
            case "8"|"Exit":
                print("Exiting ...")
                break
            #If the user enters anything that is not a valid option
            case _:
                print("Invalid Selection!")
                continue

#Call main function to run the program
main()
