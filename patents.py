from serpapi import GoogleSearch
import json
from main import serp_api

params = {
  "engine": "google_patents",
  "q": "(Coffee)",
  "api_key": serp_api
}

search = GoogleSearch(params)
results = search.get_dict()
organic_results = results["organic_results"]

with open('patents.json', 'w') as file:
    json.dump(organic_results, file, indent=4)