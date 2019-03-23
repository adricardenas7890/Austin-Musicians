from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/about/')
def about():
	return render_template('about.html')

@app.route('/general/')
def models():
	return render_template('models.html')

@app.route('/artists/')
def artists():
	return render_template('artists.html')

@app.route('/venues/')
def venues():
	return render_template('venues.html')

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
	render shows: FILL IN
'''
@app.route('/shows/queer_dance_party')
def queer_dance_party():
	return render_template('shows/queer_dance_party.html')




if __name__ == "__main__":
	app.debug = True
	app.run()