import puz
p = puz.read('testfiles/washpost.puz')

numbering = p.clue_numbering()

print('Across')
for clue in numbering.across:
    answer = ''.join(
        p.solution[clue['cell'] + i]
        for i in range(clue['len']))
    print( clue['num'], clue['clue'], '-', answer)

print( 'Down')
for clue in numbering.down:
    answer = ''.join(
        p.solution[clue['cell'] + i * numbering.width]
        for i in range(clue['len']))
    print( clue['num'], clue['clue'], '-', answer)

print (p.height)

for row in range(p.height):
    cell = row * p.width
    # Substitute p.solution for p.fill to print( the answers
    print( ' '.join(p.fill[cell:cell + p.width]))


print(numbering.across, "\n \n \n")
 

p.unlock_solution(7844)
# p.solution is unscambled

p.save('mine.puz')

print("Preamble:" ,p.preamble, "\n")

print("Postscript: ", p.postscript, "\n")
print("Title: ", p.title, "\n")

print("Author: ",p.author, "\n")

print("copyright: ", p.copyright, "\n")

print("width: ", p.width , "\n")

print("height: ", p.height , "\n")

print("version : ",p.version, "\n" )

print("fileversion : ",p.fileversion, "\n") 

print("unk1 : ",p.unk1, "\n" )

print("unk2 : ",p.unk2, "\n" )

print("scrambled_cksum : ",p.scrambled_cksum, "\n" )

print("fill : ",p.fill, "\n")

print("solution: ", p.solution, "\n")

print("clues : ",p.clues , "\n")

print("notes : ",p.notes, "\n")

print("extensions : ",p.extensions, "\n") 

print("extensions order : ",p._extensions_order, "\n") 

print("puzzletype : ",p.puzzletype, "\n"  )

print("solution state : ",p.solution_state, "\n")  

print("helpers : ",p.helpers  )


