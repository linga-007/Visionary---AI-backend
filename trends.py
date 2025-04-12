from serpapi import GoogleSearch
import json
from main import serp_api


def getTrends(product):
    params = {
      "engine": "google_trends_autocomplete",
      "q": product,
      "api_key": serp_api
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    suggestions = results["suggestions"]
    print(suggestions)
    return suggestions

# getTrends("job finder")

