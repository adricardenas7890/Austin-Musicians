# Austin Musicians

Welcome to the Wiki for Austin Musicians!

This website was created by Adriana Cardenas, Christian Gil, Katelynn Whittington, and Kevin Han. 

We hope to continue our efforts and produce a website that can continue to assist local Austin residents long after our class is over.

(Originally Gitlab Repository Maintainer: https://gitlab.com/ChristianGil/cs329e-idb)

# 1. Introduction

# Background 

Austin is known as the Live Music Capital of the World, and as such, there is no shortage of musicians performing across the city and throughout the year. The city became known by this title in 1991, when it was found that Austin had more live music venues per capita than any other city in the nation. The thousands of bands and artists that perform regularly live around the city of Austin, and there are around two hundred live music venues in the city alone that show performances just about every day of the year; as a result of the sheer number of artists performing and the venues in which they perform, it can be difficult for potential concert goers to navigate this sea in the Austin live music scene. With so many performances happening every single night, it can be hard to keep track of all the artists, venues, and shows going on. When creating this website, we wanted to help fellow Austinites in search of a good show and put all the information we can find in one central location. Instead of having to sort through Facebook, Instagram, Bandcamp, or any other website in search of tickets, show times, or venue locations, users can just come straight to our website and look up all the information they need.

# The Existing Problem

There are very little resources for finding local Austin musicians and discovering their upcoming shows. Many Austin musicians are still undiscovered. Despite Austin having a thriving music scene, venues are constantly closing down or being rebranded. There are plenty of online resources for seeing tour dates, acquiring tickets, and reading up on each band, but these are all offered separately.

# Our Mission

Our website's purpose is to provide information on live music in Austin for concert goers to have that knowledge in an efficient and intuitive manner. Our website provides this information, breaking it down into content on artists in Austin, venues in the city, and upcoming shows. The website primarily serves to educate the public on different artists in Austin and allow them an easy manner to track upcoming shows for these artists. Our project will bring together all the information that can be acquired with multiple searches into one easy to navigate website. Included are musicians that are local to Austin, shows happening in Austin, and venues only in Austin. Unlike other websites that contain information on shows happening globally, this website is ideal for an Austinite hoping to support the local music scene and catch shows down the street. By offering information on venues, we open the doors for a hidden talent to catch their big break. Our project hopes to connect people to musical talent by providing an easier way to navigate the Austin music scene.


# 2. Design

# Data Sources
We use multiple data sources when compiling our band, venue, and shows datasets. One of the main sources we use for shows is https://www.do512.com. This website is probably the next best, right behind our own. The site contains shows that happen everyday, the venue's information, and pricing. However, their website goes far beyond what we intend to offer by including food specials, happy hour information, and free non-music events.

We found a lot of information on Austin musicians by first searching what musicians are local to Austin. Many of these searches provided limited information, so the members of our project working in the back-end began to research every artist individually. Some artists had more information available on Wikipedia, which we used in our tables. When researching each artist, we first did research on whether this was a solo-artist or a full group with members. Our first attribute was members, which we were able to find on Wikipedia or Facebook Pages. From there, we used the genre the artist uses to describe themselves on their website or what their Wikipedia page states. We limited each genre attribute to three words. The year started was another attribute which proved difficult to find. Some artists do not contain the information for this attribute, which we list as 0. Additionally, we indicate whether this artist is on tour and has upcoming shows or not.

Information on venues was created by searching for music venues in Austin. Since there are over 200, we stuck to the most popular results which probably have hosted the local artists we hope to promote. We chose to stick to official venues that function as business for this phase of our website. In the future, we hope to use unofficial venues so we can fully capture the music scene. The attributes for the venues include the address, a short description of each, and business hours. Additionally, we included their website for more general information on upcoming shows. Those shows that happen to include an Austin Musician are highlighted in our website.

# Data Models

At the beginning phases of our project, we created a Google Excel Sheet and experimented with the attributes each model would have. Our Artist model contains an attribute for the Artist name, members (none if the Artist name is the group name), the Genre of the artist(kept to a minimum of three words), the year the group started,  After a few trials, we decided upon a format for each model of Artist, Show, and Venue. Once we had populated the entire sheet, we downloaded the google sheet as a CSV file. We then used http://freeformatter.com/ to convert our .csv file to a .json. Through create_db.py, we read our json files into Google Cloud Platform. Using the a pg4Admin database viewing software, we were able to visualize our database locally and read the files into our local server. We utilized Cloud SQL Proxy to securely run our database locally. Both the Cloud SQL Proxy and the flask app must be active in order to visualize the website locally. Queries can be run using Pg4Admin, which allows for an easy visualization of our tables. Our models are read into HTML tables by using dynamic flask objects which access our database loop through all records. For each attribute, we also run the attributes through a dynamic loop. Each instance utilizes a dynamic link which then generates a template.html page which is filled in with certain attributes. Our Artist page contains a high resolution photo of the artist, a in-depth about section, members, genres, and upcoming shows. The shows section is dynamic and shows only upcoming shows for the artist selected. In contrast, our view of Shows contains multiple artists for each show and only provides a link to artists that are contained within our database.

# Table Relationships

There are a total of three tables in this database. The first table is 'Band'. The fields for this table are 'group' (string), 'artist' (string), 'genre' (string), 'year_started' (integer), 'group_summary' (string), 'image' (string), 'albums' (string), 'tour' (string), 'external_links' (string), 'social_media' (string), and 'email' (string).
The field 'group', displayed as Artist, is the primary key for this table. If this is a solo artist, the table prints the Artist's name under the 'artist' field, which is displayed under Members. The 'genre' field, displayed as Genre, which is limited to three genres, all capitalized and separated by commas, excluding 'and'. The 'image' field contains a high resolution link of an image of the band. The field 'albums', represented as Albums, is a string separated by new lines, '\n'. The 'tour' field, represented by Tour, is a string represented by 'On Tour' or 'Not On Tour'. The field 'external_links', represented by links on the artist page, are links to a website. The field 'social media', represented by 'Social Media', contains a list of links for various social media, such as instagram, twitter, and facebook. The field 'email', represented by Email, is listed in the artist page. The URL of the artist page is determined by the 'artist' field.
The second table is 'Venue'. The fields for this table are 'venue_name' (string), 'location' (string), 'genre' (string), 'days_open' (string), 'hours_open' (string), 'image_link' (string), 'information' (string), 'website_link' (string). The field 'venue_name', represented in Venue, is a string that contains the venue's full name. The field 'location', represented as Location, which is an address within Austin that excludes 'Austin, TX' and a zip-code. The field 'genre', shown as Genre, is limited to three words, which are all capitalized and separated by commas. The field "days_open", represented by "Days Open" in the table view, consists of a two three letter abbreviation for the day of the week in a range to represent. The field "hours_open", represented as "Hours" in the table view contains a time range for when each venue is most likely open. The field "image_link", represented as a rendered image in the venue view, contains a URL to a high resolution photo of the venue. The field "information", represented as a paragraph of information in the venue instance view.

The third table is 'Shows'. The fields for this table are 'show_name' (string), 'presented_by' (string), 'featured_artists' (string), 'venue' (string), 'date_time' (string), 'tickets' (string), and 'flyer' (string). The field 'show_name', displayed as Show on the model page, is the primary key for this table. The 'presented_by' field, displayed as Presented by, tells the user who is presenting the show. Usually the party presenting the show is the venue itself, and sometimes it is a separate party. The 'featured_artists' field, displayed as Featured Artists, tells the user who all is performing at a particular show, all artists are separated by a new line character, so they appear on different lines. For the shows that identify more as a festival, and not one show, they only include some of the artists, not all of them. The 'venue' field, displayed as Venue on the models page, lets the user know where the show will be taking place. The 'date_time' field, displayed as Date & Time on the models page, tells the user what time and what day they show will be happening on. The 'tickets' field, displayed as Tickets on each individual shows page, links the user to the website that sells online tickets. The 'flyer' field contains the image link of each shows flyer.

# Search Capability

For our search capability, we were able to use the same plugin that we used to make our tables sortable and for the pagination. The plugin is called DataTables. Adding in the search capability was as easy as changing the script in our base.html. Since for our final project we want pagination, searching, and sorting enabled, we want to set searching and paging to true (sorting tables is automatically included in DataTables without specifying a parameter). According to the DataTables documentation, using 'searching' is smart in that it allows the user to input multiple words (space separated) and will match a row containing those words, even if not in the order that was specified (this allow matching across multiple columns). The algorithm for the search capability is subtractive, which means that it filters through the tables in order to find the searched information; it deletes more information in the tables as the search becomes more complex.

# 3. Tools

# Front-end
A base.html page was created to utilize flask block contents and minimize repeating HTML code for the rest of the views. This code includes the stylesheets for Bootstrap4 and scripts for jQuery. This also included a navigation bar that utilizes flask elements to link each render request rather than lengthy URL.
The base.html page was extended to create the home.html page, the about.html page, the artists.html page, the venues.html page, and the shows.html page. There is a navigation at the top of each page that provides a link to each of these general pages from whichever view is currently visited. The navigation bar is formatted with Javascript, causing the current page to show as bold in the navigation bar and indicate it is the current view.
The home.html page, also known as the splash page, was created using a high resolution photo of the Austin Skyline. This image was chosen because the majority of the photo is a light color that the title can contrast against. The title font had a custom CSS class created which contained a white border around black text. A bootstrap card was used in order to display a phrase that would highlight the purpose and mission of our website.
The artists view takes the user to the page listing the artists and general information about them in a table formatted using Bootstrap4. The table is sortable using DataPlugins from all 5 attributes. The instance is linkable to an individual artist page.

-Each instance links to individual artists' pages that renders a photograph, in-depth information about the artist and their genre, members and background, as well as show dates and locations, and links to their social media pages and websites.
The venues view provides the user with a general page that lists venues in Austin and basic information about each of these in a table, as well as links to additional pages for each of the respective venues. This information is contained in a table formatted with Bootstrap and sortable by each attribute. Each instance links to a view for a distinct venue.
-The page for each venue shows a picture of the venue, an about section with more specific information, an interactive map of the venue in relation to Austin in the location section, contact information with links to the venue's website and social media pages, and an upcoming shows section with links to the specific shows pages of our website.
The show tab takes the user to a page that lists the upcoming shows in a table formatted with Bootstrap 4, providing general information about the show, presenter, featured artists, venue, date and time, as well as links to pages for each of the respective shows and links to artists and venues as well. This table is sortable by each attribute. The instances each link to a view for each distinct show.

-The page for each show presents a promotional picture of the show and then goes on to provide a link to the website on which to buy tickets - or states that no tickets are required if that is the case 

- lists the date and time, links to the venue page, and lists the featured artist and provides a link to their page on our website.

In order to highlight the active pages for the website, we used JQuery, and the DataTables plug-in was used to allow for table sorting.

CSS is contained within main.css and about.css. Unique containers were created to contain the splash page photo, each title, view tables, paragraphs, the navigation bar, and navigation links. Default Bootstrap4 elements were changed using "! important" when formatting the navigation bar.
Javascript was contained within main.js, adding features to the navigation links

# Back-end

The website was built using Flask, which used Python 3.7. The main.py file is used to launch the application and render all html pages. A local server was used to visualize changes before deployment.
The web app is hosted on Google Cloud Platform, using App Engine Flexible Environment, which will allow for future incorporation of NoSQL databases for upcoming implementations of the project. The code used to create the web app was uploaded using Google Cloud SDK; Google Cloud SDK is a command line interface for the Google Cloud platform and integrates seamlessly with Google Cloud Engine and other services to allow for each of use for future integrations with other command line tools.
appengine_config.py is a file that was used by Google to import the lib folder that we used. This lib folder is a manifestation of all of the libraries that Python uses so that the app engine that we used had all of the necessary libraries to function properly. Further, app.yaml, which can be seen in our repository, describes which app engine to use when we uploaded using the Google Cloud SDK.

# Embedded media services
The project uses a Google Maps API on the venues page to provide an interactive map of each of the venues under the location section of each of those pages.


# 6. Hosting

The project also provides links to social media pages for the artists and venues, including Facebook, Twitter, Instagram, MySpace, and tumblr, as well as websites for each of the respective artists and venues.

The web app for this project was hosted using Google Cloud Platform (GCP). In order to do this, we used App Engine Flexible Environment, which will allow for easier future integration of other services, such as NoSQL databases, that will need to be incorporated at later stages of the project.
Google Cloud SDK was used to help set up Google Cloud Platform; we used Google Cloud SDK to upload the code used to create the web app. appengine_config.py is the file used by Google to import the library folder that was used for the project; this folder serves as a manifestation of all of the libraries that Python uses so that the app engine has the necessary libraries. Additionally, we used app.yaml to describe which app engine to use when we uploaded our code using Google Cloud SDK.

# 7. Other

# User Stories

As a user, I want to be able to search through each table and organize the table by each field (ascending or descending) so that I can better get information about each artist/venue/show.


As a user, I want to be able to click on a show and buy tickets.


As a user, I want to see shows organized by table where the show is clickable and the artist is clickable if it is contained in the website.


As a user, I want to see a interactive map of the venue location when I click on an instance so that I may better visualize the location.


As a user, I want to see information on venues in a table, where venues are a clickable link so that I may get further information


As a user, I want to be able to visit the social media of an artist in an organized format so that I may get information outside of the website.


As a user, I want to be able to click on an Artist in an Artist table and see more information about the artist in a different view so that the information is organized.


As a user, I want to see a page for Artists that displays a table of information on each artist so that I may click on the table for more information.


As a user, I want to be able to run unit tests from the About page so that I can confirm the website is working properly.


As a user, I want to be able to view information about the team so that I may get more information on the project that was built.


As a user, I should see a navigation bar at the top of each page so that I can navigate between views easily.


As as a user, I want to able to view the splash page upon visiting our website so that I may know the purpose of the website.

# Web Navigation

![alt text](https://gitlab.com/ChristianGil/cs329e-idb/wikis/uploads/be85582939affd90f569a6022afed617/Screen_Shot_2019-03-24_at_9.29.24_PM.png)
