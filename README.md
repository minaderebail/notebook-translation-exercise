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

## API Keys

[Obtain an API Key](https://www.alphavantage.co/support/#api-key) from AlphaVantage.


If you would like to enable email-sending functionality:

To use SendGrid for sending email, you must first follow some setup instructions to create an account, verify your account, setup a single sender address and verify it, then finally obtain an API Key:

First, sign up for a SendGrid account, and click the verification link sent to your email address. (https://signup.sendgrid.com/)

Then follow the instructions to complete your "Single Sender Verification", and click the verification link sent in another confirmation email to verify your single sender address (i.e. the SENDGRID_SENDER_ADDRESS). You should be able to access these settings via the "Sender Authentication" section of the settings menu.

Finally, create a SendGrid API Key with "full access" permissions (i.e. the SENDGRID_API_KEY). You should be able to access these settings via the "API Keys" section of the settings menu. (https://app.sendgrid.com/settings/api_keys)

Once you have obtained the credentials, set them as env variables in the called SENDGRID_SENDER_ADDRESS and SENDGRID_API_KEY, respectively.

Create a ".env" file and add contents like the following (using your own AlphaVantage API Key and Sendgrid credentials):

```sh
# this is the ".env" file:
ALPHAVANTAGE_API_KEY="..."
SENDGRID_API_KEY="..."
SENDGRID_SENDER_ADDRESS="..."
```


## Usage

Run the example script:

```sh
python app/example.py
```


Run the unemployment report:

```sh
python -m app.unemployment_report
```


Run the stocks report:

```sh
python -m app.stocks_report
```


Run the example email sending file:

```sh
python app/email_service.py
```

## Web App
Run the web app (then view in the browser at http://localhost:5000/):

```sh
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
```

## Testing

Run tests:
```sh
pytest
```