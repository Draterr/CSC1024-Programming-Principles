import os 
import datetime

"""
This Program is a Course Registration System

It creates data_
"""
def initial_data_preparation(files):
    """
    Creates Initial Files.

    Create the students record file, courses file and enrollment file and initialize them with csv format headers.

    """

    #iterate over a nested list called files to create each file, if we wanted to create a new file we just need to append a new list to the files list
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
    print(f"""\n{title.center(50)}\n{"="*50}\nChoose Between 1 - {len(options)},""")

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
    with open("enrollments.txt","r") as enrollment_file_handler:
        enrollment_data = enrollment_file_handler.readlines()
        for enrollment_info_index in range(1,len(enrollment_data)):
            enrollment_info = enrollment_data[enrollment_info_index].split(",")
            enrolled_student_id = enrollment_info[0]
            current_course_id = enrollment_info[1]
            enrollment_status = enrollment_info[3]
            if enrolled_student_id == student_id and current_course_id == course_id and enrollment_status.rstrip("\n") == "Active":
                return True
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
        
        #Iterate over each lines,skipping through the header to look for a matching course ID 
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


def enrol_in_course(student_id,course_id,enrollment_date):
    enroll_status = check_if_student_is_enrolled(student_id,course_id)
    if enroll_status == False:
        update_status = update_course_availability(course_id,-1)
        if update_status == 1:
            with open("enrollments.txt","a+") as enrollment_file_handler:
                status = "Active"
                enrollment_information = f"{student_id},{course_id},{enrollment_date},{status}\n"
                enrollment_file_handler.write(enrollment_information)
            return f"[+] Successfully Enrolled to {course_id}"
        elif update_status == 0:
            return "[-] The Course is full"
        elif update_status == -1:
            return "[-] Courses not found"
    else:
        return "[-] You are already enrolled"

def drop_course(student_id,course_id):
    enroll_status = check_if_student_is_enrolled(student_id,course_id)
    if enroll_status == True:
        update_status = update_course_availability(course_id,1)
        if update_status == 1:
            with open("enrollments.txt","r") as old_file_handler:
                temp_memory = old_file_handler.readlines()
                if len(temp_memory) < 2:
                    return "[-] There are no enrollment data"
                for line in range(1,len(temp_memory)):
                    details = temp_memory[line].split(",")
                    current_student_id = details[0]
                    current_course_id = details[1]
                    enrollment_status = details[3]
                    if current_course_id == course_id and current_student_id == student_id and enrollment_status.rstrip("\n") == "Active":
                        enrollment_status = "Dropped"
                        new_info = f"{current_student_id},{current_course_id},{datetime.date.today()},{enrollment_status}\n" 
                        temp_memory[line] = new_info 
                        with open("enrollments.txt","w") as new_file_handler:
                            new_file_handler.writelines(temp_memory)
                        return f"[+] Successfully Dropped Course {course_id}"
        elif update_status == -1:
            return "[-] Courses not found"
    else:
        return "[-] You are not currently Enrolled in this Course"

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
               ["[7]","Exit"]]
    title = "Course Registration System"
    display_menu(title,options)

    #define user_selection to be an empty string to ensure the while loop's condition is true
    user_selection = ""

    #The main while loop to keep the program running until the user chooses the exit option
    while user_selection != "7":
        #prompt user for selection, the number of options is dynamic, it changes depending on the size of the options nested list
        user_selection = input(f"Select an Option Between 1 - {len(options)}: ")
        match user_selection:
            case "1":
                print("Please Enter the information in the following order: StudentID,Name,Contact")
                add_new_student() 
            case "2":
                print("Please Enter the information in the following order:Course ID,Course name, Seats Available,Maximum Seats")
                add_new_course()
            case "3":
                course_id = input("Which Course would you like to enroll in? Enter the Course ID: \n")
                if len(course_id) > 20:
                    print("Invalid Course Id")
                    continue
                student_id = input("Enter your student ID: \n")
                if len(student_id) > 9:
                    print("Invalid Student Id")
                    continue
                enrollment_date = datetime.date.today()
                enrollment_status = enrol_in_course(student_id,course_id,enrollment_date)
                print(enrollment_status)
                continue
            case "4":
                course_id = input("Which Course would you like to drop? Enter the Course ID: \n")
                if len(course_id) > 20:
                    print("Invalid Course Id")
                    continue
                student_id = input("Enter your student ID: \n")
                if len(student_id) > 9:
                    print("Invalid Student Id")
                    continue
                enrollment_status = drop_course(student_id,course_id)
                print(enrollment_status)
                continue
            case "5":
                view_available_course()
            case "6":
                view_student_information()
            case "7"|"Exit":
                print("Exiting ...")
                break
            case _:
                print("Invalid Input!")

#Call main function to run the program
main()
