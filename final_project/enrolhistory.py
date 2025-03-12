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