from flask import Flask, render_template, url_for, request
from sqlalchemy.sql.expression import func, select
try:
	from models import Band, Venue, Shows, db, app
except:
	from .models import Band, Venue, Shows, db, app
import os
import sys
import subprocess
import random
from io import *
from datetime import datetime

# Main Page
@app.route('/')
def index():
	band = Band.query.filter(Band.image != "").order_by(func.random()).first()
	venue = Venue.query.filter(Venue.image_link != "").order_by(func.random()).first()
	show = Shows.query.filter(Shows.flyer != "").order_by(func.random()).first()
	return render_template('home.html', show = show, band = band, venue = venue)

# About Page
@app.route('/about/')
def about():
	# Manually count gitlab commits
	gitlabCommits = getCommits()
	return render_template('about.html', tests = "", commits = gitlabCommits)

@app.route('/about/', methods=['POST'])
def about_post():
	# Commits
	gitlabCommits = getCommits()
	# Setup Testing
	output = getTests()
	return render_template('about.html', tests = "<br/>".join(output.split("\n")), commits = gitlabCommits)

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
	# Convert date string to datetime
	for show in context:
		stipped_datetime = show.date_time.replace("rd", "").replace("th", "").replace("nd", "").replace("@", "") + " 2019"
		try:
			show.date_time = datetime.strptime(stipped_datetime, '%B %d %I%p %Y')
		except:
			show.date_time = datetime.strptime(stipped_datetime, '%B %d %I:%M%p %Y')
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
	# Find what shows have this venue as the venue
	venue_show_list = []
	for show in show_context:
		if show.venue.lower() in context.venue_name.lower():
			venue_show_list.append(show)
	# Of the bands at each show, find which are linkable
	band_context = Band.query.order_by(Band.group).all()
	all_bands_we_have = set( [band.group.lower().strip() for band in band_context] )
	all_bands = dict( zip( sorted( list(all_bands_we_have) ), sorted( [band.group for band in band_context] )) )
	show_band_list = []
	for show in venue_show_list:
		band_dict = {}
		for band in show.featured_artists.split(","):
			band = band.strip().lower()
			if band in all_bands_we_have:
				band_dict[all_bands[band]] = "/artists/" + all_bands[band]
			else:
				band_dict[band.title()] = ""
		show_band_list.append(band_dict)
	return render_template('venues/template.html', venue = context, shows = venue_show_list, artists = show_band_list)

# Shows Page
@app.route('/shows/<url>')
def show(url):
	if " w " in url:
		url = url.replace(" w ", " w/ ")
	context = Shows.query.filter(Shows.show_name == url).first()
	band_context = Band.query.order_by(Band.group).all()
	venue_context = Venue.query.order_by(Venue.venue_name).all()
	return render_template('shows/template.html', show = context, bands = band_context, venues = venue_context)

# Function to open IDB2.log and get commits
def getCommits():
	# Read IDB2.log
	currentParent = os.path.dirname( os.path.realpath(__file__) ) # Parent folder of main.py
	logParent = os.path.dirname( currentParent )
	log = open(os.path.join(logParent, "IDB3.log"), "r")
	GitLabDict = {"ChristianGil": 0, "Katelynn19": 0, "Adriana Cardenas": 0, "Kevin Han": 0, "commit": 0}
	for line in log:
		for ID in GitLabDict.keys():
			if ID != "commit":
				search = " " + ID + " "
			else:
				search = ID + " "
			if search in line:
				GitLabDict[ID] = GitLabDict[ID] + 1
	return GitLabDict
# Function to open TestWebsite.tmp and get test results
def getTests():
	currentParent = os.path.dirname( os.path.realpath(__file__) ) # Parent folder of main.py
	tmpParent = os.path.dirname( currentParent )
	websiteTestResults = open(os.path.join(tmpParent, "TestWebsite.tmp"), 'r')
	string = ""
	for line in websiteTestResults:
		string = string + line
	return string

if __name__ == "__main__":
	app.debug = True # TODO Uncomment in production
	app.run()