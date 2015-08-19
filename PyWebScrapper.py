from bs4 import BeautifulSoup
import requests
from urllib2 import urlopen
import codecs

class WebScrapper(object):

    BASE_URL = "http://www.espnfc.us/scores"
    '''?date=20150816'''
    
    def __init__(self):
        pass

    def get_page(self, section_url):
        count = 1
        TeamsList = []
        Goals = []
        WriteToFile = WebScrapper()
        
        page = urlopen(section_url)
        soup = BeautifulSoup(page.read(), 'html.parser')
        league_name = soup.find_all("div", {"class": "score-league"})
        
        for league in league_name:
            WriteToFile.write_to_file(league.h4.get_text(), "", "", "")
            GameContent = league.find_all("div", {"class": "score-content"})
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
                Team1 =  "Team 1: " + TeamsList[0] + " Score: " + Goals[0]
                Team2 = "Team 2: " + TeamsList[1] + " Score: " + Goals[1]
                Time = "Time  : " + game_time.encode('utf8') + "\n"
                WriteToFile.write_to_file(None, Team1, Team2, Time)
                del TeamsList[:]
                del Goals[:]
                count = 1

    def write_to_file(self, League, Team1, Team2, time):
        
        if(League == None):
            f = open('Soccer_Scores.txt', 'a')
            f.write(Team1 + "\n" + Team2  + "\n" + time + "\n")
            f.write("\n")
            f.close()
        else:
            f = codecs.open('Soccer_Scores.txt', 'a', 'utf8')
            f.write("League: " + League)
            f.close()
            f = open('Soccer_Scores.txt', 'a')
            f.write("\n\n")
            f.close()


if __name__ == "__main__":
    Scrappy = WebScrapper()
    BASE_URL = "http://www.espnfc.us/scores?date=20150816"
    Scrappy.get_page(BASE_URL)

    


