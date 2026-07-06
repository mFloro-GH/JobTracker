from tracker import load_applications
from tracker import add_application
from tracker import save_applications
from menu import display_applications
from menu import get_application_input



def main():
    while True:
        print("=" * 40)
        print("      Job Tracker")
        print("=" * 40)
        print("1. View Applications")
        print("2. Add Application")
        print("3. Update Status")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            applications = load_applications()
            display_applications(applications)

        elif choice == "2":
            new_application = get_application_input()
            add_application(new_application)
            print("Application added successfully!")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("That option is not ready yet.")


if __name__ == "__main__":
    main()