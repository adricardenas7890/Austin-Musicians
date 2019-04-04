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
    for _ in range(inputString.count("")):
        inputString.remove("")
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
    for _ in range(inputLink.count("")):
        inputLink.remove("")
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
        newBand = Band(group = group,
                    artists = artists,
                    genre = genre,
                    year_started = year_started,
                    group_summary = group_summary,
                    image = image,
                    albums = albums,
                    tour = tour,
                    external_links = external_links,
                    social_media = social_media,
                    email = email,
                    id = i)

        db.session.add(newBand)
        db.session.commit()

def create_venues():
    venues = load_json('venues.json')

    for i, venue in enumerate(bands):

        if band['Venue'] != "":
            band['Venue'] = "!!Missing Venue Name!!"

        band['Venue'] = capitalizeFirst(band['Venue'])
        band['Genres (Format: \"Genre, Genre\")'] = capitalizeFirst(band['Genres (Format: \"Genre, Genre\")'])


        if !isLinkValid(band['Website']):
            band['Website'] = ''

        band['Images'] = removeAllButFirstLink(band['Images'])


        newVenue = Venue(id = i,
                        venue_name = band['Venue'],
                        location = band['Location (do not include Austin,TX, ZIP)'],
                        genres = band['Genres (Format: \"Genre, Genre\")'],
                        days_open = band['Days Open (Format: \"Mon-Sun\")'],
                        hours_open = band['Hours (Format: \"3PM-9PM)'],
                        image_link = band['Images'],
                        information = band['Information (Keep short, use google/wiki)'],
                        website_link = band['Website'])

        db.session.add(newVenue)
        db.session.commit()
		
def create_shows():
    shows = load_json('database/shows.json')

    # For each show
    for i, show in emumerate(shows):
        # Get data
        show_name        = show['Name']
        presented_by     = show['Presented By']
        featured_artists = show['Featured Artist']
        venue            = show['Venue']
        date_time        = show['Date and Time']
        tickets          = show['Tickets']
        flyer            = show['Image Link']

        # if tickets = 'none' replace with nothing
        if tickets == "None": 
            tickets = ""

        # if tickets link not valid, set to nothing
        if not isLinkValid(tickets): 
            tickets = ""

        # if flyer link not valid, set to nothing
        if not isLinkValid(flyer): 
            flyer = ""

        # clean columns - capitalize all first letters and no repeat commas
        show_name = capitalizeFirst(removeExtraCommas(show_name))
        presented_by = capitalizeFirst(removeExtraCommas(presented_by))
        featured_artists = capitalizeFirst(removeExtraCommas(featured_artists))
        venue = capitalizeFirst(removeExtraCommas(venue))
        date_time = capitalizeFirst(removeExtraCommas(date_time))


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
