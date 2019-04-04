# beginning of create_db.py
import json
from models import app, db, Artist, Venue
import os

current = os.path.dirname( os.path.realpath(__file__) )
def load_json(filename):
    filename = os.path.join(current, filename)
    with open(filename) as file:
        jsn = json.load(file)
        file.close()

    return jsn

def create_bands():
    bands = load_json('music.json')

    for i, band in enumerate(bands):
        if band['What year did they start making music'] == "None":
            band['What year did they start making music'] = 0000

        newBand = Artist(id = i,
                        band_name = band['Artist name'],
                        members = band['Group name, if none then put none'],
                        genre = band['Genre of music'],
                        is_shows = False,
                        year_started = band['What year did they start making music'])
        
        db.session.add(newBand)
        db.session.commit()

def create_venues():
    venues = load_json('venues.json')

    for i, venue in enumerate(bands):
        if venue['Venue'] == "":
            band['Venue'] = "!!Missing Venue Name!!"

        if venue['Website'][:8] != "https://":
            venue['Website'] = 

        newVenue = Venue(id = i,
                        venue_name = band['Venue'],
                        location = band['Location (do not include Austin,TX, ZIP)'],
                        genres = band['Genres (Format: \"Genre, Genre\")'],
                        days_open = band['Days Open (Format: \"Genre, Genre\")'],
                        hours_open = band['Hours (Format: \"Mon-Sun\")'],
                        image_link = band['Images'],
                        information = band['Information (Keep short, use google/wiki)'],
                        website_link = band['Website'])

        db.session.add(newVenue)
        db.session.commit()
		
create_bands()
# end of create_db.py
