//
// Класс матрицы.
//
function Matrix(containerId, rows, cols)
{
	// id контейнера
	this.containerId = containerId;
	
	// число строк 
	this.rows = rows;
	
	// число столбцов
	this.cols = cols;
	
	// создание сетки
	this.create = function()
	{
		var matrix = document.getElementById(this.containerId);
		var n = this.rows * this.cols;	
		
		matrix.innerHTML = '';
		 
		for (var i = 0; i < n; i++)
		{
			var div = document.createElement('div');
			div.className = 'cell';
			matrix.appendChild(div);
		}
	}
	
	// получить значение ячейки
	this.getCell = function(row, col)
	{
		// todo
	}
	
	// установить значение ячейки
	this.setCell = function(row, col, val)
	{
		var ind = (row - 1) * this.cols + col - 1;
		var matrix = document.getElementById(this.containerId);
		var cell = matrix.children[ind];
		
		if(val)
			cell.className = 'cell on';
		else
			cell.className = 'cell';
		
	}	
}

//
// Точка входа.
//
window.onload = function()
{
	var m1 = new Matrix('matrix1', 20, 20);
	m1.create();
	m1.setCell(5, 5, true);

	var m2 = new Matrix('matrix2', 10, 10);
	m2.create();
	m2.setCell(2, 2, true);	
	m2.setCell(2, 3, true);		
}				
