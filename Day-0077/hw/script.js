function func(keys, values) {
    let obj = {};
    for (let i = 0; i < keys.length; i++) {
      obj[keys[i]] = values[i];
    }
    return obj;
}

let keys = ['saxeli', 'asaki', 'qalaqi'];
let values = ['irakli', 16, 'tbilisi'];

let result = func(keys, values);
console.log(result);