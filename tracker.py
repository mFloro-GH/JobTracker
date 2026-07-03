import csv


def load_applications():
    applications = []

    with open("data/applications.csv", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            applications.append(row)

    return applications