//CREATE CROSSWORD CLASS HERE 
class Crossword {
	constructor(bla,dimension,across,down,solution){
		this._bla = bla;
		this._dimension = dimension;
		this._across = across;
		this._down = down;
		this._solution = solution;
	}
	get bla(){
		return this._bla;
	}
	get dimension(){
		return this._dimension;
	}
  	get across(){
		return this._across;
	}
  	get down(){
		return this._down;
	}
  	get solution(){
		return this._solution;
	}
	get size(){
		return this._dimension * this._dimension;
	}
}


const dimension = 15

const across = [{'num': 1, 'clue': "Mary's pet", 'cell': 0, 'len': 4},
{'num': 5, 'clue': 'Disagreement', 'cell': 5, 'len': 4},
{'num': 9, 'clue': 'Cut, as a turkey', 'cell': 10, 'len': 5},
{'num': 14, 'clue': 'Kind of history', 'cell': 15, 'len': 4},
{'num': 15, 'clue': 'On the sheltered side', 'cell': 20, 'len': 4},
{'num': 16, 'clue': 'Theater awards', 'cell': 25, 'len': 5},
{'num': 17, 'clue': 'Outburst of controversy', 'cell': 30, 'len': 9},
{'num': 19, 'clue': 'Cite', 'cell': 40, 'len': 5},
{'num': 20, 'clue': 'Aim for', 'cell': 45, 'len': 12},
{'num': 22, 'clue': 'JPEG file, often', 'cell': 63, 'len': 3},
{'num': 23, 'clue': 'Rebuke to a backstabber', 'cell': 67, 'len': 4},
{'num': 24, 'clue': 'Tanning lotion tube letters', 'cell': 72, 'len': 3},
{'num': 27, 'clue': 'Graduate prog. award', 'cell': 75, 'len': 3},
{'num': 30, 'clue': 'Old Microsoft product', 'cell': 79, 'len': 3},
{'num': 32, 'clue': 'On-line game character', 'cell': 84, 'len': 6},
{'num': 34, 'clue': 'Regrets', 'cell': 90, 'len': 4},
{'num': 36, 'clue': 'Chess corner piece', 'cell': 95, 'len': 4},
{'num': 39, 'clue': 'Shiraz citizen', 'cell': 100, 'len': 5},
{'num': 40, 'clue': 'Go unnoticed', 'cell': 105, 'len': 15},
{'num': 43, 'clue': 'Get rid of', 'cell': 120, 'len': 5},
{'num': 44, 'clue': 'Haiku, for one', 'cell': 126, 'len': 4} ,
{'num': 45, 'clue': 'Warm and cozy', 'cell': 131, 'len': 4} ,
{'num': 46, 'clue': 'Signal receivers', 'cell': 135, 'len': 6} ,
{'num': 48, 'clue': '"All the way with ___" (political slogan)', 'cell': 143, 'len': 3} ,
{'num': 50, 'clue': '___ Anne de Beaupré', 'cell': 147, 'len': 3} ,
{'num': 51, 'clue': 'Choose', 'cell': 150, 'len': 3} ,
{'num': 52, 'clue': 'Insulation material', 'cell': 154, 'len': 4} ,
{'num': 55, 'clue': 'Shocking swimmer', 'cell': 159, 'len': 3} ,
{'num': 57, 'clue': 'Current sitcom set in Cleveland', 'cell': 168, 'len': 12} ,
{'num': 62, 'clue': 'Very important', 'cell': 180, 'len': 5} ,
{'num': 65, 'clue': 'Direction giver', 'cell': 186, 'len': 9} ,
{'num': 66, 'clue': '"There\'s no such thing as a free lunch," e.g.', 'cell': 195, 'len': 5} ,
{'num': 67, 'clue': 'On strike', 'cell': 201, 'len': 4} ,
{'num': 68, 'clue': 'Police team', 'cell': 206, 'len': 4} ,
{'num': 69, 'clue': 'Office aides', 'cell': 210, 'len': 5} ,
{'num': 70, 'clue': 'Bit of bird chow', 'cell': 216, 'len': 4} ,
{'num': 71, 'clue': "Holliday's marshal friend", 'cell': 221, 'len': 4}]

