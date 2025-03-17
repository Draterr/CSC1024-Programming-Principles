# File to store student data

FILE_NAME = "students.txt"

def display_student():
    try:
        # Open the file and read student data
        # "r" stands for read mode
        # .readlines() reads all lines from the file and stores them as a list of strings
        with open(FILE_NAME, "r") as file:
            students = file.readlines()

        # Check if the file is empty
        # print("-" * 50) separates sections in the output, making the lists easy to read
        if not students:
            print("\nNo students registered.")
        else:
            print("\nList of Registered Students:")
            print("-" * 75)
            print(f"{'ID':<15} {'Name':<30} {'Contact':<20}")
            print("-" * 75)

            # Loop through each student record and print details
            # .strip() removes trailing spaces including newline characters
            # .split(',') splits the line into a list of values using a comma
            for student in students:
                if not student.startswith("Student ID"):
                    student_data = student.strip().split(',')
                    if len(student_data) == 3:  # Check that student data has exactly four elements
                        student_id, name,  contact = student_data
                        print(f"{student_id:<15} {name:<30} {contact:<20}")
                    else:
                        print("Invalid student data")

            print("-" * 75)


    except FileNotFoundError:
        print(f"Error: The file '{FILE_NAME}' was not found")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


