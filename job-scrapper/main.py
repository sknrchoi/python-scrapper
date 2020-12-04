import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')

pagination = indeed_soup.find("div", {"class":"pagination"})

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

for n in range(max_page):
  print(f"start={n * 50}")
