# this is the app/drinks.py file...

import requests

def fetch_nonalcoholic_drinks():
    drinks_url = f'https://www.thecocktaildb.com/api/json/v1/1/filter.php?a=Non_Alcoholic'
    drinks_response = requests.get(drinks_url)
    drinks_parsed_response = drinks_response.json()
    drinks1 = drinks_parsed_response.get('drinks', [])
    return drinks1

if __name__ == "__main__":
    # FETCH THE DATA
    drinks = fetch_nonalcoholic_drinks()
    #print(drinks[0:3])
    #print(drinks[0].keys())