function Person(name, age, height, id) {
    this.name = name;
    this.age = age;
    this.height = height;
    this.id = id;
}

let person1 = new Person("Nino", 30, 165, "001");
let person2 = new Person("Giorgi", 25, 180, "002");
let person3 = new Person("Mariami", 28, 170, "003");

console.log(person1);
console.log(person2);
console.log(person3);
