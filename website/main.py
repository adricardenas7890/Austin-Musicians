from flask import Flask, render_template, url_for, request
try:
	from models import Band, Venue, Shows, db, app
except:
	from .models import Band, Venue, Shows, db, app
import os
import sys
import subprocess
#import coverage
sys.path.append('../')

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
	# # Setup Testing
	# current = os.path.dirname( os.path.dirname( os.path.realpath(__file__) ) )
	# # cov = coverage.Coverage(branch = True, source = os.path.join(current, 'TestWebsite.py'))
	# cov = coverage.Coverage(branch = True)
	# # Do Testing
	# cov.start()
	# import TestWebsite
	# cov.stop()
	# # Save report to file
	# coverageReport = open("coverageReport.txt", "w")
	# cov.report(omit = "*lib*", ignore_errors = True, file = coverageReport)
	# coverageReport.close()
	# Open the file and get the data
	coverageReport = open("coverageReport.txt", "r")
	testData = coverageReport.readlines()
	testData = [x.replace("-", "") for x in testData]
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
	band_context = Band.query.order_by(Band.group).all()
	venue_context = Venue.query.order_by(Venue.venue_name).all()
	return render_template('shows.html', shows = context, bands = band_context, venues = venue_context)

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
	venue_context = Venue.query.order_by(Venue.venue_name).all()
	return render_template('shows/template.html', show = context, bands = band_context, venues = venue_context)


if __name__ == "__main__":
	app.debug = True
	app.run()