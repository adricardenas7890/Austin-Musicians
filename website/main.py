from flask import Flask, render_template, url_for, request
try:
	from models import Band, Venue, Shows, db, app
except:
	from .models import Band, Venue, Shows, db, app
import os
import subprocess

# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']

# Main Page
@app.route('/')
def index():
	return render_template('home.html')

# About Page
@app.route('/about/')
def about():
	return render_template('about.html', tests = {})

@app.route('/about/', methods=['POST'])
def about_post():
	# Save current path
	og_path = os.path.dirname( os.path.realpath(__file__) )
	# Change to path where "make test" can run
	os.chdir( os.path.dirname(os.path.dirname( os.path.realpath(__file__) ) ))
	# Clean
	subprocess.check_output(['make', 'clean'])
	# Make test
	testData = subprocess.check_output(['make', 'test'])
	# GO back to origional path
	os.chdir( og_path )
	# Split by newline
	testData = testData.decode().split("\n")
	return render_template('about.html', tests = testData)

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

# Artists Page
@app.route('/artists/<url>')
def artist(url):
	context = Band.query.filter(Band.group == url).first()
	show_context = Shows.query.order_by(Shows.show_name).all()
	venue_context = Venue.query.order_by(Venue.venue_name).all()
	return render_template('artists/template.html', band = context, shows = show_context, venues = venue_context)

# Venue Page
@app.route('/venues/<url>')
def venue(url):
	context = Venue.query.filter(Venue.venue_name == url).first()
	show_context = Shows.query.order_by(Shows.show_name).all()
	return render_template('venues/template.html', venue = context, shows = show_context)

# Shows Page
@app.route('/shows/<url>')
def show(url):
	if " w " in url:
		url = url.replace(" w ", " w/ ")
	context = Shows.query.filter(Shows.show_name == url).first()
	band_context = Band.query.order_by(Band.group).all()
	return render_template('shows/template.html', show = context, bands = band_context)


if __name__ == "__main__":
	app.debug = True
	app.run()