import csv

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


def add_application(new_application):
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
