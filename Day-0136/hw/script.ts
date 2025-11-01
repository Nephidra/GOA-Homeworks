let num1: number = 5;
let num2: number = 7;
console.log(num1 + num2);

let text: string = "Hello";

function greet(name: string): void {
  console.log("Hello, " + name);
}

function sayHi(): void {
  console.log("Hi!");
}

function sumFive(a: number, b: number, c: number, d: number, e: number): number {
  return a + b + c + d + e;
}
console.log(sumFive(1, 2, 3, 4, 5));

let numbers: number[] = [1, 2, 3];
let names: Array<string> = ["Ana", "Nino"];

let nums: number[] = [10, 20, 30, 40, 50];
let people: string[] = ["Gio", "Luka", "Tiko"];

function printArray(arr: any[]): void {
  for (let i = 0; i < arr.length; i++) {
    console.log(arr[i]);
  }
}
printArray(["apple", "banana", "cherry"]);

function mergeArrays(arr1: any[], arr2: any[]): any[] {
  return arr1.concat(arr2);
}
console.log(mergeArrays([1, 2], [3, 4]));

let user: [string, number] = ["Nino", 25];
let userInfo: [string, number, boolean] = ["Giga", 20, true];
console.log(userInfo);
