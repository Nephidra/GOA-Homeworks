function Car(make, model, year) {
    this.make = make;
    this.model = model;
    this.year = year;
}

let car1 = new Car("Toyota", "Corolla", 2020);
let car2 = new Car("Honda", "Civic", 2018);
let car3 = new Car("Ford", "Mustang", 2022);

function Animal(species, name, age) {
    this.species = species;
    this.name = name;
    this.age = age;
}

let animal1 = new Animal("Dog", "ragac", 3);
let animal2 = new Animal("Cat", "ragac 2", 2);
let animal3 = new Animal("Parrot", "ragac 3", 5);

function Student(name, age, grade) {
    this.name = name;
    this.age = age;
    this.grade = grade;
}

let student1 = new Student("Nino", 16, "10 grade");
let student2 = new Student("Giorgi", 17, "11 grade");
let student3 = new Student("Mariami", 15, "9 grade");

console.log(car1, car2, car3);
console.log(animal1, animal2, animal3);
console.log(student1, student2, student3);
