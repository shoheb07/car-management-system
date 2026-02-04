from car_manager import *

def menu():
    print("\n=== Car Management System ===")
    print("1. Add Car")
    print("2. View Cars")
    print("3. Search Car")
    print("4. Update Car")
    print("5. Delete Car")
    print("6. Exit")
    return input("Choose option: ")

while True:
    choice = menu()

    if choice == "1":
        add_car()
    elif choice == "2":
        view_cars()
    elif choice == "3":
        search_car()
    elif choice == "4":
        update_car()
    elif choice == "5":
        delete_car()
    elif choice == "6":
        break
    else:
        print("Invalid choice.")