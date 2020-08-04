const matrix = document.getElementById('matrix');
function createMatrix() {
    let n = 20*20;
    for(i=0; i<n; i++) {
        let div = document.createElement('div');
        div.className = 'cell'
        div.id='c'+(i+1);
        matrix.appendChild(div)
    }
}
function cellNumber(row, col) {
    return 20*(row-1)+(col-1)
}
function setCell(row, col,color) {
    color = color || 'red';
    document.getElementById('matrix').children[cellNumber(row,col)].style.backgroundColor = color //(val == true ? color : 'white');
}
function randomInt(min,max) {
    let rand = Math.random();
    let num =  Math.floor(rand * (max-min+1));
    return num;
}

let currentRow, currentCol, targetRow, targetCol;
function init() {
    currentRow = 1;
    currentCol = 3;
    targetRow = randomInt(1,20);
    targetCol = randomInt(1,20);
    setCell(currentRow,currentCol);
    setCell(targetRow,targetCol,'blue');
}
function checkKeyDown() {
    if((event.keyCode >= 37) && (event.keyCode <= 40)) {
        setCell(currentRow,currentCol,'white')
        switch (event.keyCode) {
            case 37:
                currentCol = (currentCol == 1 ? 1 : currentCol-1);
                break;
            case 38:
                currentRow = (currentRow == 1 ? 1 : currentRow - 1);
                break;
            case 39:
                currentCol = (currentCol == 20 ? 20 : currentCol+1);
                break;
            case 40:
                    currentRow = (currentRow == 20 ? 20 : currentRow+1);
                break;
            
        }
        setCell(currentRow, currentCol)
        if((currentRow == targetRow) && (currentCol == targetCol)) {
            alert('Поздравляем! Вы достигли цели!');
            setCell(targetRow, targetCol, 'white');
            init();
            // document.body.focus()
        } 
    }

}
window.onload = function() {
    createMatrix()
    init()
    document.onkeydown = checkKeyDown;
}