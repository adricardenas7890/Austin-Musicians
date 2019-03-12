#!/usr/bin/env python3

# -------
# imports
# -------
from unittest import main, TestCase

# -----------
# TestWebsite
# -----------

class TestWebsite (TestCase):

    # ----
    # Check Dependencies
    # ----

    def test_isFlaskPresent(self):
        successful = False
        try:
            # Hide depreciation warning
            import warnings
            warnings.filterwarnings("ignore", category=DeprecationWarning) 
            # Do Test
            from flask import Flask
            successful = True
        except:
            pass
        self.assertTrue(successful, "ERROR: Could not import flask")

    # -------
    # Check functions in code
    # -------

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
