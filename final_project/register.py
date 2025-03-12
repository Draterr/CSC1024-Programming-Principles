import os 
import display_student_list
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
    helper.initial_data_preparation(files)


    #nested list for the option numbers and option text to allow for better text alignment
    #inner list consists of [{option_numbers},{option_text}]
    options = [["[1]","Add a Student"],
               ["[2]","Add a New Course"],
               ["[3]","Enrol in a Course"],
               ["[4]","Drop a Course"],
               ["[5]","View Available Courses"],
               ["[6]","View Student information"],
               ["[7]","Edit a Course"],
               ["[8]","Delete a Course"],
               ["[9]","Exit"]]
    title = "Course Registration System"
    helper.display_menu(title,options)

    #define user_selection to be an empty string to ensure the while loop's condition is true
    user_selection = ""

    #The main while loop to keep the program running until the user chooses the exit option
    while user_selection != "9":
        #prompt user for selection, the number of options is dynamic, it changes depending on the size of the options nested list
        user_selection = input(f"\nSelect an Option Between 1 - {len(options)} or type help to display the menu: ")
        match user_selection:
            case "1":
                print("Please Enter the information in the following order: StudentID,Name,Contact")
            case "2":
                print("Please Enter the information in the following order:Course ID,Course name, Seats Available,Maximum Seats")
                addcourses.add_course()
                continue
            #If the user chooses to enroll in a course(Option  3)
            case "3":
                #Invoke the enrol_in_course function with the user input
                enrollment_status = enrol.enrol_in_course()
                #display the result
                print(enrollment_status)
                continue
            case "4":
                #Invoke the drop_course function with the user input
                enrollment_status = drop.drop_course()

                #display the result
                print(enrollment_status)
                continue
            case "5":
                continue
            case "6":
                display_student_list.display_student()
                continue
            case "7":
                editcourse.edit_course()
                continue
            case "8":
                deletecourse.delete_course()
                continue
            case "9"|"Exit":
                print("Exiting ...")
                break
            case "help"|"HELP"|"Help":
                helper.display_menu(title,options)
            case _:
            #If the user enters anything that is not a valid option
                print("Invalid Selection!")
                continue

#Call main function to run the program
main()
