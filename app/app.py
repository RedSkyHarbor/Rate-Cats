from flask import Flask, render_template
import os
import requests

app = Flask(__name__)

API_KEY = os.environ.get('CAT_API_KEY', None)
CAT_SEARCH_URL = 'https://api.thecatapi.com/v1/images/search'

@app.route('/')
def index():
    r = requests.get(CAT_SEARCH_URL, headers={'x-api-key': API_KEY})
    image = r.json()[0]
    return render_template('index.html', cat=image)
