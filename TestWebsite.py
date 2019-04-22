#!/usr/bin/env python3

# -------
# imports
# -------
from unittest import main, TestCase
from website.models import Band, Venue, Shows, db, app


# -----------
# TestWebsite
# -----------

class TestWebsite (TestCase):
    # -------
    # Check functions in code
    # -------

    #check that none of Artist column is empty
    def test_ArtistNotEmpty(self):
        context = Band.query.order_by(Band.group).all()
        for artist in context:
            self.assertEqual(artist.group != "", True)
        pass
    
    #check that none of Show column is empty
    def test_ShowNotEmpty(self):
        context = Shows.query.order_by(Shows.show_name).all()
        for show in context:
            self.assertEqual(show.show_name != "", True)
        pass

    #check that none of Venue column is empty
    def test_VenueNotEmpty(self):
        context = Venue.query.order_by(Venue.venue_name).all()
        return self.assertGreater(len(context), 0)

    #check that exact Artist returns the right Genre
    def test_ArtistGenreIsCorrect(self):
        context = Band.query.filter(Band.group == "TC Superstar").first()
        return self.assertEqual(context.genre, "Pop")

    #check that exact Venue returns the right Address
    #adri
    def test_VenueLocationIsCorrect(self):
        context = Venue.query.filter(Venue.venue_name == "Mohawk").first()
        return self.assertEqual(context.location, "912 Red River St")


    #check that non-existent entry in Venue does not return a value
    def test_VenueNonexistentRecord(self):
        context = Venue.query.filter(Venue.venue_name == "NotRealRecord").first()
        return self.assertEqual(context, None)

    #check that non-existent entry in Show does not return a value
    def test_ShowNonexistentRecord(self):
        context = Shows.query.filter(Shows.show_name == "NotRealRecord").first()
        return self.assertEqual(context, None)

    # from website import main

# ----
# main
# ----			
if __name__ == '__main__':
    main()

""" #pragma: no cover
% coverage3 run --branch TestWebsite.py >  TestWebsite.out 2>&1



% coverage3 report -m   --omit=*/lib/*                >> TestWebsite.out



% cat TestWebsite.out
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
Name             Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------
main.py          27      0      4      0   100%
__init__.py      13      0      0      0   100%
views.py         13      0      0      0   100%
------------------------------------------------------------
TOTAL            53      0      4      0   100%

"""
