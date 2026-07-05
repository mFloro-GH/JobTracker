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