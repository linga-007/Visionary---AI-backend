import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt

def plotGraph(product):
    data = TrendReq(hl='en-US', tz=360)
    data.build_payload(kw_list=[product])
    data = data.interest_over_time()

    # fig, ax = plt.subplots(figsize=(10,5))
    data[product].plot()
    plt.style.use('fivethirtyeight')
    plt.title(product, fontweight='bold')
    plt.xlabel('Year')
    plt.ylabel('Total Count')
    plt.savefig("graph.png")
