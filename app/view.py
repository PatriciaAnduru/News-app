from flask import Flask, render_template
from app import app
from .request import NewsRequests


@app.route('/')
def index():
    n = NewsRequests()
    # return news.get_top_headlines()
    global_news = n.get_top_headlines(sources='')
    return render_template('index.html', sport=global_news['articles'])


@app.route('/about')
def about():
    return render_template('about.html')
