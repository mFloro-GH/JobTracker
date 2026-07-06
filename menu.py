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