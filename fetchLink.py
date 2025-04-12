import json

def extract_links(data, filtered_links=None):
    if filtered_links is None:
        filtered_links = []

    if isinstance(data, dict):
        for key, value in data.items():
            if key == "link" and isinstance(value, str):
                if not (value.startswith("https://www.reddit.com") or 
                        "google.com/search" in value or 
                        "play.google.com" in value or 
                        "apps.apple.com" in value):  
                    filtered_links.append(value)
            else:
                extract_links(value, filtered_links)

    elif isinstance(data, list):
        for item in data:
            extract_links(item, filtered_links)

    return filtered_links
