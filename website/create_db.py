# beginning of create_db.py
import json
from models import app, db, Artist, Shows
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

def create_shows():
    shows = load_json('shows.json')

    for i, show in emumerate(shows):
        if show['Tickets'] == "None":
            show['Tickets'] = ""

        if (not show['Tickets'].startswith('https://')) or (not show['Tickets'].startswith('http://')):
            show['Tickets'] = 'https://' + show['Tickets']

        if (not show['Image Link'].startswith('https://')) or (not show['Image Link'].startswith('http://')):
            show['Image Link'] = 'https://' + show['Image Link']

        show['Name'].capitalize()
        show['Presented By'].capitalize()
        show['Featured Artist'].capitalize()
        show['Venue'].capitalize()
        show['Date and Time'].capitalize()

        newShow = Shows(id               = i,
                        show_name        = show['Name'],
                        presented_by     = show['Presented By'],
                        featured_artists = show['Featured Artist'],
                        venue            = show['Venue'],
                        date_time        = show['Date and Time'],
                        tickets          = show['Tickets'],
                        flyer            = show['Image Link'])
            
        db.session.add(newShow)
        db.session.commit()

		
create_bands()
create_shows()
# end of create_db.py
