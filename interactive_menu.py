
def menu(students):

    end_menu = 0

    while end_menu == 0:

        print("\n1. Register student")
        print("2. Display student list")
        print("3. Search student")
        print("4. Update student")
        print("5. Delete student")
        print("6. Exit")

        option = input("\nPlease select an option: ")
        print()

        if option == "1":
            


        elif option == "2":
            # Check if inventory is empty before displaying
            if not inventory:
                print("INVENTORY IS EMPTY!")
            else:
                # Call function to show all products
                show_inventory(inventory)

        elif option == "3":
            # Check if inventory is empty before calculating statistics
            if not inventory:
                print("INVENTORY IS EMPTY!")
            else:
                # Call function to calculate totals
                total_revenue, total_product = statistics(inventory)

                # Display formatted results
                print(f"Total revenue: $ {total_revenue:,}")
                print(f"Total registered products: {total_product}")

        elif option == "4":
            # Change control variable to exit the loop
            end_menu = 1

        else:
            # Print invalid input
            print("PLEASE ENTER A VALID VALUE!")

    # Return exit message after leaving the loop
    return "THANKS FOR USING MY SERVICES!\n"