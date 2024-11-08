# version-control-exercise

## Setup

Create a new virtual environment (first time only):

```sh
conda create -n reports-env python=3.10
```

Activate the virtual environment (whenever you come back to this project): 

```sh
conda activate reports-env
```


Install packages:

```sh
pip install -r requirements.txt
```


[Obtain an API Key](https://www.alphavantage.co/support/#api-key) from AlphaVantage.

Create a ".env" file and add contents like the following (using your own AlphaVantage API Key):

```sh
# this is the ".env" file:
ALPHAVANTAGE_API_KEY="..."
```


## Usage

Run the example script:

```sh
python app/example.py
```


Run the unemployment report:

```sh
ALPHAVANTAGE_API_KEY="..." python app/unemployment_report.py
```


Run the stocks report:

```sh
python app/stocks_report.py
```