
# Divisions

## Purpose

We're using OPR as our source of division dividing randomness at
LAFTC's championship this year. We'll pull each team's non-penalty OPR
off of ftcstats, order them by that (impossible to game meaningfully)
metric, and go every other team for the two divisions.

Data is pulled from http://ftcstats.org/california.html. This is just
to ensure that we have a consistent calculation of OPR. It's a bit of a down
side in that divisions can't be calculated until ftcstats is updated.

## Setup

Probably only works with python 3.

    sudo pip install bs4

## Use

    python3 divisions.py

will print out a team list with divisions, numbers and names. If you also
want OPR's, set an environment variable and run it again. So in a unix-like
shell, you could do

    env AUDIT=y python3 divisions.py

if you wanted to check against ftcstats.
