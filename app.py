from tracker import find_application_by_id
from tracker import load_applications
from tracker import add_application
from tracker import update_application_status
from tracker import search_applications
from tracker import update_application_field
from menu import get_field_selection
from menu import display_applications
from menu import get_application_input
from menu import display_application_details



def main():
    while True:
        print("=" * 40)
        print("      Job Tracker")
        print("=" * 40)
        print("1. View Applications")
        print("2. Add Application")
        print("3. Update Status")
        print("4. View Application Details")
        print("5. Search Applications")
        print("6. Edit Application")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            applications = load_applications()
            display_applications(applications)

        elif choice == "2":
            new_application = get_application_input()
            add_application(new_application)
            print("Application added successfully!")

        elif choice == "3":
            application_id = input("Enter Application ID: ").strip().upper()
            new_status = input("Enter new status: ").strip()

            old_status = update_application_status(application_id, new_status)

            if old_status is not None:
                print(f"Status updated: {old_status} -> {new_status}")
            else:
                print("Application not found.")

        elif choice == "4":
            application_id = input("Enter Application ID: ").strip().upper()
            application = find_application_by_id(application_id)

            if application is None:
                print("Application not found.")
                continue

            display_application_details(application)

        elif choice == "5":
            search_term = input("Enter company name: ").strip()
            matches = search_applications(search_term)

            if matches:
                display_applications(matches)
            else:
                print("No matching applications found.")

        elif choice == "6":
            application_id = input("Enter Application ID: ").strip().upper()
            application = find_application_by_id(application_id)

            if application is None:
                print("Application not found.")
                continue

            field_name = get_field_selection()

            if field_name is not None:
                new_value = input(f"Enter new value for {field_name}: ").strip()

                updated = update_application_field(
                    application_id,
                    field_name,
                    new_value
                )

                if updated:
                    print("Application updated successfully!")

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("That option is not ready yet.")


if __name__ == "__main__":
    main()