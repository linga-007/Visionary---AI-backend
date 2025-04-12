import requests
import os
import json

API_KEY = "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"

url = "https://api.groq.com/openai/v1/chat/completions"

def analyze_business(product, traffic):
    prompt = f"""
    You are a highly skilled business analyst AI with expertise in competitive market analysis. 
    Your task is to assess whether the product '{product}' can sustain itself in the market against competitors based on their traffic data.

    **Instructions:**
    - Conduct a **deep traffic analysis** of competitor websites. Identify key trends, user engagement, bounce rates, and traffic sources.
    - Evaluate whether these competitors dominate the market and how difficult it is for '{product}' to compete.
    - Provide a clear and data-backed verdict: **Can '{product}' sustain itself in this competitive landscape?**
    - If the outlook is unfavorable, suggest **actionable strategies** to improve market positioning, including marketing, SEO, partnerships, or product enhancements.

    **Traffic Data for Analysis:**  
    {traffic}

    Be precise, data-driven, and provide a well-structured response.
    Give the Response approx 300 - 400 words

    Also Give a one line answer whether my product sustains or not

    Give Each subheading as a key value pair

    """

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-70b-8192", 
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        # print("res is ",response)
        return response.json()["choices"][0]["message"]["content"]
    else:
        return {"error": response.json()}


