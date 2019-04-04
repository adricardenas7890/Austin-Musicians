# beginning of create_db.py
import json
from models import *
import os

current = os.path.dirname( os.path.realpath(__file__) )
def load_json(filename):
    filename = os.path.join(current, filename)
    with open(filename) as file:
        jsn = json.load(file)
        file.close()

    return jsn

# Function to remove extra commas
def removeExtraCommas( inputString ):
    inputString = inputString.split(",")
    inputString = inputString.clear("")
    inputString = ",".join(inputString)
    return inputString
# Function to capitalize the first letter of each word
def capitalizeFirst( inputString ):
    inputString = inputString.lower()
    inputString = inputString.title()
    return inputString
# Function to check that each link starts with http or https
def isLinkValid( inputLink ):
    http = inputLink.startswith("http://")
    https = inputLink.startswith("https://")
    return http or https
# Remove all but first link
def removeAllButFirstLink( inputLink ):
    inputLink = inputLink.split("\n")
    inputLink = inputLink.clear("")
    if len(inputLink) > 1:
        return inputLink[0]
    else:
        return "".join(inputLink)

def create_bands():
    # Load the bands in
    bands = load_json('database/artists.json')

    # For each band
    for i, band in enumerate(bands):
        # Get the data
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

        # Clean artists - extra commas and capitilization
        artists = capitalizeFirst( removeExtraCommas( artists ) )
        # Clean genre - extra commas and capitilization
        genre = capitalizeFirst( removeExtraCommas( genre ) )
        # Make sure that year_started is an int
        if type(year_started) != int:
            year_started = 0
        # Check that the image link is valid
        if not isLinkValid( image ):
            image = ""
        image = removeAllButFirstLink( image )
        # Check that the tour link is valid
        if not isLinkValid( tour ):
            tour = ""
        tour = removeAllButFirstLink( tour )
        # Check that the external links are valid
        if not isLinkValid( external_links ):
            external_links = ""
        external_links = removeAllButFirstLink( tour )
        # If email == none or None, set as blank
        if email.lower() == "none" or email.lower() == "na" or email.lower() == "n/a":
            email = ""

        # Create our Band Object


        # db.session.add(newBand)
        # db.session.commit()
		
create_bands()
# end of create_db.py
