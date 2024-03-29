# beginning of models.py
# note that at this point you should have created "bookdb" database (see install_postgres.txt).
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI', "postgresql+psycopg2://postgres:password123@127.0.0.1:5432/austin-music")
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # to suppress a warning message
#db = SQLAlchemy(app)

class Band(db.Model):
    __tablename__ = 'band'

    group =             db.Column( db.String(100),  nullable = False ) 
    artists =           db.Column( db.String(500), nullable = True ) 
    genre =             db.Column( db.String(100),  nullable = True) 
    year_started =      db.Column( db.Integer,  nullable = True) 
    group_summary =     db.Column( db.String(10000),  nullable = True) 
    image =             db.Column( db.String(500), nullable = True )
    albums =            db.Column( db.String(10000), nullable = True )
    tour =              db.Column( db.String(500), nullable = True )
    external_links =    db.Column( db.String(500), nullable = True )
    social_media =      db.Column( db.String(10000), nullable = True )
    email =             db.Column( db.String(100),  nullable = False ) 
    id =                db.Column( db.Integer, primary_key = True )

class Venue(db.Model):
	__tablename__ = 'venue'

	venue_name =	db.Column( db.String(80), nullable = False )
	location =		db.Column( db.String(100), nullable = False )
	genres = 		db.Column( db.String(100), nullable = True )
	days_open = 	db.Column( db.String(100), nullable = True )
	hours_open =	db.Column( db.String(100), nullable = True )
	image_link =	db.Column( db.String(500), nullable = True )
	information =	db.Column( db.String(10000), nullable = True )
	website_link =	db.Column( db.String(1000), nullable = True )
	id =			db.Column( db.Integer, primary_key = True )

class Shows(db.Model):
    __tablename__ = 'shows'

    show_name        =  db.Column( db.String(80), nullable = False)
    presented_by     =  db.Column( db.String(80), nullable = True)
    featured_artists =  db.Column( db.String(300), nullable = False)
    venue            =  db.Column( db.String(80), nullable = False)
    date_time        =  db.Column( db.String(80), nullable = False)
    tickets          =  db.Column( db.String(500), nullable = True)
    flyer            =  db.Column( db.String(500), nullable = True)
    id               =  db.Column( db.Integer, primary_key = True)
