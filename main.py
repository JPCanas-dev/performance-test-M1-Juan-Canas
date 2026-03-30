from interactive_menu import menu

students = [
    {"id" : int(1000), "name" : "Juan", "age" : int(28), "course" : "Math", "state" : "active"}
]

if __name__ == "__main__":


    print()
    print("=" * 40)
    print("WELCOME TO J-STUDENT REGISTRITATION SYSTEM").center(40)
    print("=" * 40)
    end_message = menu(students)
    print(end_message)