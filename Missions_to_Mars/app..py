from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://localhost:27017/mars_news'
mongo = PyMongo(app)

@app.route('/')
def index():
    listings = mongo.db.news.find_one()
    return render_template('index.html',listings=listings)

@app.route('/scrape')
def scraper():
    #listings = mongo.db.listings
    #listings_data = scrape_mars.scrape()
    #listings.update({}, listings_data, upsert=True)
    

if __name__ == "__main__":
