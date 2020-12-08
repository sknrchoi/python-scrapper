import csv

def save_to_file(jobs):
    file = open("jobs.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["title", "company", "location", "link"])
    for job in jobs:
        # convert dict_value to list
        # write row into csv file
        writer.writerow(list(job.values())) 
    return