function func(matrix) {
    let lengths = [];
    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[i].length; j++) {
            lengths.push(matrix[i][j].length);
        }
    }
    return lengths;
}

const matrix = [
    ["ragac", "ragac2", "ragac3"],
    ["ragac4", "ragac5"],
    ["ragac6", "ragac7"]
];

const result = func(matrix);
console.log(result);