from bs4 import BeautifulSoup
import requests

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
		requested_data = self.html_soup.find_all('td', attrs={'class': "cri_hometeam"})
		for i in requested_data:	
			teamName = " ".join(i.text.strip().split()[:2])
			returnDict[teamName] = list()
			i = i.find_all_next('td', attrs={'class': "cri_set cur-ptr", 'title': 'Match Details'})[:2]
			for j in i:
				returnDict[teamName].append(j.text.strip())
		
		requested_data = self.html_soup.find_all('td', attrs={'class': "cri_awayteam"})
		for i in requested_data:	
			teamName = " ".join(i.text.strip().split()[:2])
			returnDict[teamName] = list()
			i = i.find_all_next('td', attrs={'class': "cri_set cur-ptr", 'title': 'Match Details'})[:2]
			for j in i:
				returnDict[teamName].append(j.text.strip())

		return returnDict

LiveScoreCricket().fetchScore()

