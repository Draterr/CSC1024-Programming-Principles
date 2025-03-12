import os 
import helper
import enrol
import deletecourse
import editcourse 
import enrolhistory
import drop 
import addcourses
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
            print(f"{file_name} not Found...")
            print("Creating files...")
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
               ["[8]","Edit a Course"],
               ["[9]","Delete a Course"],
               ["[10]","Exit"]]
    title = "Course Registration System"
    display_menu(title,options)

    #define user_selection to be an empty string to ensure the while loop's condition is true
    user_selection = ""

    #The main while loop to keep the program running until the user chooses the exit option
    while user_selection != "10":
        #prompt user for selection, the number of options is dynamic, it changes depending on the size of the options nested list
        display_menu(title,options)
        user_selection = input(f"Select an Option Between 1 - {len(options)}: ")
        if not user_selection.isdigit():
            print(f"Input must be between 1 - {len(options)}")
            continue
        match user_selection:
            case "1":
                print("Please Enter the information in the following order: StudentID,Name,Contact")
                add_new_student() 
            case "2":
                print("Please Enter the information in the following order:Course ID,Course name, Seats Available,Maximum Seats")
                addcourses.add_course()
                continue
            #If the user chooses to enroll in a course(Option  3)
            case "3":
                while True:
                    #Ask the user for the Course ID
                    course_id = input("Which Course would you like to enroll in? Enter the Course ID: \n")

                    #Ensure that the Course_ID is of a probable length
                    if len(course_id) > 20 or len(course_id) <= 0 or helper.course_id_exists(course_id,"courses.txt"): 
                        print("Invalid Course Id")
                        continue
                    else:
                        break
                while True:
                    #Ask the user for their studentID
                    student_id = input("Enter your student ID: \n")

                    #Ensure that the student_ID is of a probable length
                    if len(student_id) > 9 or len(student_id) <= 0:
                        print("Invalid Student Id")
                        continue
                    else:
                        break

                #Invoke the enrol_in_course function with the user input
                enrollment_status = enrol.enrol_in_course(student_id,course_id)
                
                #display the result
                print(enrollment_status)
                continue
            case "4":
                while True:
                    #Ask the user for the Course ID
                    course_id = input("Which Course would you like to drop? Enter the Course ID: \n")

                    #Ensure that the Course_ID is of a probable length
                    if len(course_id) > 20 or len(course_id) <= 0 or not helper.course_id_exists(course_id,"courses.txt"):
                        print("Invalid Course Id")
                        continue
                    else:
                        break

                #Ask the user for their studentID
                while True:
                    student_id = input("Enter your student ID: \n")
                    #Ensure that the student_id is of a probable length
                    if len(student_id) > 9 or len(course_id) <= 0:
                        print("Invalid Student Id")
                        continue
                    else:
                        break

                #Invoke the drop_course function with the user input
                enrollment_status = drop.drop_course(student_id,course_id)

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
                while True:
                    if len(student_id) > 9 or len(student_id) <= 0:
                        print("Invalid Student Id")
                        continue
                    else:
                        break
                histories = enrolhistory.view_enrollment_history(student_id)
                print(histories)
                continue
            #Exits If the user chooses option 7 or type "Exit"
            case "8":
                editcourse.edit_course()
                continue
            case "9":
                deletecourse.delete_course()
                continue
            case "10"|"Exit":
                print("Exiting ...")
                break
            #If the user enters anything that is not a valid option
            case _:
                print("Invalid Selection!")
                continue

#Call main function to run the program
main()
