from bs4 import BeautifulSoup
import requests
from urllib2 import urlopen
import codecs

class WebScrapper(object):

    BASE_URL = "http://www.espnfc.us/barclays-premier-league/23/"
    '''scores?date=20150816'''
    
    def __init__(self):
        pass

    def get_data_links(self, section_url):
        html = urlopen(section_url).read()
        soup = BeautifulSoup(html, "lxml")
        boccat = soup.find("dl", "boccat")
        category_links = [BASE_URL + dd.a["href"] for dd in boccat.findAll("dd")]
        print category_links
        return category_links

    def get_page(self, section_url):
        num = 0
        League_Score = {}
        WriteToFile = WebScrapper()
        page = urlopen(section_url)
        soup = BeautifulSoup(page.read())
        league_name = soup.find_all("div", {"class": "score-league"})
        All_Teams = soup.find_all("div", {"class": "score-group" "score-group first"})
        for league in league_name:
            print(league.h4.get_text())
            teams = league.find_all("div", {"class": "score-group" "score-group first"})
            for team in teams.findAll('span'):
                print team.get_text()
            '''WriteToFile.write_to_file(league.h4.get_text())'''

    def write_to_file(self, data):
        f = codecs.open('Soccer_Scores.txt', 'a', 'utf-8')
        f.write(data + "\n")
        f.close()

if __name__ == "__main__":
    Scrappy = WebScrapper()
    BASE_URL = "http://www.espnfc.us/scores?date=20150815"
    Scrappy.get_page(BASE_URL)
    '''url = raw_input("Enter a website to exctract the URL's from: ")
    r = requests.get("http://" + BASE_URL)
    data = r.text
    soup = BeautifulSoup(data)
    for link in soup.find_all('a'):
        print(link.get('href'))'''
    


