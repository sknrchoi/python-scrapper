import requests
from bs4 import BeautifulSoup

URL = "https://weworkremotely.com"

def get_search_page_url(word):
    return f"{URL}/remote-jobs/search?term={word}"


def extract_job(html):
    title = html.find("span", {"class": "title"}).string
    company = html.find_all("span", {"class":"company"})[0].string
    link = html.find("a")["href"]
    return {
        'title': title,
        'company': company,
        "link": f"{URL}{link}"
    }


def extract_jobs(url):
    jobs = []
    request = requests.get(url)
    soup = BeautifulSoup(request.text, "html.parser")
    container = soup.find("section", {"class":"jobs"})
    if container:
        jobs_list = container.find_all("li", {"class": "feature"})
        jobs_list += container.find_all("li", {"class": ""})
        for idx, item in enumerate(jobs_list):
            print("Scrapping wework item:", {idx})
            job = extract_job(item)
            jobs.append(job)
    return jobs


def wework_get_jobs(word):
    url = get_search_page_url(word)
    jobs = extract_jobs(url)
    return jobs