function Student(name, age) {
  this.name = name;
  this.age = age;

  this.getName = function () {
    return this.name;
  };

  this.setName = function (name) {
    this.name = name;
  };

  this.getAge = function () {
    return this.age;
  };

  this.setAge = function (age) {
    this.age = age;
  };
}

function Book(title, author, pages) {
  this.title = title;
  this.author = author;
  this.pages = pages;

  this.getTitle = function () {
    return this.title;
  };

  this.setTitle = function (title) {
    this.title = title;
  };

  this.getAuthor = function () {
    return this.author;
  };

  this.setAuthor = function (author) {
    this.author = author;
  };

  this.getPages = function () {
    return this.pages;
  };

  this.setPages = function (pages) {
    this.pages = pages;
  };
}

function Car(brand, model, year) {
  this.brand = brand;
  this.model = model;
  this.year = year;

  this.getFullName = function () {
    return this.brand + " " + this.model;
  };

  this.setYear = function (year) {
    this.year = year;
  };

  this.getYear = function () {
    return this.year;
  };
}

function Rectangle(width, height) {
  this.width = width;
  this.height = height;

  this.getArea = function () {
    return this.width * this.height;
  };

  this.getPerimeter = function () {
    return 2 * (this.width + this.height);
  };

  this.setWidth = function (width) {
    this.width = width;
  };

  this.setHeight = function (height) {
    this.height = height;
  };

  this.getWidth = function () {
    return this.width;
  };

  this.getHeight = function () {
    return this.height;
  };
}

function User(username, email, password) {
  this.username = username;
  this.email = email;
  this.password = password;

  this.getUsername = function () {
    return this.username;
  };

  this.setUsername = function (username) {
    this.username = username;
  };

  this.getEmail = function () {
    return this.email;
  };

  this.setEmail = function (email) {
    this.email = email;
  };

  this.getPassword = function () {
    return this.password;
  };

  this.setPassword = function (newPassword) {
    this.password = newPassword;
  };
}

