from bs4 import BeautifulSoup
import requests
from datetime import date
class LiveScoreCricket():

	def __init__(self) -> None:
		
		self.url = "https://www.scorespro.com/cricket/"
		self.session = requests.Session()

		self.my_headers = {'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/71.0.3578.98 Safari/537.36", 
		'Accept':"text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,image/apng,*/*;q=0.8"}

		self.response = self.session.get(self.url, headers=self.my_headers)

		self.html_soup = BeautifulSoup(self.response.text, 'html.parser')

	def fetchScore(self,):
		returnDict = dict()
		# today = date.today().strftime("%d_%m_%Y")
		today = 'data'
		returnDict[today] = []

		requested_data_first_team = self.html_soup.find_all('td', attrs={'class': "cri_hometeam"})
		requested_data_second_team = self.html_soup.find_all('td', attrs={'class': "cri_awayteam"})
		for i in range(len(requested_data_first_team)):	
			teamName1 = " ".join(requested_data_first_team[i].text.strip().split()[:2])
			teamName2 = " ".join(requested_data_second_team[i].text.strip().split()[:2])
			score_team1 = requested_data_first_team[i].find_all_next('td', attrs={'class': "cri_set cur-ptr", 'title': 'Match Details'})[:2]
			score_team2 = requested_data_second_team[i].find_all_next('td', attrs={'class': "cri_set cur-ptr", 'title': 'Match Details'})[:2]
			lst1 = [teamName1]
			lst2 = [teamName2]
			for j in range(len(score_team1)):
				lst1.append(score_team1[j].text.strip())
				lst2.append(score_team2[j].text.strip())
			returnDict[today].append(lst1)
			returnDict[today].append(lst2)
		
		return returnDict

# LiveScoreCricket().fetchScore()

