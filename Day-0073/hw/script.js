let people = [
    { name: "Nino", age: 30, height: 165, gender: "Female" },
    { name: "Giorgi", age: 25, height: 180, gender: "Male" },
    { name: "Mariami", age: 28, height: 170, gender: "Female" },
    { name: "Lasha", age: 35, height: 175, gender: "Male" }
];

people.forEach((person, i) => {
    console.log(`${i + 1}) Person:`);
    console.log(`Name: ${person.name},`);
    console.log(`Age: ${person.age},`);
    console.log(`Height: ${person.height},`);
    console.log(`Gender: ${person.gender}`);
    console.log('');
});