# beginning of models.py
# note that at this point you should have created "bookdb" database (see install_postgres.txt).
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI', "postgresql+psycopg2://postgres:password123@127.0.0.1:5432/austin-music")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # to suppress a warning message
db = SQLAlchemy(app)

class Band(db.Model):
    __tablename__ = 'band'

    group =         db.Column( db.String(80),  nullable = False ) 
    artists   =     db.Column( db.String(500), nullable = True ) 
    genre     =     db.Column( db.String(50),  nullable = True) 
    is_shows  =     db.Column( db.Boolean, nullable = False ) 
    year_started =  db.Column( db.Integer, nullable = True ) 
    id =            db.Column( db.Integer, primary_key = True )
    
    group =             band["group"]
    artists =           band["artists"]
    genre =             band["Genre"]
    year_started =      band["year_started"]
    group_summary =     band["group_summary"]
    image =             band["image"]
    albums =            band["albums"]
    tour =              band["tour"]
    external_links =    band["external_links"]
    social_media =      band["social_media"]
    email =             band["email"]

class Shows(db.Shows):
    __tablename__ = 'shows'

    show_name        =  db.Column( db.String(80), nullable = False)
    presented_by     =  db.Column( db.String(80), nullable = True)
    featured_artists =  db.Column( db.String(300), nullable = False)
    venue            =  db.Column( db.String(80), nullable = False)
    date_time        =  db.Column( db.String(80), nullable = False)
    tickets          =  db.Column( db.String(500), nullable = True)
    flyer            =  db.Column( db.String(500), nullable = True)
    id               =  db.Column( db.Integer, primary_key = True)

db.drop_all()
db.create_all()
# End of models.py