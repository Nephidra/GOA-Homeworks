function Car(brand, model, year, engineVolume) {
    this.brand = brand;
    this.model = model;
    this.year = year;
    this.engineVolume = engineVolume;
}

Car.prototype.getDescription = function() {
    return `${this.brand} ${this.model}, ${this.year}, ${this.engineVolume}L`;
};

let car1 = new Car("rag", "ac", 2018, 1.8);
let car2 = new Car("rag", "ac 2", 2020, 2.0);
let car3 = new Car("rag", "ac 3", 2022, 5.0);

console.log(car1.getDescription());
console.log(car2.getDescription());
console.log(car3.getDescription());


function Book(title, author, pages, year) {
    this.title = title;
    this.author = author;
    this.pages = pages;
    this.year = year;
}

Book.prototype.pagesPerDay = function() {
    return this.pages / 7;
};

let book1 = new Book("wigni 1", "avtori 1", 180, 1925);
let book2 = new Book("wigni 2", "avtori 2", 328, 1949);
let book3 = new Book("wigni 3", "avtori 3", 281, 1960);

console.log(`${book1.title}:${book1.pagesPerDay()}`);
console.log(`${book2.title}:${book2.pagesPerDay()}`);
console.log(`${book3.title}:${book3.pagesPerDay()}`);


function Athlete(name, age, sport, trainingHours) {
    this.name = name;
    this.age = age;
    this.sport = sport;
    this.trainingHours = trainingHours;
}

Athlete.prototype.calc = function() {
    let increase = this.trainingHours * 0.2;
    let totalDailyHours = this.trainingHours + increase;
    return totalDailyHours * 7;
};

let athlete1 = new Athlete("vigac", 25, "curva", 2);
let athlete2 = new Athlete("vigac 2", 22, "rbena", 3);
let athlete3 = new Athlete("vigac 3", 28, "fexburti", 1.5);

console.log(`${athlete1.name}:${athlete1.calc()}`);
console.log(`${athlete2.name}:${athlete2.calc()}`);
console.log(`${athlete3.name}:${athlete3.calc()}`);