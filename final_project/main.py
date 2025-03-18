import view_available_courses
import add_new_student
import display_student_list
import helper
import enrol
import deletecourse
import editcourse 
import drop 
import addcourses

"""

Course Registration System

This program allows students to:
- Enroll in courses
- Drop courses
- View available courses
- Delete courses
- Edit courses
- Add new students to the system
- Add new course to the system
- View Student Information

The system maintains records of students, courses, and enrollments.

"""

def main():
    """

    A main function to encapsulate the whole program into one function.

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

        #this checks if an enrollment record has been removed without using the system and updates the available seats accordingly
        update_seats = helper.update_course_available_seats()
        if update_seats:
            print("[+] available seats has been changed. It has been updated")
        #prompt user for selection, the number of options is dynamic, it changes depending on the size of the options nested list
        user_selection = input(f"\nSelect an Option Between 1 - {len(options)} or type help to display the menu: ")

        #check if the user entered a word
        if not user_selection.isdigit():
            user_selection = user_selection.lower()
        #based on the option the user chooses we invoke diffrent functions
        match user_selection:
            case "1":
                add_new_student.register_student()
                continue
            case "2":
                addcourses.add_course()
                continue
            case "3":
                enrol.enrol_in_course()
                continue
            case "4":
                drop.drop_course()
                continue
            case "5":
                view_available_courses.view_available_courses()
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
            case "9"|"exit":
                print("Exiting ...")
                break
            case "help":
                helper.display_menu(title,options)
                continue 
            case _:
                #If the user enters anything that is not a valid option
                print("Invalid Selection!")
                continue

#Call main function to run the program
main()
