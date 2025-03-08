import os 

"""
This Program is a Course Registration System

It creates data_
"""
def initial_data_preparation(files):
    """
    Creates Initial Files.

    Create the students record file, courses file and enrollment files and initialize them with csv format headers.
    """

    #iterate over a nested list called files to create each file, if we wanted to create a new file we just need to append a new list to the files list
    for file_list in files:
        file_name = file_list[0]
        file_header = file_list[1]
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
        #Left-Just option_number by 5 to keep alignment consistent incase we get to double digit option numbers.
        #Ex: [10]\t = 5 characters
        print(f"{option[0]:<5} {option[1]}")

    #more "=" to contain the output
    print("="*50)


def add_new_student():
    return

def add_new_course():
    return

def enrol_in_course():
    return

def drop_course():
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
             ["courses.txt","Course ID,Course name, Seats Available\n"],
             ["enrollments.txt","Student ID,Course ID,Enrollment date\n"]]
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
                add_new_student() 
            case "2":
                add_new_course()
            case "3":
                enrol_in_course()
            case "4":
                drop_course()
            case "5":
                view_available_course()
            case "6":
                view_student_information()
            case "7":
                print("Exiting ...")
                break

#Call main function to run the program
main()
