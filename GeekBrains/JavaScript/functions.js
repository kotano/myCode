
function getRandomNumber(max) {
    return  Math.round(Math.random() * max);
}

function max(a,b) {
    if(a >= b) {
        return a;
    } else {
        return b;
    }
}

function factorial(n) {
    if (n==0) {
        return 1;
    } else if (n<0) {
        alert("Факториал расчитывается только для натуральных чисел.");
    } else {
        return factorial(n - 1) * n;
    }
}

document.onkeydown = function(key) {
alert(key.keyCode)
}

// var f = prompt()
// alert(factorial(f))

// var a = max(34,68)
// var n = getRandomNumber(100);
// var m = getRandomNumber(4);