// const t11_one = new Promise((resolve) => setTimeout(() => resolve("promise 1"), 1000));
// const t11_two = new Promise((resolve) => setTimeout(() => resolve("promise 2"), 2000));
// const t11_three = new Promise((resolve) => setTimeout(() => resolve("promise 3"), 3000));

// Promise.all([t11_one, t11_two, t11_three])
//   .then(values => console.log(values));
  
  
// function randDelayPromise(msg) {
//   const delay = 1000 + Math.random() * 4000
//   return new Promise((resolve) => setTimeout(() => resolve(msg), delay));
// }

// Promise.all([
//   randDelayPromise("Random Promise 1"),
//   randDelayPromise("Random Promise 2"),
//   randDelayPromise("Random Promise 3"),
// ]).then(values => console.log(values));



// const t13_one = new Promise((resolve) => {
//     setTimeout(() => resolve("t1, pass"), 1000);
// });
// const t13_two = new Promise((_, reject) => {
//     setTimeout(() => reject("t2, failed"), 2000);
// });
// const t13_three = new Promise((resolve) => {
//     setTimeout(() => resolve("t3, pass"), 3000);
// });
// Promise.all([t13_one, t13_two, t13_three])
//     .then(values => console.log(values))
//     .catch(error => console.log(error));


// Promise.race([
//     randDelayPromise("race promise 1"),
//     randDelayPromise("race promise 2"),
//     randDelayPromise("race promise 3")
//     ]).then(value => console.log(value));



function randomCondition(name) {
    return new Promise((resolve) => {
        if (Math.random() > 0.5) {
            resolve(name + " instant")
        } else {
            setTimeout(() => resolve(name + " delayed"), 2000)
        }
    })
}

Promise.race([
    randomCondition("first"),
    randomCondition("second"),
    randomCondition("third")
    ]).then(value => console.log(value))

