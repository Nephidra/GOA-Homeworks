function getEvenNumbersFrom2DArray(arr) {
    let flatArray = [];
    

    for (let i = 0; i < arr.length; i++) {
        for (let j = 0; j < arr[i].length; j++) {
            flatArray.push(arr[i][j]);
        }
    }
    
    let evenNumbers = [];
    

    for (let i = 0; i < flatArray.length; i++) {
        if (flatArray[i] % 2 === 0) {
            evenNumbers.push(flatArray[i]);
        }
    }
    
    return evenNumbers;
}


let matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9, 10]
];