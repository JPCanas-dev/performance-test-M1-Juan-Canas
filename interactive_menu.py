# Import functions from other modules
from register_student import new_student
from search_student import search
from update_student import update
from delete_student import delete

def menu(students):

    # Variable to control the menu loop
    end_menu = 0

    # Main loop: keeps showing the menu until user chooses to exit
    while end_menu == 0:

        # Display menu options
        print("\n1. Register student")
        print("2. Display student list")
        print("3. Search student")
        print("4. Update student")
        print("5. Delete student")
        print("6. Exit")

        option = input("\nPlease select an option: ")
        print()

        if option == "1":
            add_message = new_student(students)
            print(add_message)

        elif option == "2":
            if not students:
                print("STUDENTS LIST EMPTY!")
            else:
                for s in students:
                    print(f"ID: {s['id']}")
                    print(f"Name: {s['name']}")
                    print(f"Age: {s['age']}")
                    print(f"Course: {s['course']}")
                    print(f"State: {s['state']}\n")

        elif option == "3":
            if not students:
                print("STUDENTS LIST EMPTY!")
            else:
                search(students)

        elif option == "4":
            if not students:
                print("STUDENTS LIST EMPTY!")
            else:
                update(students)

        elif option == "5":
            if not students:
                print("STUDENTS LIST EMPTY!")
            else:
                delete(students)

        elif option == "6":
            # Change control variable to exit the loop
            end_menu = 1

        else:
            # Print invalid input
            print("PLEASE ENTER A VALID VALUE!")

    # Return exit message after leaving the loop
    return "THANKS FOR USING OUR SERVICES!\n"