from manager import StudentManager


def main():
    manager = StudentManager()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. List Students")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.update_student()
        elif choice == "3":
            manager.delete_student()
        elif choice == "4":
            manager.list_students()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
