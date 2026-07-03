from tracker import load_applications


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

            for application in applications:
                print(application)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("That option is not ready yet.")


if __name__ == "__main__":
    main()