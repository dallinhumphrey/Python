import requests
from bs4 import BeautifulSoup


URL = 'http://www.dailysmarty.com/topics/python'
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")

python_titles = results.find_all("h2", string=lambda t: "python" in t.lower())
for p_titles in python_titles:
    link = p_titles.find("a")["href"]
    print(p_titles.text.strip())
    print(f"Learn here: {link}/n")

title_elems = results.find_all("section", class_="card-content")
for title_elem in title_elems:
    title_elem = title_elem.find("h2", class_="title")
    if None in (title_elem):
        continue
    print(title_elem.text.strip())
