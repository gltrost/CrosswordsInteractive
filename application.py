
#!/usr/bin/env python
# -*- coding: utf-8 -*- 


# import puz
# import sys
# p = puz.read('testfiles/washpost.puz')


from flask import Flask, request, render_template
import sys
import puz
reload(sys)
sys.setdefaultencoding('utf-8')


p = puz.read('testfiles/washpost.puz')
numbering = p.clue_numbering()

app = Flask(__name__)

# METHODS CALLED FROM puz.py :
#    title: title of crossword
#    across: across clues
#    down: down clues
#    Height: height of board
#    Width: width of board
#    solutions: list of solutions
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
   							author = p.author,
   							copyright = p.copyright)	


if __name__ == '__main__':
   app.run(debug = True)