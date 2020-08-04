function Square(row, col, course)
{
	this.body = [row, col];
	this.course = course;
	var that = this; // то = это
	
	this.create = function()
	{
		m1.setCell(that.body[0], that.body[1], true);
	}
	
	this.move = function()
	{
		var last_body = that.body.slice();
		
		switch(that.course)
		{
			case 'right':
				that.body[1]++;
				break;
		}
		
		m1.setCell(last_body[0], last_body[1], false);
		m1.setCell(that.body[0], that.body[1], true);
	}
}