from flask import Flask, render_template, url_for
from models import app
import os

# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']

app = Flask(__name__)

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

# Artists Page
@app.route('/artists/')
def artists():
	return render_template('artists.html')

# Venue Page
@app.route('/venues/')
def venues():
	return render_template('venues.html')

# Shows Page
@app.route('/shows/')
def shows():

	return render_template('shows.html')

'''
	render artists
'''

@app.route('/artists/explosions_in_the_sky/')
def explosions_in_the_sky():
	return render_template('artists/explosions_in_the_sky.html')

@app.route('/artists/octopus_project/')
def octopus_project():
	return render_template('artists/octopus_project.html')

@app.route('/artists/tc_superstar/')
def tc_superstar():
	return render_template('artists/tc_superstar.html')

'''
	render venues
'''

@app.route('/venues/cheer_up_charlies')
def cheer_up_charlies():
	return render_template('venues/cheer_up_charlies.html')

@app.route('/venues/empire_control_room')
def empire_control_room():
	return render_template('venues/empire_control_room.html')

@app.route('/venues/mohawk')
def mohawk():
	return render_template('venues/mohawk.html')


'''
	render shows
'''

@app.route('/shows/queer_dance_party')
def queer_dance_party():
	return render_template('shows/queer_dance_party.html')

@app.route('/shows/clusterfunk_ep_release')
def cluster_funk():
	return render_template('shows/clusterfunk_ep_release.html')

@app.route('/shows/drip_drop_iv')
def drip_drop_iv():
	return render_template('shows/drip_drop_iv.html')




if __name__ == "__main__":
	app.debug = True
	app.run()