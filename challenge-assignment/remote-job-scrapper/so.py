import requests
from bs4 import BeautifulSoup

URL = "https://stackoverflow.com/jobs"

def get_search_page_url(word):
    return f"{URL}?r=true&q={word}"


def get_last_page(url):
    request = requests.get(url)
    soup = BeautifulSoup(request.text, "html.parser")
    pagination = soup.find("div", {"class": "s-pagination"})
    if pagination:
        pages = pagination.find_all("a")
        last_pages = pages[-2].get_text(strip=True)
    else:
        last_pages = 0
    return int(last_pages)


def extract_job(html):
    title = html.find("h2", {"class": "mb4"}).find("a")["title"]
    company, location = html.find("h3", {
        "class": "mb4"
    }).find_all(
        "span", recursive=False)
    company = company.get_text(strip=True)
    job_id = html["data-jobid"]
    return {
        'title': title,
        'company': company,
        "link": f"{URL}/{job_id}"
    }


def extract_jobs(last_page, url):
    jobs = []
    for page in range(last_page):
        print("Scrapping stackoverflow page:", {page})
        request = requests.get(f"{url}&PG={page+1}")
        soup = BeautifulSoup(request.text, "html.parser")
        jobs_list = soup.find_all("div", {"class": "-job"})
        for item in jobs_list:
            job = extract_job(item)
            jobs.append(job)
    return jobs


def so_get_jobs(word):
    url = get_search_page_url(word)
    last_page = get_last_page(url)
    jobs = extract_jobs(last_page, url)
    return jobs