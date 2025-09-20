let num = parseInt(prompt("Enter a number:"));
console.log(num % 2 === 0 ? "Two" : num);

let num = parseInt(prompt("Enter a number:"));
console.log(num % 2 === 0 ? num * 8 : num * 9);

function checkNumber(num) {
    return num > 0 ? "Positive" : "Negative";
}

function random(arr) {
    return arr[Math.floor(Math.random() * arr.length)];
}