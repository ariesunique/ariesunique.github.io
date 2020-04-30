=============
Stock Tracker
=============

:date: 2019-04-04 8:21
:tags: 30-day-project-challenge
:category: blog, projects
:slug: stock-tracker
:summary: A CLI tool to display a stock quote for a given stock symbol.

------------
Description
------------

A simple command line interface to look up the stock quote of a given stock symbol

**Example Usage**:

 .. code-block:: shell

    >> stocktracker GOOG

    Here are the stock prices on 2019-10-27:

    Stock      Quote
    =========================
    GOOG       1265.1300

    >> stocktracker GOOG AAPL FB

    Here are the stock prices on 2019-10-27:

    Stock      Quote
    =========================
    GOOG       1265.1300
    AAPL       246.5800
    FB         187.8900

    >> stocktracker -a GOOG AAPL FB

    Here are the stock prices on 2019-10-27:

    Stock      Quote
    =========================
    AAPL       246.5800
    FB         187.8900
    GOOG       1265.1300


**Code**:

Full `source code <https://github.com/ariesunique/30-day-project-challenge/tree/master/stocktracker>`_ in GitHub

---------------
What I Learned
---------------

I only worked on this for about 5 consecutive days in short bursts (but this could easily have been done in an hour or two on a single day). I chose this project because I like command-line interfaces and I wanted to work more with the Click library.

The first step was to figure out how I would get the stock quotes. I found a nice site with a free API for this purpose - alphavantage. I signed up for a free API key and added this to my config file. I’m using configparser to read the config file. To make this into a true CLI, I added a setup.py file (so the code can be called with a simple command instead of having to type the “python” command to run this).

----------
Assessment
----------

I learned more about Click and ConfigParser, and how to create a setup.py file.
There is a lot more that could be added to make this more robust, but it works well enough as a simple CLI proof-of-concept. This was a fun little project and I plan to use Click again for future CLI tools.
