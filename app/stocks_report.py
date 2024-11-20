# this is the app/stocks_report.py file...

# LOCAL DEV (ENV VARS)

from pandas import read_csv
from plotly.express import line

from app.alpha import API_KEY

def format_usd(my_price):
    return f"${float(my_price):,.2f}"

def fetch_stocks_csv(symbol):
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={API_KEY}&outputsize=full&datatype=csv"
    df = read_csv(request_url)
    return df


if __name__ == "__main__":

    # SELECT A SYMBOL

    symbol = input("Please input a symbol (e.g. 'NFLX'): ") or "NFLX"
    print("SYMBOL:", symbol)

    # FETCH THE DATA

    df = fetch_stocks_csv(symbol)

    print(df.columns)
    print(len(df))
    print(df.head())


    # Challenge A
    #
    # What is the most recent adjusted closing price? And the corresponding date?
    # Display the price formatted as USD, with dollar sign and two decimal places.

    print("-------------------------")
    print("LATEST CLOSING PRICE:")
    first_row = df.iloc[0]
    #print(first_row)
    print(f"${first_row['adjusted_close']}", "as of", first_row["timestamp"])


    # Challenge B
    #
    # What is the average, median, min, and max adjusted closing price
    # (over the latest 100 available days only)?

    recent_df = df.iloc[0:100] # use slicing or df.head(100)
    print(len(recent_df))

    print("-------------------------")
    print("RECENT STATS...")
    print(f"MEAN PRICE: ${recent_df['adjusted_close'].mean()}")
    print(f"MEDIAN PRICE: ${recent_df['adjusted_close'].median()}")
    print(f"MIN PRICE: ${recent_df['adjusted_close'].min()}")
    print(f"MAX PRICE: ${recent_df['adjusted_close'].max()}")
    # quantiles, for fun :-)
    print(f"75TH PERCENTILE: ${recent_df['adjusted_close'].quantile(.75).round(2)}")
    print(f"25TH PERCENTILE: ${recent_df['adjusted_close'].quantile(.25).round(2)}")


    # Challenge C
    #
    # Plot a line chart of adjusted closing prices over time (all time).


    fig = line(x=df["timestamp"], y=df["adjusted_close"],
                title=f"Stock Prices ({symbol})",
            labels= {"x": "Date", "y": "Stock Price ($)"})
    fig.show()

    # SEND EMAIL
    # to be honest this part isn't functioning perfectly because the formatting is weird
    # and it asks for user input then overrrides it
    # but I can't figure out how to get it to not ask for user input in the first place
    # but it does send an email!
    from app.email_service import send_email_with_sendgrid
    '''
    stocks_subject = "Stocks Report"
    latest_price = str(first_row['adjusted_close'])
    mean_price = str(recent_df['adjusted_close'].mean())
    median_price = str(recent_df['adjusted_close'].median())
    min_price = str(recent_df['adjusted_close'].min())
    max_price = str(recent_df['adjusted_close'].max())
    body_of_email = str(("Here are some stats about ", symbol, 
                        ". The latest closing price is ", latest_price, 
                        ". The mean price is ", mean_price,
                        ". The median price is ", median_price,
                        ". The minimum price is ", min_price,
                        ". The maximum price is ", max_price))
    '''
    stocks_subject = "Stocks Report"
    latest_price = first_row['adjusted_close']
    mean_price = recent_df['adjusted_close'].mean()
    median_price = recent_df['adjusted_close'].median()
    min_price = recent_df['adjusted_close'].min()
    max_price = recent_df['adjusted_close'].max()
    body_of_email = f"""Here are some stats about {symbol}. The latest closing price is {latest_price}.
    The mean price is {mean_price}. The median price is {median_price}. The minimum price is {min_price}.
    The maximum price is {max_price}.
    """

    send_email_with_sendgrid(subject = stocks_subject,
                             html_content = body_of_email)
