let person = {
    name: "Nino",
    age: 30,
    profession: "programmer",
    city: "Tbilisi",
    language: "Georgian"
};

console.log(person.profession);


let obj = {
    row_0: [2, 4, 6, 8, 10],
    row_1: [1, 3, 5, 7, 9]
};

for (let i = 0; i < obj.row_0.length; i++) {
    console.log(`row_0 element: ${obj.row_0[i]}, row_1 element: ${obj.row_1[i]}`);
}


function createArrayFromObject(obj) {
    let quantity = obj.quantity;
    let element = obj.element;
    
    let resultArray = [];
    for (let i = 0; i < quantity; i++) {
        resultArray.push(element);
    }
    
    return resultArray;
}

let inputObj = {
    quantity: 5,
    element: "apple"
};

let result = createArrayFromObject(inputObj);
console.log(result);