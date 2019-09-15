# CrosswordsInteractive

## Goals

This is a work in progress front and back-end project for a crossword puzzle website, using HTML, Python, Jinja and Flask.

It will become an interactive crossword site where multiple people may fill in a crossword simultaneously from different computers. 

## Running this application

### Requirements

* Python 3.4+ 

```
pip install Flask==1.1.1
```

### Running this application

```
FLASK_APP=application.py FLASK_RUN_PORT=5000 flask run --host=0.0.0.0
```

## Architecture
  1. `applications.py` : The main Python application file, linked to puz.py 
  2. `CW.html` : The main HTML file
  3. `puz.py` : Crossword parser, taken from [`alexdef/puzpy`](https://github.com/alexdej/puzpy/blob/master/puz.py).

## Examplex
![](images/readmePhoto.png)

## Testing
Some puzzles (.puz files) are available in the /testfiles folder. These puzzles allow for integration testing. The project defaults to using 15by15.puz, which exists in /testfiles. To test different puzzles, you can go to applications.py and edit line 12 ("p = puz.read('testfiles/15by15.puz'") by inserting the name of your prefered .puz file over "15by15.puz".
