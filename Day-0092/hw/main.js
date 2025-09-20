function checkNumber(num) {
    return num > 18 ? True : False;
}

function checkNumbers(num1, num2) {
    return num1 > num2 
        ? `${num1} more than ${num2}` 
        : num1 < num2 
            ? `${num2} more than ${num1}` 
            : "Equal";
}
