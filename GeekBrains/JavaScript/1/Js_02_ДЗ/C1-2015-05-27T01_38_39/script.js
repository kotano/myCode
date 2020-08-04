//
// Создание матрицы.
//
function createMatrix() {
    var matrix = document.getElementById('matrix');
    var n = 20 * 20;

    for (var i = 0; i < n; i++) {
        var div = document.createElement('div');
        div.className = 'cell';
        matrix.appendChild(div);
    }
}

//
// Чтение ячейки матрицы.
//
function getCell(row, col) {
    // Функция принимает координаты ячейки
    // должна вернуть true, если она закрашена,
    // false, если не закрашена.
    return document.getElementById('matrix').children[cellNumber(row, col)].style.backgroundColor == 'red';
}

//
// Установка ячейки матрицы.
//
function setCell(row, col, val, color) {
    // Функция принимает координаты ячейки
    // если val == true, закрашивает ячейку,
    // иначе убирает закраску.
    color = color || 'red';
    document.getElementById('matrix').children[cellNumber(row, col)].style.backgroundColor = (val == true ? color : 'white');
}

//
// Вычисление номера ячейки
//
function cellNumber(row, col) {
    return (row - 1) * 20 + (col - 1);
}
//
// Случайное целое
//
function randomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}
//
// Инициализация
//
var currentRow, currentCol, targetRow, targetCol;
//
function init() {
    currentRow = 1;
    currentCol = 1;
    targetRow = randomInt(1, 20);
    targetCol = randomInt(1, 20);
    // Целевая ячейка
    setCell(targetRow, targetCol, true, 'blue');
    // Стартовая ячейка
    setCell(currentRow, currentCol, true);
}
//
// Обработчик нажатия клавиш
//
function checkKeyDown() {
    if ((event.keyCode >= 37) && (event.keyCode <= 40)) {
        setCell(currentRow, currentCol, false);
        switch (event.keyCode) {
            case 37:
                currentCol = (currentCol == 1 ? 1 : (currentCol - 1));
                break;
            case 38:
                currentRow = (currentRow == 1 ? 1 : (currentRow - 1));
                break;
            case 39:
                currentCol = (currentCol == 20 ? 20 : (currentCol + 1));
                break;
            case 40:
                currentRow = (currentRow == 20 ? 20 : (currentRow + 1));
                break;
        }
        if ((currentCol == targetCol) && (currentRow == targetRow)) {
            alert("Поздравления! Цель достигнута!");
            setCell(targetRow, targetCol, false);
            init();
            document.body.focus();
        }
        else {
            setCell(currentRow, currentCol, true);
        }
    }
}

//
// Точка входа.
//
window.onload = function () {
    createMatrix();

    init();

    document.onkeydown = checkKeyDown;
};