const down = [{'num': 1, 'clue': 'Hit high in the air', 'cell': 0, 'len': 4} ,
{'num': 2, 'clue': 'Caruso solo', 'cell': 1, 'len': 4} ,
{'num': 3, 'clue': 'Simplified signature', 'cell': 2, 'len': 4} ,
{'num': 4, 'clue': 'Censor', 'cell': 3, 'len': 5} ,
{'num': 5, 'clue': 'College admission factor', 'cell': 5, 'len': 8} ,
{'num': 6, 'clue': 'Tractor attachment', 'cell': 6, 'len': 4} ,
{'num': 7, 'clue': "Eagle's nest", 'cell': 7, 'len': 5} ,
{'num': 8, 'clue': 'Entice', 'cell': 8, 'len': 5} ,
{'num': 9, 'clue': 'French chicken dish', 'cell': 10, 'len': 8} ,
{'num': 10, 'clue': 'Touch', 'cell': 11, 'len': 4} ,
{'num': 11, 'clue': '1983 Duran Duran hit', 'cell': 12, 'len': 3} ,
{'num': 12, 'clue': 'Doggy doc', 'cell': 13, 'len': 3} ,
{'num': 13, 'clue': 'Jargon suffix', 'cell': 14, 'len': 3} ,
{'num': 18, 'clue': 'Spoken', 'cell': 34, 'len': 4} ,
{'num': 21, 'clue': 'LAX listing', 'cell': 54, 'len': 3} ,
{'num': 24, 'clue': 'Soiled spots', 'cell': 72, 'len': 6} ,
{'num': 25, 'clue': 'Succeed', 'cell': 73, 'len': 6} ,
{'num': 26, 'clue': 'Green edge', 'cell': 74, 'len': 6} ,
{'num': 27, 'clue': 'Magic word', 'cell': 75, 'len': 6} ,
{'num': 28, 'clue': 'Keep quiet', 'cell': 76, 'len': 6} ,
{'num': 29, 'clue': 'Draw off sherry', 'cell': 77, 'len': 6} ,
{'num': 31, 'clue': 'Word before bubble or opera', 'cell': 81, 'len': 4} ,
{'num': 33, 'clue': 'Part of NEA', 'cell': 86, 'len': 4} ,
{'num': 35, 'clue': 'Drink with sushi', 'cell': 93, 'len': 4} ,
{'num': 37, 'clue': 'Ally of the Missouri', 'cell': 97, 'len': 3} ,
{'num': 38, 'clue': 'Record company name now licensed to an on-line pharmaceutical company', 'cell': 98, 'len': 4} ,
{'num': 41, 'clue': 'Sings and dances', 'cell': 109, 'len': 8} ,
{'num': 42, 'clue': 'Like some wartime journalists', 'cell': 114, 'len': 8} ,
{'num': 47, 'clue': 'Make soaking wet', 'cell': 140, 'len': 3} ,
{'num': 49, 'clue': 'Boss, usually following "El"', 'cell': 145, 'len': 4} ,
{'num': 53, 'clue': 'Protection', 'cell': 156, 'len': 5} ,
{'num': 54, 'clue': 'Bea Arthur sitcom', 'cell': 157, 'len': 5} ,
{'num': 56, 'clue': 'Fall into disuse', 'cell': 161, 'len': 5} ,
{'num': 57, 'clue': 'NBA target', 'cell': 168, 'len': 4} ,
{'num': 58, 'clue': 'West ___ virus', 'cell': 173, 'len': 4} ,
{'num': 59, 'clue': 'Big Ten school', 'cell': 177, 'len': 4} ,
{'num': 60, 'clue': 'Lenin foe', 'cell': 178, 'len': 4} ,
{'num': 61, 'clue': 'URL starter', 'cell': 179, 'len': 4} ,
{'num': 62, 'clue': 'Exercise accessory', 'cell': 180, 'len': 3} ,
{'num': 63, 'clue': "Paul Bunyan's tool", 'cell': 181, 'len': 3} ,
{'num': 64, 'clue': 'Former NFL quarterback Kelly or Harbaugh', 'cell': 182, 'len': 3}]

