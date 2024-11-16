
# this is the app/email_service.py file...

# LOCAL DEV (ENV VARS)

import os
from dotenv import load_dotenv

load_dotenv() # looks in the ".env" file for env vars

SENDGRID_SENDER_ADDRESS = input("Please input the sender's email address: ")
SENDGRID_RECIPIENT_ADDRESS = input("Please input the recipient's email address: ")
SENDGRID_SUBJECT = input("Please input the email's subject line: ")
SENDGRID_EMAIL_CONTENTS = input("Please type the email's contents: ")
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# HELPER FUNCTION:

def send_email_with_sendgrid(sender_address = SENDGRID_SENDER_ADDRESS, 
                             recipient_address = SENDGRID_RECIPIENT_ADDRESS,
                             subject = SENDGRID_SUBJECT,
                             html_content = SENDGRID_EMAIL_CONTENTS
                            ):
    """Sends an email to the given recipient address.
    """
    print("SENDING EMAIL FROM:", sender_address)
    print("SENDING EMAIL TO:", recipient_address)
    print("SUBJECT:", subject)
    print("HTML:", html_content)

    client = SendGridAPIClient(SENDGRID_API_KEY)
    print("CLIENT:", type(client))

    # always send from the sender, but allow us to customize the recipient by passing it in to the function as a parameter
    message = Mail(from_email=SENDGRID_SENDER_ADDRESS, to_emails=recipient_address, subject=subject, html_content=html_content)

    try:
        response = client.send(message)

        print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
        print(response.status_code) #> 202 indicates SUCCESS
        #print(response.body)
        #print(response.headers)
        print("Email sent successfully!")
    except Exception as err:
        print(f"Error sending email:")
        print(type(err))
        print(err)


if __name__ == "__main__":

    # SEND EXAMPLE EMAIL:

    send_email_with_sendgrid(sender_address = SENDGRID_SENDER_ADDRESS, 
                             recipient_address = SENDGRID_RECIPIENT_ADDRESS,
                             subject = SENDGRID_SUBJECT,
                             html_content = SENDGRID_EMAIL_CONTENTS)