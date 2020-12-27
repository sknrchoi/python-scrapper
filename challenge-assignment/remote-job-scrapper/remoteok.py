import requests
from bs4 import BeautifulSoup

URL = "https://remoteok.io"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

def get_search_page_url(word):
    return f"{URL}/remote-dev+{word}-jobs"


def extract_job(html):
    title = html.find("h2", {"itemprop": "title"}).string
    company = html.find("h3", {"itemprop":"name"}).string
    link = html.find("a", {"class":"preventLink"})["href"]
    return {
        'title': title,
        'company': company,
        "link": f"{URL}{link}"
    }


def extract_jobs(url):
    jobs = []
    request = requests.get(url, headers=headers)
    soup = BeautifulSoup(request.text, "html.parser")
    table = soup.find("table", {"id":"jobsboard"})
    if table:
        job_list = table.find_all("tr", {"class":"job"})
        for idx, item in enumerate(job_list):
            print("Scrapping remoteok item:", {idx})
            job = extract_job(item)
            jobs.append(job)
    return jobs


def remoteok_get_jobs(word):
    url = get_search_page_url(word)
    jobs = extract_jobs(url)
    return jobs