const solution = 'LAMB.SPAT.CARVEORAL.ALEE.OBIESFIRESTORM.QUOTETAKEASWIPEAT......PIC.ETTU.SPFPHD.DOS..AVATARRUES.ROOK.IRANIESCAPEATTENTIONSHAKE.POEM.SNUGTUNERS..LBJ.STEOPT.FOAM.EEL......HOPEANDFAITHMAJOR.GUIDEPOSTAXIOM.IDLE.SWATTEMPS.SEED.EARP'

const cw = new Crossword('cw',dimension,across,down,solution);


function index_to_position(index, width){
    // Determine the cartesian coordinates of an index in an array.
    // index - index in the array
    // width - width of the array
    return index % width, index;
}

function position_to_index(x, y, width){
    // Determine the index in an array of cartesian coordinates.
    // x - x position in cartesian
    // y - y position in cartesian
    // width - width of the array
    return x + y * width;
}

var acrossList = document.getElementById('acrossList');
var downList = document.getElementById('downList');

for (var i = 0; i < cw.across.length; i ++){
	var bla = document.createElement('li');
	bla.innerHTML = cw.across[i].clue;
	acrossList.appendChild(bla);
}

for (var i = 0; i < cw.down.length; i ++){
	var bla = document.createElement('li');
	bla.innerHTML = cw.down[i].clue;;
	downList.appendChild(bla);
}

let box = document.getElementById('box');

let wrapper = document.getElementById('wrapper');


wrapper.style = 'border:1px solid black;width:100px;height:100px;margin:0 auto;';
wrapper.style.width = (2*cw.size)+'px';
wrapper.style.height = (2* cw.size)+'px';


var funcs = [];

function createBoard(i){
	return function () {
		if (cw.solution[i] != '.'){		
			var box2 = document.createElement('input');
			box2.maxLength = '1';
			// box2.fontSize = "90px"
			box2.id = 'box' + i;
			box2.style = 'width: 10px;height: 10px;border: 1px solid black;padding: 0;margin: 0;float: left;';
			box2.style.width = (cw.dimension * 2)+'px';
			box2.style.height = (cw.dimension * 2)+'px';
			box2.textAlign ="center";

			//box2.innerHTML = i;
			box2.addEventListener('click', function(){
				if 	(box2.style.backgroundColor === 'red') {
				box2.style.backgroundColor = 'white';}
				else
				{box2.style.backgroundColor = 'white';}
				});	}
		else {
			var box2 = document.createElement('div');
			box2.id = 'box' + i;
			box2.style = 'width: 10px;height: 10px;border: 1px solid black;padding: 0;margin: 0;float: left;';
			box2.style.width = (2 * cw.dimension-2)+'px';
			box2.style.height = (2* cw.dimension-2)+'px';
			box2.style.backgroundColor = 'black';
		}
		wrapper.appendChild(box2);
	};
} 

for (var i = 0; i < (cw.size); i++) {
  funcs[i] = createBoard(i);
}

for (var j = 0; j < (cw.size); j++) {
  // and now let's run each one to see
  funcs[j]();
}

// $('#myForm').submit(function() {
//     var data = $("#myForm:input").serializeArray();
//      alert('Handler for .submit() called.') ;
//      const x = document.CreateElement('p') ;
//      x.innerHTML = data;
//     acrossList.appendChild(x);
// })(jQuery);
 
// $.ajax({
//   type: "POST",
//   url: "/Users/gtrost/Documents/CW/static/puzpy-master/Tests2.py",
//   data: { param: text}
// }).done(function( o ) {
//    // do something
// });
