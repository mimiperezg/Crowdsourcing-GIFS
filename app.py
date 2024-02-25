import requests
from flask import Flask, render_template, request
import giphy_client
from giphy_client.rest import ApiException


api_key = 'jxBRxbkEp4LLtLEOMsOpnI2VQGuDHkfV'

# creating an app with flask
app = Flask(__name__)

# defining route for home page
@app.route('/')
def index():
    # index.html for the homepage
    return render_template('index.html')

# route for handling search requests
@app.route('/search', methods = ['POST'])
def search(api_key = api_key):
    # api key
    api_key = api_key
    # getting user input and search type using POST instead of GET (to send to the server)
    # getting data from the user form
    user_input = request.form['user_input']
    limit = 5

    api_instance = giphy_client.DefaultApi()
    api_instance.api_key = api_key

    try:
        # Use the SDK to search for GIFs --  based on user input's keywords
        response = api_instance.gifs_search_get(api_key, user_input, limit=limit)
        gifs = response.data

        # render result.html with the gifs collected to display them
        return render_template('result.html', gifs=gifs)
    except ApiException as e:
        # API error to show up if GIF retrieval doesnt work
        error_message = f"Error: {str(e)}"
        return render_template('error.html', error_message=error_message)
    

if __name__ == '__main__':
    app.run(debug=True)
