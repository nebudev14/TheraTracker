from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

link = 'https://www.psychologytoday.com/us/therapists?search=11366'

def scrape_locations(url):
    # scraping all the therapists from website
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req)
    page_soup = BeautifulSoup(page.read(), "html.parser")
    page.close()

    # scraping all links to therapist's personal page
    therapist_links = []
    therapist_locations = []
    therapist_home_page = page_soup.findAll('div', attrs={'class':'result-row normal-result row'})
    for therapist in therapist_home_page:
        therapist_links.append(therapist['data-result-url'])
    num = 0
    # grabbing the office location from each therapist using personal page
    for urls in therapist_links:
        address = ""
        if num > 3:
            break
        req = Request(urls, headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(req)
        page_soup = BeautifulSoup(page.read(), "html.parser")
        page.close()
        try:
            street = page_soup.find('span', attrs={'itemprop':'streetAddress'})
        except:
            street = page_soup.find('div', attrs={'class':'location-address-phone'})
        if street is None: 
            continue
        locality = page_soup.find('span', attrs={'itemprop':'addressLocality'})
        region = page_soup.find('span', attrs={'itemprop':'addressRegion'})
        postal_code = page_soup.find('span', attrs={'itemprop':'postalcode'})
        num +=1    
        address += street.text.strip() + " " + locality.text.strip() + ", " + region.text.strip() + " " + postal_code.text.strip()
        therapist_locations.append(address)
    return therapist_locations
