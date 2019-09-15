# CrosswordsInteractive

## Goals

This is a work in progress front and back-end project for a crossword puzzle website, using HTML, Python, Jinja and Flask.

It will become an interactive crossword site where multiple people may fill in a crossword simultaneously from different computers. 

## Running this application

### Requirements

* Python 3.4+ 

```
pip install Flask==1.1.1
pip install puzpy==0.2.5
```

### Running this application

```
FLASK_APP=application.py FLASK_RUN_PORT=5000 flask run --host=0.0.0.0
```
Then open in your web browser `http://127.0.0.1:5000/`. 

## Architecture
  1. `applications.py` : The main Python application file. Starts a Flask application and initiates a crossword.
  2. `templates/CW.html` : The main HTML file. Displays the crossword puzzle, clues and correct-answer checker. 

## Examplex
![](images/readmePhoto.png)

## Testing
This project so far is mostly an interface to an existing library. Therefore, all tests have been manual. To perform manual tests, do the following: For each `.puz` file in `/testfiles`, move the name of the `.puz` file into `applications.py` on line 12. Run the application and visually confirm that the crossword puzzle looks like the image in this `README`. 
