from flask import Flask, request, render_template
import puz
import utilities
import string

app = Flask(__name__)

def adjuster(x):
   if (x > 20): return 1.5
   elif (x > 10): return 2.5
   else: return 3.5

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
            result.append({'aNum':numbering.across[count]['num'],'aList':[str((i // Height + 1))+"-"+str((i % Width + 1))]})
        elif (dashes[i] == "-"):
            if (i == 0):
                result.append({'aNum':numbering.across[count]['num'],'aList':["1-1"]})                     
            elif (dashes[i-1] == "."):
                count = count + 1
                result.append({'aNum':numbering.across[count]['num'],'aList':[str((i // Height + 1))+"-"+str((i % Width +1))]})
            else:
                result[count]['aList'].append(str((i // Height + 1))+"-"+str((i % Width +1)))
        else: 
            pass
    return result 