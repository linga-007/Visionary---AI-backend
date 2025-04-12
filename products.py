from serpapi import GoogleSearch
import json


def otherProducts(product , serp_api):
    
  params = {
    "engine": "google",
    "q": product,
    "location": "India",
    "hl": "en",
    "gl": "us",
    "google_domain": "google.com",
    "num": "10",
    "start": "10",
    "safe": "active",
    "api_key": serp_api
  }

  search = GoogleSearch(params)
  results = search.get_dict()
  organic_results = results["organic_results"][:1]
 

  # print(organic_results)

  # with open('products.json', 'w') as file:
  #   json.dump(organic_results, file, indent=4)

  return organic_results


