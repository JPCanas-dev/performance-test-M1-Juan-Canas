from input_validations import id_validation, name_validation, age_validation
from input_validations import course_validation, state_validation


def new_student(students):

    id = id_validation(students)
    name = name_validation(students)
    age = age_validation()
    course = course_validation()
    state = state_validation()

    student_added = {
        "id" : id,
        "name" : name,
        "age" : age,
        "course" : course,
        "state" : state
    }

    students.append(student_added)

    return"\nSTUDENT REGISTERED SUCCESSFULLY!"






