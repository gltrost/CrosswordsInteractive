#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from flask import Flask, request, render_template
from flask_scss import Scss
import sys
import puz
reload(sys)
sys.setdefaultencoding('utf-8')


p = puz.read('testfiles/15by15.puz')
numbering = p.clue_numbering()

app = Flask(__name__)
Scss(app, static_dir='static', asset_dir='assets')

# adjuster : 
# takes in a crossword width and returns a value to 
# adjust the size of the board, allowing for large, medium and small 
# puzzles to all occupy approximately the same size on the screen 
def adjuster(x):
   if (x > 20): return 1.5
   elif (x > 10): return 2.5
   else: return 3.5


# METHODS CALLED FROM puz.py :
#    title: title of crossword
#    across: across clues
#    down: down clues
#    Height: height of board
#    Width: width of board
#    solutions: list of solutions
#    lcSolutions : solutions in all lower-case (needed for pattern matching right answers)
#    author: creator of puzzle
#    copyright: any copyright information
@app.route('/')
def index():
   return render_template('CW.html', title=p.title ,marks = 10, 
   							across= numbering.across, 
   							down= numbering.down, 
   							Height = p.height, 
   							Width = p.width,
   							listSize = p.height * p.width,
   							solutions = p.solution,
                        lcSolutions = p.solution.lower(),
   							author = p.author,
   							copyright = p.copyright,
                        adjust = adjuster(p.width))	


if __name__ == '__main__':
   app.run(debug = True)

