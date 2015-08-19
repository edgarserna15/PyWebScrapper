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
        count = 1
        TeamsList = []
        Goals = []
        GameNum = []
        League_Score = {}
        WriteToFile = WebScrapper()
        page = urlopen(section_url)
        soup = BeautifulSoup(page.read(), 'html.parser')
        league_name = soup.find_all("div", {"class": "score-league"})
        for league in league_name:
            print(league.h4.get_text())
            WriteToFile.write_to_file(league.h4.get_text(), "League")
            GameContent = league.find_all("div", {"class": "score-content"})
            '''league.find_all("div", {"class": "team-name"})'''
            for content in GameContent:
                Teams = content.find_all("div", {"class": "team-name"})
                Scores = content.find_all("div", {"class": "team-score"})
                Time = content.find_all("div", {"class": "game-info"})
                for team in Teams:
                    team_name = team.span.get_text()
                    TeamsList.append(team_name.encode('utf8'))
                for score in Scores:
                    goals = score.find("span")
                    string_goals = str(goals)
                    if count > 2:
                        pass
                    else:
                        amt = string_goals.replace("<span>", "").replace("</span>", "")
                        Goals.append(amt)
                    count = count + 1
                for time in Time:
                    game_time = time.span.get_text()
                print "Team 1: " + TeamsList[0] + " Score: " + Goals[0]
                print "Team 2: " + TeamsList[1] + " Score: " + Goals[1]
                print "Time  : " + game_time.encode('utf8') + "\n"
                del TeamsList[:]
                del Scores[:]
                count = 1
                
                '''WriteToFile.write_to_file(teams.span.get_text(), "Teams")'''
            
            '''teams = league.find_all("div", {"class": "score-group" "score-group first"})
            for team in teams.findAll('span'):
                print team.get_text()'''
            '''WriteToFile.write_to_file(league.h4.get_text())'''

    def write_to_file(self, data, League):
        f = codecs.open('Soccer_Scores.txt', 'a', 'utf-8')
        f.write(data)
        f.close()
        f = open('Soccer_Scores.txt', 'a')
        f.write("\n")
        f.close()

if __name__ == "__main__":
    Scrappy = WebScrapper()
    BASE_URL = "http://www.espnfc.us/scores?date=20150819"
    Scrappy.get_page(BASE_URL)
    '''url = raw_input("Enter a website to exctract the URL's from: ")
    r = requests.get("http://" + BASE_URL)
    data = r.text
    soup = BeautifulSoup(data)
    for link in soup.find_all('a'):
        print(link.get('href'))'''
    


