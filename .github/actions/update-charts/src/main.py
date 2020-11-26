import os
import requests
import csv
from matplotlib import pyplot as plt
from collections import defaultdict

states = defaultdict(int)
top10states = defaultdict(int)

def store_data():
    with open("data.csv", "r") as f:
        csv_reader = csv.DictReader(f)
        for line in csv_reader:
            if(line['State'] != 'Total'):
                states[line['State']] = {
                    'Confirmed': int(line['Confirmed']),
                    'Recovered': int(line['Recovered']),
                    'Deaths': int(line['Deaths'])
                }

def top10():
    confirmed = sorted([states[x]['Confirmed'] 
                        for x in states], reverse=True)[0:10]
    
    for cases in confirmed:
        for state in states:
            if(states[state]['Confirmed'] == cases):
                top10states[state] = {
                    'Confirmed': states[state]['Confirmed'],
                    'Recovered': states[state]['Recovered'],
                    'Deaths': states[state]['Deaths']
                }
def analyze():
    store_data()
    top10()
    ran = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45]
    plt.style.use('fivethirtyeight')
    plt.title('Top 10 States With Active COVID-19 Cases')

    plt.barh(
        [x-1.5 for x in ran], 
        [d['Confirmed'] for d in top10states.values()],
        1.5, 
        color='darkorange'
    )

    plt.barh(
        ran,
        [d['Recovered'] for d in top10states.values()],
        1.5,
        color='steelblue'
    )

    plt.barh(
        [x+1.5 for x in ran], 
        [d['Deaths'] for d in top10states.values()], 
        1.5, 
        color='crimson'
    )

    plt.yticks(ticks=ran, labels=top10states.keys())
    plt.xlabel('Count')
    plt.ylabel('States')
    plt.legend(labels=['Confirmed', 'Recovered', 'Deaths'])
    plt.tight_layout()
    plt.savefig('barhfig_covid.png')
    #plt.show()


endpoint = "https://api.covid19india.org/csv/latest/state_wise.csv"


def get_data():
    return(requests.get(endpoint).content)

def write_data():
    with open("data.csv", "wb") as f:
        f.write(get_data())

write_data()
analyze()

# Set the data-output of the action as the value of get_data response
print(f"::set-output name=data::get_data()")
