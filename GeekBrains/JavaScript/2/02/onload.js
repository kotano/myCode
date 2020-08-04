//
// Точка входа.
//
window.onload = function()
{
	m1 = new Matrix('matrix1', 20, 20);
	m1.create();
	
	var square = new Square(1, 2, 'right');
	square.create();

	setInterval(square.move, 300);
}		