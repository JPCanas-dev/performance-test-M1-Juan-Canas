
def id_validation(students):

    correct_id = 0

    while correct_id == 0:

        # Ask user for student id
        id = input("Enter id: ").strip()

        if not id:
            print("EMPTY ID! Please enter integers")
        else:
            try:
                id = int(id)
                if id < 0:
                    print("Please enter not negative ID")
                else:
                    for student in students:
                        if student["id"] == id:
                            print("ID ALREADY EXISTS! Please enter a new one")
                            break
                        else:
                            correct_id = 1
            except ValueError:
                print("Please enter only integers!")

    return id

def name_validation(students):

    correct_name = 0

    while correct_name == 0:

        # Ask user for student name
        name = input("Enter name: ").strip()

        if not name:
            print("EMPTY NAME! Please enter strings")
        elif name.replace(" ","").isalpha():
            for student in students:
                if student["name"].lower() == name.lower():
                    print("NAME ALREADY EXISTS! Please enter a new one")
                    break
            else:
                correct_name = 1
        else:
            print("Please enter only strings!")

    return name

def age_validation():

    correct_age = 0

    while correct_age == 0:

        # Ask user for student age
        age = input("Enter age: ").strip() 

        if not age:
            print("\nEMPTY AGE! Please enter a number")
        else:
            try:
                age = int(age)
                if age <= 6:
                    print("Age must be greater than 6!")
                else:
                    correct_age = 1
            except:
                print("\nPlease enter only integers!")

    return age

def course_validation():

    correct_course = 0

    while correct_course == 0:

        # Ask user for student course
        course = input("Enter course: ").strip()

        if not course:
            print("EMPTY COURSE! Please enter strings")
        elif course.replace(" ","").isalpha():
                correct_course = 1
        else:
            print("Please enter only strings!")

    return course

def state_validation():

    correct_state = 0

    # Ask user for student state
    while correct_state == 0:

        state = input("Enter state (active/inactive): ").strip()

        if not state:
            print("EMPTY STATE! Please enter strings")
        elif state.replace(" ","").isalpha():
                if not state.lower() in ["active","inactive"]:
                    print("Please enter only active/inactive")
                else:
                    correct_state = 1
        else:
            print("Please enter only strings!")

    return state