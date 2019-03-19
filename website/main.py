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


if __name__ == "__main__":
	app.debug = True
	app.run()