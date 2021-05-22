from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from therapist_model import Therapist

link = 'https://www.psychologytoday.com/us/therapists?search=11366'

def scrape_therapists(url):
    # scraping all the therapists from website
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req)
    page_soup = BeautifulSoup(page.read(), "html.parser")
    page.close()

    # scraping all links to therapist's personal page
    therapist_links = []
    therapists = []
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

        # getting the name
        name = page_soup.find('h1', attrs={'itemprop':'name'}).text

        # getting the phone number
        phone = page_soup.find('a', attrs={'id':'phone-click-reveal'}).text

        # getting the address
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
        address += street.text.strip() + " " + locality.text.strip() + " " + region.text.strip() + " " + postal_code.text.strip()
        
        final_therapist = Therapist(name.strip(), phone.strip(), address, urls)
        therapists.append(final_therapist)
    return therapists

