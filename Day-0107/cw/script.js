const arr = ["Goa", "novatori", "step", "step"];

const newArr = arr.map(word => {
    if (word.charAt(0) === word.charAt(0).toUpperCase()) {
        return "Good";
    } else {
        return "Bad";
    }
});

console.log(newArr);

const numbers = [11, 3, 1, 5, 6, 2, 0, 13];
const filtered = numbers.filter(num => num > 5);

console.log(filtered);