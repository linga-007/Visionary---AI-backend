from flask import Flask , request, jsonify
from flask_cors import CORS 
from products import otherProducts
from fetchLink import extract_links
from traffic import fetchTraffic
from graph import plotGraph

from summarise import analyze_business

from dotenv import load_dotenv
import os

app = Flask(__name__)
CORS(app) 

load_dotenv()



api_key = os.getenv("API_KEY")
serp_api = os.getenv("SERP_API")

print(api_key)


@app.route('/')
def hello():
    return "Hello"

@app.route('/otherProducts' , methods = ["POST"])
def otherProduct():
    obj = request.get_json()
    product  = obj['product']
    # print("product is " , product)/
    other_products = otherProducts(product , serp_api)
    # print(other_products)
    links = extract_links(other_products)

    return jsonify({"data" : other_products , "links" : links })


@app.route('/traffic' , methods = ['POST'])
def getData():
    obj = request.get_json()    
    links  = obj['data']
    

    Engagements = []
    MonthlyVisits = []
    TrafficSources = []
    
    print("links is" , links)
    for i in links:
        print(i)
        traffics = fetchTraffic(i)
        print(traffics)
        Engagements.append(traffics["Engagments"])
        MonthlyVisits.append(traffics["EstimatedMonthlyVisits"])
        TrafficSources.append(traffics["TrafficSources"])
    
    # summarised_content = analyze_business("PDF Summariser" , Engagements , MonthlyVisits, traffics)

    return jsonify({"data" : [Engagements , MonthlyVisits , TrafficSources]})

@app.route('/summarise', methods = {"POST"})
def summariseTraffic():
    obj = request.get_json()
    traffic = obj["data"]
    # print(traffic)

    summarised_content = analyze_business("PDF Summariser" , traffic)

    return jsonify({"data" : summarised_content})


if(__name__ == "__main__"):
    app.run(debug = True)
