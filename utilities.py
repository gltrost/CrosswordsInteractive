from flask import Flask, request, render_template
import puz
import utilities
import string

app = Flask(__name__)

#ADJUSTS THE SIZE OF THE BOARD ACCORDING TO THE DIMENSIONS OF THE BOARD
def adjuster(x):
   if (x > 20): return 1.5
   elif (x > 10): return 2.5
   else: return 3.5

#MERGES ACROSS AND DOWN BOARD-NUMBERINGS INTO A SINGLE LIST
#None REPRESENTS THE SQUARE HAS NO NUMBER
def mergeNumberings(p):
    numbering = p.clue_numbering()
    across = numbering.across
    down = numbering.down
    aLen = len(across)
    dLen = len(down)
    a = 0
    d = 0
    result = []
    count = 0
    while (count < (p.width * p.height)):
        if (a < aLen and across[a]['cell'] == count):
            result.append(across[a]['num'])
            if (d < dLen and across[a]['cell'] == down[d]['cell']):
                d = d + 1
            a = a + 1
        elif (d < dLen and down[d]['cell'] == count):
            result.append(down[d]['num'])
            d = d + 1
        else: 
            result.append(None)
        count = count + 1
    return result

# DASHES SIGNIFY BEGINNINGS OF WORDS
def pFillRowSlice(p):
    result = ""
    dashes = p.fill
    length = len(dashes) #this is equal to the board-size
    count = 0
    Height = p.height
    Width = p.width
    numbering = p.clue_numbering()
    for i in range(0,length):
        if (i == 0):
            result = result + dashes[i]
        elif (i % Width == 0 and dashes[i-1] != "."):
            result = result + "/"
        elif (result[i-1] == "." and dashes[i]=="-"):
            result = result + "/"    
        else: 
            result = result + dashes[i]
    return result      


#GIVES THE PROPER ROW-COL INDICES FOR AN ELEMENT IN THE (i)th PLACE IN
#A LIST FOR A MATRIX WITH 2 DIMENSIONS width AND height 
def listToCross(i,width,height):
    return str((i // height + 1))+"-"+str((i % width +1))


#COMBINES ACROSS-CLUE-NUMBERS WITH THEIR RESPECTIVE SQUARES
def assignLetterToAcrossClue(p):
    result = []
    dashes = pFillRowSlice(p)
    length = len(dashes) #this is equal to the board-size + (width - 1)
    count = 0
    Height = p.height
    Width = p.width
    numbering = p.clue_numbering()
    for i in range(0,length):
        if (dashes[i] == "/"):
            count = count + 1
            result.append({'aNum':numbering.across[count]['num'],
            	'aList':[listToCross(i,Width,Height)]})
        elif (dashes[i] == "-"):
            if (i == 0):
                result.append({'aNum':numbering.across[count]['num'],'aList':["1-1"]})                     
            elif (dashes[i-1] == "."):
                count = count + 1
                result.append({'aNum':numbering.across[count]['num'],
                	'aList':[listToCross(i,Width,Height)]})
            else:
                result[count]['aList'].append(listToCross(i,Width,Height))
        else: 
            pass
    return result 


def getDownMarkers(p):
    numbering = p.clue_numbering()
    down = numbering.down
    dLen = len(down)
    d = 0
    result = []
    count = 0
    while (count < (p.width * p.height)):
        if (d < dLen and down[d]['cell'] == count):
            result.append(down[d]['num'])
            d = d + 1
        else: 
            result.append(None)
        count = count + 1
    return result





#COMBINES DOWN-CLUE-NUMBERS WITH THEIR RESPECTIVE SQUARES
def assignLetterToDownClue(p):
    result = []
    markers = getDownMarkers(p)
    length = len(markers) #this is equal to the board-size + (width - 1)
    count = 0
    Height = p.height
    Width = p.width
    numbering = p.clue_numbering()
    downClues = numbering.down
    for i in range(0,length):
        if (markers[i] == None):
            pass 
        else: 
            clueLen = numbering.down[count]['len']
            for j in range(0,clueLen):
                if (j==0):
                    result.append({'dNum':downClues[count]['num'],
                        'dList':[listToCross(downClues[count]['cell'],Width,Height)]})
                else:
                    result[count]['dList'].append(listToCross(downClues[count]['cell']+(j*Width),Width,Height))
            count = count + 1
    return result 