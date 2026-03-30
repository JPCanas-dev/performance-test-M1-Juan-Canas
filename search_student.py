from input_validations import id_validation

def search(students):

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
            print("\nFOUND STUDENT:")
            print(f"ID: {s['id']}")
            print(f"Name: {s['name']}")
            print(f"Age: {s['age']}")
            print(f"Course: {s['course']}")
            print(f"State: {s['state']}")
            break

    else:
        print("\nSTUDENT DOESN'T EXIST!")


        
        
