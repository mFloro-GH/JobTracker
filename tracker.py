import csv
from datetime import date

CSV_FIELDS = [
    "ApplicationID",
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
    "CurrentStatus",
    "CurrentStage",
    "InterviewCount",
    "NextInterviewDate",
    "NextInterviewType",
    "LastContactDate",
    "FollowUpDue",
    "ResumeVersion",
    "CoverLetter",
    "Referral",
    "LinkedInApplied",
    "WorkdayApplied",
    "Notes"
]

def load_applications():
    applications = []

    with open("data/applications.csv", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            applications.append(row)

    return applications

def get_todays_date():
    today = date.today().isoformat()
    return today

def add_application(new_application):
    new_application["ApplicationID"] = generate_application_id()
    new_application["DateApplied"] = get_todays_date()
    new_application["CurrentStatus"] = "Applied"
    new_application["InterviewCount"] = 0
    new_application["CurrentStage"] = "Application Submitted"
    applications = load_applications()
    applications.append(new_application)
    save_applications(applications)


def save_applications(applications):

    with open("data/applications.csv", "w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=CSV_FIELDS
        )

        writer.writeheader()

        for application in applications:
            writer.writerow(application)

def generate_application_id():
    applications = load_applications()

    highest_id = 0

    for application in applications:
        application_id = application["ApplicationID"]

        if application_id:
            current_id = int(application_id[4:])

            if current_id > highest_id:
                highest_id = current_id

    next_id = highest_id + 1

    return f"APP-{next_id:04}"