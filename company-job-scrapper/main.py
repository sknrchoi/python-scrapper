import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")
alba_url = "http://www.alba.co.kr"


def extract_job(html):
    job = {}
    local = html.find("td", {"class": "local"})
    if local:
        local = local.text.replace(u'\xa0', u' ')
    else:
        return job
    company = html.find("td", {
        "class": "title"
    }).find("span", {
        "class": "company"
    }).string
    time = html.find("td", {"class": "data"}).string
    pay = html.find("td", {"class": "pay"})
    pay = pay.find("span", {
        "class": "payIcon"
    }).string + " " + pay.find("span", {
        "class": "number"
    }).string
    regist_date = html.find("td", {"class": "regDate"}).string
    job = {
        "local": local,
        "company": company,
        "time": time,
        "pay": pay,
        "regist": regist_date
    }
    return job


# find jobs
def extract_jobs(link):
    jobs = []
    link = f"{link}?pagesize=1000"
    request_company = requests.get(link)
    soup_company = BeautifulSoup(request_company.text, "html.parser")
    table = soup_company.find("div", {"id": "NormalInfo"}).find("table")
    jobs_html = table.find("tbody").select("tr:not(.summaryView)")

    for job in jobs_html:
        job = extract_job(job)
        jobs.append(job)
    return jobs


def save_cvs_file(name, jobs):
    # create cvs file
    file = open(f"{name}.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["place", "title", "time", "pay", "date"])
    for job in jobs:
        writer.writerow(list(job.values()))


def main():
    request = requests.get(alba_url)
    soup = BeautifulSoup(request.text, "html.parser")
    container = soup.find("div", {"id": "MainSuperBrand"})
    companies = container.find_all("li", {"class": "impact"})
    for company in companies:
        a = company.find("a", {"class": "goodsBox-info"})
        name = a.find("span", {"class": "company"}).string
        if "/" in name:
            name = name.replace("/", "_")
        link = a['href']
        if "job/brand" in link:
            link = link
        else:
            link = f"{a['href']}job/brand/"
        
        print(f"Scapping '{name}' jobs")
        jobs = extract_jobs(link)
        save_cvs_file(name, jobs)


main()
