# this is the "web_app/routes/drink_routes.py" file...

from flask import Blueprint, request, render_template, redirect, flash

from app.drinks import fetch_nonalcoholic_drinks

drink_routes = Blueprint("drink_routes", __name__)

@drink_routes.route("/drinks")
def drinks():
    print("NONALCOHOLIC DRINKS...")

    try:
        drinks = fetch_nonalcoholic_drinks()
        return render_template("drinks.html",drinks=drinks)

    except Exception as err:
        print('OOPS', err)
        return {"message":"Drinks Data Error. Please try again."}, 404