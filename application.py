
#!/usr/bin/env python
# -*- coding: utf-8 -*- 


# import puz
# import sys
# p = puz.read('testfiles/washpost.puz')




# numbering = p.clue_numbering()

# print('Across')
# for clue in numbering.across:
#     answer = ''.join(
#         p.solution[clue['cell'] + i]
#         for i in range(clue['len']))
#     print( clue['num'], clue['clue'], '-', answer)

# print( 'Down')
# for clue in numbering.down:
#     answer = ''.join(
#         p.solution[clue['cell'] + i * numbering.width]
#         for i in range(clue['len']))
#     print( clue['num'], clue['clue'], '-', answer)

# for row in range(p.height):
#     cell = row * p.width
#     # Substitute p.solution for p.fill to print( the answers
#     print( ' '.join(p.fill[cell:cell + p.width]))

# p.unlock_solution(7844)
# # p.solution is unscambled

# p.fill = 'LAMB' + p.fill[4:]
# p.save('mine.puz')

from flask import Flask, request, render_template
import sys
import puz
reload(sys)
sys.setdefaultencoding('utf-8')

# class Crossword :
# 	def __init__(self,title,height,width,across,down,solution):
# 		self.title = title
# 		self.height = height
# 		self.width = width
# 		self.across = across
# 		self.down = down
# 		self.solution = solution	
	
# 	def size(self):
# 		return self.width * self.height


p = puz.read('testfiles/washpost.puz')
numbering = p.clue_numbering()

# These are the lists of clues, with each clue formatted as follows:
# {'num': 1, 'clue': "Mary's pet", 'cell': 0, 'len': 4
# cw = Crossword(title,height,width,across,down,solution)

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('CW.html', title=p.title ,marks = 10, 
   							across=numbering.across, 
   							down=numbering.down, 
   							Height = p.height, 
   							Width = p.width,
   							listSize = p.height * p.width,
   							solutions = p.solution,
   							author = p.author,
   							copyright = p.copyright)	


if __name__ == '__main__':
   app.run(debug = True)