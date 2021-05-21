from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

link = 'https://www.psychologytoday.com/us/therapists?search='

req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
page = urlopen(req)
page_soup = BeautifulSoup(page.read(), "html.parser")
page.close()

divs = page_soup.findAll('div', attrs={'class':'result-row normal-result row'})
for i in divs:
    print(i['data-prof-name'])
    
# data-result-url