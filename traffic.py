import requests
import json
def fetchTraffic(link):
	# print(link)
	url = "https://similarweb-traffic.p.rapidapi.com/traffic"
	

	querystring = {"domain":link}

	headers = {
		"x-rapidapi-key": "d9e6579aaemshd344c5afdabba18p1808eajsn98067dbcde22",
		"x-rapidapi-host": "similarweb-traffic.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)

	return response.json()

