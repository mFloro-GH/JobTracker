EDITABLE_FIELDS = [
    "Company",
    "Position",
    "Location",
    "RemoteType",
    "DateApplied",
    "Source",
    "Recruiter",
    "RecruiterEmail",
    "HiringManager",
    "SalaryMin",
    "SalaryMax",
    "SalaryExpectation",
    "Notes"
]

def display_applications(applications):

    print("=" * 70)
    print("ID | Company | CurrentStatus")
    print("=" * 70)

    for application in applications:
        print(
            f'{application["ApplicationID"]} | '
            f'{application["Company"]} | '
            f'{application["CurrentStatus"]}'
        )

def get_application_input():
    company = input("Company: ")
    position = input("Position: ")
    location = input("Location: ")
    remote_type = input("Remote Type: ")
    source = input("Source: ")

    application = {
        "Company": company,
        "Position": position,
        "Location": location,
        "RemoteType": remote_type,
        "Source": source,
        "CurrentStatus": "Applied"
    }

    return application

def display_application_details(application):
    print("=" * 50)
    print("Application Details")
    print("=" * 50)

    for field, value in application.items():
        print(f"{field:<20}: {value}")

def display_editable_fields():
    for number, field in enumerate(EDITABLE_FIELDS, start=1):
        print(number, field)

def get_field_selection():
    display_editable_fields()

    try:
        selection = int(input("Select a field to edit: "))
    except ValueError:
        print("Please enter a number.")
        return None

    if selection < 1 or selection > len(EDITABLE_FIELDS):
        print(f"Please enter a number between 1 and {len(EDITABLE_FIELDS)}.")
        return None

    return EDITABLE_FIELDS[selection - 1]