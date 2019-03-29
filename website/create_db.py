# beginning of create_db.py
import json
from models import app, db, Artist
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
		
create_bands()
# end of create_db.py
