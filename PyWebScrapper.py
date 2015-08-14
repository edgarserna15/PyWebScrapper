from bs4 import BeautifulSoup
import request
from urllib2 import urlopen

class WebScrapper(object):

    BASE_URL = ""
    
    def __init__(self):
        print "hello"

    def get_data_links(self, section_url):
        html = urlopen(section_url).read()
        soup = BeautifulSoup(html, "lxml")
        boccat = soup.find("dl", "boccat")
        category_links = [BASE_URL + dd.a["href"] for dd in boccat.findAll("dd")]
        print category_links
        return category_links


if __name__ == "__main__":
    Scrappy = WebScrapper()
    url = raw_input("Enter a website to exctract the URL's from: ")
    r = requests.get("http://" + url)
    data = r.text
    soup = BeautifulSoup(data)
    for link in soup.find_all('a'):
        print(link.get('href'))
    


