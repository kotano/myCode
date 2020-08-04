
function createMatrix()
{
	var matrix = document.getElementById('matrix');
	var n = 20 * 20;

	for (var i = 0; i < n; i++)
	{
		var div = document.createElement('div');
		div.className = 'cell';
		matrix.appendChild(div);
	}
	console.log(matrix.classList);
}



function getCell(row, col) {
	var divs = document.querySelectorAll('.cell');
	return divs[row * 20 + col]
}


function setCell(row, col, val) {
	var div = getCell(row, col);
	div && div.classList[val ? 'add' : 'remove']('red')
}
var x = setApple;
function setApple(row, col) {
	var div = getCell(row, col);
	div && div.classList['add']('green')
}



window.onload = function() {
	createMatrix();

	function Apple () {
		var newPos = {
			x: Math.floor((Math.random() * (19 - 1 + 1)) + 1),
			y: Math.floor((Math.random() * (19 - 1 + 1)) + 1)

		};
		return newPos;
	}
	var point = Apple();
	setApple (point.x, point.y, true);

	setCell(0, 0, true);
	var b = {
			39: ["col", 0.15],
			37: ["col", -0.15],
			40: ["row", 0.15],
			38: ["row", -0.15],
			row: 0,
			col: 0
		};
		var c = {};
	function move() {
		if (b.col < 0 || b.col > 19 || b.row < 0 || b.row > 19) {
			alert('game over!');
			return
		}
		for (var a in c)
			if (c[a]) {
				setCell(b.row | 0, b.col | 0, false)
				var d = b[a][0];
				b[d] += b[a][1];
				setCell(b.row | 0, b.col | 0, true)
			}
		window.requestAnimationFrame(move)
	}


	document.body.onkeydown = function (a) {
		a = a || window.event;
		a = a.keyCode;
		a in b && (c = {}, c[a] = true);
		return false
	};
	move();
};