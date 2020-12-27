import csv

def save_to_cvs(jobs):
    file = open("jobs.csv", mode="w") # mode must be in lower case
    writer = csv.writer(file)
    writer.writerow(["Title", "Company", "Link"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return