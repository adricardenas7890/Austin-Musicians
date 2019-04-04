from flask import Flask, render_template, url_for
try:
	from models import Band, Venue, Shows, db, app
except:
	from .models import Band, Venue, Shows, db, app
import os

# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']

# Main Page
@app.route('/')
def index():
	return render_template('home.html')

# About Page
@app.route('/about/')
def about():
	return render_template('about.html')

# ????? Unsure what this is here for
@app.route('/general/')
def models():
	return render_template('models.html')

'''
	Overall View
'''

# Artists Page
@app.route('/artists/')
def artists():
	context = Band.query.order_by(Band.group).all()
	return render_template('artists.html', bands = context)

# Venue Page
@app.route('/venues/')
def venues():
	context = Venue.query.order_by(Venue.venue_name).all()
	return render_template('venues.html', venues = context)

# Shows Page
@app.route('/shows/')
def shows():
	context = Shows.query.order_by(Shows.show_name).all()
	return render_template('shows.html', shows = context)

'''
	Dynamic Rendering of each page
'''

# UNFINISHED: GOOGLE "Dynamic URLS Flask" for info https://stackoverflow.com/questions/35107885/how-to-generate-dynamic-urls-in-flask

# Artists Page
@app.route('/artists/<url>')
def artist(url):
	context = Band.query.filter(Band.group == url).first()
	return render_template('artists/template.html', band = context)

# Venue Page
@app.route('/venues/<url>')
def venue(url):
	context = Venue.query.filter(Venue.venue_name == url).first()
	return render_template('venues.html', venue = context)

# Shows Page
@app.route('/shows/<url>')
def show(url):
	context = Shows.query.filter(Shows.show_name == url).first()
	return render_template('shows.html', show = context)


if __name__ == "__main__":
	app.debug = True
	app.run()