# this is the app/unemployment_report.py file...

# LOCAL DEV (ENV VARS)


from statistics import mean


import requests
from plotly.express import line


from app.alpha import API_KEY


def fetch_unemployment_json():

    request_url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={API_KEY}"

    response = requests.get(request_url)

    parsed_response = response.json()

    #return parsed_response["data"]

    # we probably want to clean the data before returning it
    # including converting string values to floats
    data = parsed_response["data"]

    # we could use a traditional mapping approach and collect the data into a new empty list
    # but here we are mutating / changing the data in place. choose whatever approach you like

    #clean_data = []
    #for item in data:
    #    clean_data.append({"date": item["date"], "value": float(value)})
    #return clean_data

    for item in data:
        item["value"] = float(item["value"])

    return data



if __name__ == "__main__":


    data = fetch_unemployment_json()

    # Challenge A
    #
    # What is the most recent unemployment rate? And the corresponding date?
    # Display the unemployment rate using a percent sign.

    print("-------------------------")
    print("LATEST UNEMPLOYMENT RATE:")
    #print(data[0])
    print(f"{data[0]['value']}%", "as of", data[0]["date"])




    # Challenge B
    #
    # What is the average unemployment rate for all months during this calendar year?
    # ... How many months does this cover?


    this_year = [d for d in data if "2022-" in d["date"]]

    rates_this_year = [float(d["value"]) for d in this_year]
    #print(rates_this_year)

    print("-------------------------")
    print("AVG UNEMPLOYMENT THIS YEAR:", f"{mean(rates_this_year)}%")
    print("NO MONTHS:", len(this_year))


    # Challenge C
    #
    # Plot a line chart of unemployment rates over time.

    dates = [d["date"] for d in data]
    rates = [float(d["value"]) for d in data]

    fig = line(x=dates, y=rates, title="United States Unemployment Rate over time", labels= {"x": "Month", "y": "Unemployment Rate"})
    fig.show()

    # SEND EMAIL
    # to be honest this part isn't functioning perfectly because the formatting is weird
    # and it asks for user input then overrrides it
    # but I can't figure out how to get it to not ask for user input in the first place
    # but it does send an email!
    from app.email_service import send_email_with_sendgrid
    unemployment_subject = "Unemployment Report"
    latest_unemployment_rate = str(data[0]['value'])
    avg_unemployment_this_year = str(mean(rates_this_year))
    body_of_email_2 = str(("Here are some stats about unemployment rates. ", 
                        "The latest unemployment rate is ", latest_unemployment_rate, 
                        ". The average unemployment rate this year is ", avg_unemployment_this_year))

    send_email_with_sendgrid(subject = unemployment_subject,
                             html_content = body_of_email_2)