
students = [
    {"id" : int(1000), "name" : "Juan", "age" : int(28), "course" : "Math", "state" : "active"}
]

def student_id(students):

    correct_id = 0

    while correct_id == 0:

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

    correct_name = 0

    while correct_name == 0:

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

        correct_age = 0

    while correct_age == 0:

        age = input("Enter age: ").strip() 

        if not age:
            print("\nEMPTY AGE! Please enter a number")
        else:
            try:
                age = int(age)
                if age <= 0:
                    print("Age must be greater than 0!")
                else:
                    correct_age = 1
            except:
                print("\nPlease enter only integers!")

    correct_course = 0

    while correct_course == 0:

        course = input("Enter course: ").strip()

        if not course:
            print("EMPTY COURSE! Please enter strings")
        elif course.replace(" ","").isalpha():
                correct_course = 1
        else:
            print("Please enter only strings!")

    correct_state = 0

    while correct_state == 0:

        state = input("Enter state (active/inactive): ").strip()

        if not state:
            print("EMPTY COURSE! Please enter strings")
        elif state.replace(" ","").isalpha():
                if not state.lower() in ["active","inactive"]:
                    print("Please enter only active/inactive")
                else:
                    correct_state = 1
        else:
            print("Please enter only strings!")

    

student_id(students)