from flask import Flask, make_response, render_template, request, redirect
import os
import requests

app = Flask(__name__)

API_KEY = os.environ.get('CAT_API_KEY', None)
CAT_SEARCH_URL = 'https://api.thecatapi.com/v1/images/search'
CAT_VOTE_URL = 'https://api.thecatapi.com/v1/votes'

@app.route('/')
def vote():
    """displays image of cat on webpage for user to vote on"""
    r = requests.get(CAT_SEARCH_URL, headers={'x-api-key': API_KEY})
    image = r.json()[0]
    return render_template('vote.html', cat=image)

@app.route('/favorites')
def favorites():
    """displays all favorited cat images"""
    if not request.cookies.get('favorite_cats'):
        # render favorite template with no image ids, handle view accoordingly
        return render_template('favorites.html')
    else:
        image_ids = request.cookies.get('favorite_cats').split(' ')
        urls = []
        for image_id in image_ids:
            r = requests.get('https://api.thecatapi.com/v1/images/' + image_id, headers={'x-api-key': API_KEY})
            urls.append(r.json()['url'])
        return render_template('favorites.html', urls=urls)

@app.route('/like', methods=['POST'])
def like():
    """sends vote to cat api with a like vote"""
    r = requests.post(CAT_VOTE_URL, json={'image_id': request.form["id"], 'value': 1 })
    return redirect("/")

@app.route('/dislike', methods=['POST'])
def dislike():
    """sends vote to cat api with a dislike vote"""
    r = requests.post(CAT_VOTE_URL, json={'image_id': request.form["id"], 'value': 0 })
    return redirect("/")


@app.route('/favorite', methods=['POST'])
def favorite():
    """Stores id of cat image in cookie"""
    res = make_response(redirect('/'))
    if not request.cookies.get('favorite_cats'):
        res.set_cookie('favorite_cats', value=request.form["id"], max_age=None)
    else:
        cookie = request.cookies.get('favorite_cats')
        res.set_cookie('favorite_cats', value=cookie + " " + request.form["id"], max_age=None)
    return res

@app.context_processor
def inject_template_scope():
    injections = dict()

    def cookies_check():
        value = request.cookies.get('cookie_consent')
        return value == 'true'
    injections.update(cookies_check=cookies_check)

    return injections