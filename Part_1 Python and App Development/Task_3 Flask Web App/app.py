# Create a Flask Application that takes the user name in the query parameter from the URL and 
# converts it to UPPER CASE and displays it on the browser.

# Step 1 - To import FLASK
from flask import Flask, request

# Step 2 - Create the object with a parameter __name__
app = Flask(__name__)

# Step 3 - Create an END POINT using routes and bind them with a functionality

@app.route("/")
def home_page():
    return "<h1> Welcome to Innomatics Research Labs! <h1>"

@app.route('/upper') # http://127.0.0.1:5000/upper?user=shanu
def UpperCase():
    user = request.args.get('user')
    return '<h1>Nice to meet you {} </h1> <h2> Have a good day.</h2>'.format(user.upper())

#============================================================================================
# BONUS - Be a little creative and try to create some cool functions in your Flask App.
# Convert Celsius to Fahrenheit Degrees

@app.route("/<int:celsius>") # http://127.0.0.1:5000/37
def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit Degrees."""
    fahrenheit = float(celsius) * 9 / 5 + 32
    fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
    return "<h1> Fahrenheit Degrees : {} </h1>".format(str(fahrenheit))

#============================================================================================
    
# Step 4 - Run the app

if __name__ == '__main__':
    app.run(debug=True)