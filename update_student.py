from input_validations import age_validation, course_validation, state_validation

def update(students):

    correct_id = 0

    while correct_id == 0:

        what_id = input("Enter id: ").strip()

        if not what_id:
            print("EMPTY ID! Please enter integers")
        else:
            try:
                what_id = int(what_id)
                if what_id < 0:
                    print("Please enter not negative ID")
                else:
                    correct_id = 1
            except ValueError:
                print("Please enter only integers!")

    for s in students:
            
            if s["id"] == what_id:

                change_age = input("\nDo you want to change age (y/n)?: ")
                if change_age.lower() in ["y", "yes"]:
                    
                    new_age = age_validation()

                    for s in students:
                        if s["id"] == what_id:
                            print(f"STUDENT UPDATE: {s['name']} | New age: {new_age}")
                            break

                change_course = input("\nDo you want to change course (y/n)?: ")
                if change_course.lower() in ["y", "yes"]:

                    new_course = course_validation()
                    
                    for s in students:
                        if s["id"] == what_id:
                            print(f"STUDENT UPDATE: {s['name']} | New course: {new_course}")
                            break

                change_state = input("\nDo you want to change state (y/n)?: ")
                if change_state.lower() in ["y", "yes"]:

                    new_state = state_validation()

                    for s in students:
                        if s["id"] == what_id:
                            print(f"STUDENT UPDATE: {s['name']} | New state: {new_state}")
                            break

                if change_age.lower() not in ["y", "yes"] and change_course.lower() not in ["y", "yes"] and change_state.lower() not in ["y", "yes"]:
                    print("\nSTUDENT WASNT'T MODIFIED!")
                
                break
    
    else:
            print("STUDENT DOESN'T EXIST!")