import requests
from bs4 import BeautifulSoup
# <h2>
# <a href="/job/python-nlp-intern-elloe">Python/NLP Intern at Elloe</a>
# </h2>
response = requests.get("https://www.myjobmag.co.ke/search/jobs?q=python+data+science")
htmldoc = response.content
#print(htmldoc)
soup = BeautifulSoup(htmldoc, 'html.parser')
h2_tags = soup.find_all('h2')
domain = "https://www.myjobmag.co.ke/"
#print(h2_tags)
for h2_tag in h2_tags:
    a_tag = h2_tag.a
    if a_tag is not None:
        title = a_tag.text
        url = a_tag["href"]
        name = domain + url
        #name = "https://www.myjobmag.co.ke/" + url
        print(title, name)

