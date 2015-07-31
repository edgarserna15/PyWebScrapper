from bs4 import BeautifulSoup
from urllib2 import urlopen

class WebScrapper(object):

    BASE_URL = "http://www.chicagorader.com"
    
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
    Data = Scrappy.get_data_links("/chicago/best-of-chicago-2011-food-drink/BestOf?oid=4106228")
