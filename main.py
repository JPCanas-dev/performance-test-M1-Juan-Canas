from interactive_menu import menu

students = [
    {"id" : int(1000), "name" : "Juan", "age" : int(28), "course" : "Math", "state" : "active"},
    {"id" : int(2000), "name" : "Jose", "age" : int(20), "course" : "Biology", "state" : "inactive"}
]

if __name__ == "__main__":
    print()
    print("=" * 46)
    print("WELCOME TO J-STUDENT REGISTRITATION SYSTEM".center(46))
    print("=" * 46)
    end_message = menu(students)
    print(end_message)