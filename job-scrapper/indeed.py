import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, 'html.parser')
  pagination = soup.find("div", {"class":"pagination"})

  #list
  links = pagination.find_all('a')
  pages = []
  # except the last one
  for link in links[:-1]:
    pages.append(int(link.string))

  # first item from the end
  #print(pages[-1])

  # get maximum number
  max_page = pages[-1]
  return max_page

def extract_indeed_jobs(last_page):
  jobs = []
  for page in range(last_page):
    result = requests.get(f"{URL}&start={page*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class":"jobsearch-SerpJobCard"})
  
  for result in results:
    title = result.find("h2", {"class":"title"}).find("a")["title"]
  return jobs