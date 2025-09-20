class Product {
  constructor(name, price) {
    this.name = name;
    this._price = price >= 0 ? price : 0;
  }

  get price() {
    return this._price;
  }

  set price(value) {
    if (value < 0) {
      throw new Error("ფასი არ შეიძლება იყოს უარყოფითი");
    }
    this._price = value;
  }
}

class Rectangle {
  constructor(width, height) {
    this.width = width;
    this.height = height;
  }

  get area() {
    return this.width * this.height;
  }

  set dimensions({ width, height }) {
    this.width = width;
    this.height = height;
  }
}

class User {
  constructor(firstName, lastName) {
    this.firstName = firstName;
    this.lastName = lastName;
  }

  get fullName() {
    return `${this.firstName} ${this.lastName}`;
  }

  set fullName(value) {
    const parts = value.split(" ");
    this.firstName = parts[0];
    this.lastName = parts.slice(1).join(" ");
  }
}

class MathHelper {
  static sum(a, b) {
    return a + b;
  }
}

class Account {
  #balance;

  constructor(initialBalance) {
    this.#balance = initialBalance;
  }

  get balance() {
    return this.#balance;
  }

  set balance(amount) {
    if (amount < 0) {
      throw new Error("ბალანსი არ შეიძლება იყოს უარყოფითი");
    }
    this.#balance = amount;
  }
}
