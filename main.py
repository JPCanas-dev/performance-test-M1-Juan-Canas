# Import the menu function from another module
from interactive_menu import menu

# Create an initial list to store students
students = [
    {"id" : int(1000), "name" : "Juan", "age" : int(28), "course" : "Math", "state" : "active"},
    {"id" : int(2000), "name" : "Jose", "age" : int(20), "course" : "Biology", "state" : "inactive"}
]

# Check if this file is running here (not imported)
if __name__ == "__main__":
    print()
    print("=" * 46)
    print("WELCOME TO J-STUDENT REGISTRITATION SYSTEM".center(46))
    print("=" * 46)

     # Print a welcome message with a simple visual format
    end_message = menu(students)
    print(end_message)