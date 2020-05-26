from flask import Flask, render_template, request, redirect
import os
import requests

app = Flask(__name__)

API_KEY = os.environ.get('CAT_API_KEY', None)
CAT_SEARCH_URL = 'https://api.thecatapi.com/v1/images/search'
CAT_VOTE_URL = 'https://api.thecatapi.com/v1/votes'

@app.route('/')
def index():
    r = requests.get(CAT_SEARCH_URL, headers={'x-api-key': API_KEY})
    image = r.json()[0]
    return render_template('index.html', cat=image)

@app.route('/like', methods=['POST'])
def like():
    r = requests.post(CAT_VOTE_URL, json={'image_id': request.form["id"], 'value': 1 })
    return redirect("/")

@app.route('/dislike', methods=['POST'])
def dislike():
    r = requests.post(CAT_VOTE_URL, json={'image_id': request.form["id"], 'value': 0 })
    return redirect("/")


