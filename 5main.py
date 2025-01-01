import db_connection

def main():
    """
    Main function of the program. Provides user interaction with the program.
    """
    while True:
        print("\nChoose an action:")
        print("1. List all cats")
        print("2. Find a cat by name")
        print("3. Update a cat's age")
        print("4. Add a new feature to a cat")
        print("5. Delete a cat by name")
        print("6. Delete all cats")
        print("7. Find all cats older than a specific age")
        print("8. Find all cats with a specific feature")
        print("9. Sort cats by name")
        print("10. Exit")

        choice = input("Your choice: ")

        if choice == "1":
            # Get all cats from the database and print them
            cats = db_connection.get_all_cats()
            for cat in cats:
                print(cat)
        elif choice == "2":
            # Find a cat by its name
            name = input("Enter the cat's name: ")
            cat = db_connection.find_cat_by_name(name)
            if cat:
                print(cat)
            else:
                print("Cat not found")
        elif choice == "3":
            # Update a cat's age
            name = input("Enter the cat's name: ")
            new_age = int(input("Enter the new age: "))
            db_connection.update_cat_age(name, new_age)
            print("Cat's age updated successfully")
        elif choice == "4":
            # Add a new feature to a cat
            name = input("Enter the cat's name: ")
            new_feature = input("Enter the new feature: ")
            db_connection.add_feature_to_cat(name, new_feature)
            print("Feature added")
        elif choice == "5":
            # Delete a cat by name
            name = input("Enter the cat's name to delete: ")
            db_connection.delete_cat_by_name(name)
            print("Cat deleted")
        elif choice == "6":
            # Delete all cats
            confirm = input("Are you sure you want to delete all cats? (yes/no): ")
            if confirm.lower() == "yes":
                db_connection.delete_all_cats()
                print("All cats deleted")
            else:
                print("Operation canceled")
        elif choice == "7":
            # Find all cats older than a specific age
            age = int(input("Enter the age: "))
            cats = db_connection.find_cats_by_age(age)
            for cat in cats:
                print(cat)
        elif choice == "8":
            # Find all cats with a specific feature
            feature = input("Enter the feature: ")
            cats = db_connection.find_cats_by_feature(feature)
            for cat in cats:
                print(cat)
        elif choice == "9":
            # Sort cats by name
            cats = db_connection.sort_cats_by_name()
            for cat in cats:
                print(cat)
        elif choice == "10":
            # Exit the program
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
