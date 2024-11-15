# this is the "test/stocks_test.py" file...

from pandas import DataFrame

from app.stocks_report import fetch_stocks_csv, format_usd

def test_usd_formatting():
    assert format_usd(3.5) == "$3.50"
    assert format_usd(0.44444) == "$0.44"
    assert format_usd(123456789) == "$123,456,789.00"

def test_data_fetching():

    df = fetch_stocks_csv("SPOT")
    assert isinstance(df, DataFrame)
    assert df.columns.tolist() == ["timestamp", "open", "high", "low", "close", "adjusted_close", "volume", "dividend_amount", "split_coefficient"]
    assert len(df) > 1500

    earliest = df.iloc[-1]
    assert earliest["timestamp"] == '2018-04-03'
    assert earliest["adjusted_close"] == 149.01