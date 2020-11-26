import os
import requests

endpoint = "https://api.covid19india.org/csv/latest/state_wise.csv"


def get_data():
    return(requests.get(endpoint).content)

def write_data():
    with open("data.csv", "wb") as f:
        f.write(get_data())

write_data()

# Set the data-output of the action as the value of get_data response
print(f"::set-output name=data::get_data()")
