#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from flask import Flask, request, render_template
import sys
import puz
from utilities import *
reload(sys)
sys.setdefaultencoding('utf-8')


p = puz.read('testfiles/15by15.puz')
numbering = p.clue_numbering()

app = Flask(__name__)


# METHODS CALLED FROM puz.py:
#    title: title of crossword
#    across: across clues
#    down: down clues
#    Height: height of board
#    Width: width of board
#    solutions: list of solutions
#    lcSolutions : solutions in all lower-case 
#        (needed for pattern matching right answers)
#    author: creator of puzzle
#    copyright: any copyright information

# METHODS CALLED FROM utilities.py:
#    adjuster : alters board size depending on dimensions of the board
#    mergeNumberings : gathers all the numbers to be displayed in the top
#         corners of squares in order
#    assignLetterToAcrossClue : assigns each across clue to its squares
@app.route('/')
def index():
   return render_template('CW.html', title=p.title ,marks = 10, 
                        across= numbering.across,
                        numAcrossClues = len(numbering.across),
                        numDownClues = len(numbering.down),                        
                        down= numbering.down, 
                        Height = p.height, 
                        Width = p.width,
                        listSize = p.height * p.width,
                        solutions = p.solution,
                        lcSolutions = p.solution.lower(),
                        author = p.author,
                        copyright = p.copyright,
                        adjust = adjuster(p.width),
                        numbers = mergeNumberings(p),
                        acrossSets = assignLetterToAcrossClue(p),
                        downSets = assignLetterToDownClue(p))   


if __name__ == '__main__':
   app.run(debug = True)

