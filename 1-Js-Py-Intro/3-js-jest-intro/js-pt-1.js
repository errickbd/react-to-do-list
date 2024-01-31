/*
 * Intro to JS
 * 
 * - Why JS matters & the internet?
 * - Node.js 
 * - Review of JS language features
 *      - Variable types (primitive vars, complex vars)
 *      - Functions
 *      - Conditional logic
 * /
 
/**
 * Features of every programming language:
 * - Syntax
 * - Logical operators (if, and, else)
 * - "Primitive" data types such as strings or integers/numbers and booleans
 * - More complex data types like objects, or dictionaries,
 * - If the language is "strongly typed" or "weakly typed"
 * - "Weakly typed" languages are also called "dynamic" languages
 * - How do you run the code? Do you have to use one program to compile and another to run
 *   the compiled source code?
 */

console.log('hello world')

// Example of changing the type of a variable
x = 5 // number
x = "hello" // string

// not changing type, we change the value but y is still a string
y = "hi"
y = "bye"

/**
 *  Variables
 */

// The bad old way don't do this. ALWAYS use let or const. Start with const, then change to let if you need to.
foo = "hello"
foo = "hi!!!"
console.log(foo)

// `let` lets you change the variable value
let bar = "goodbye"
bar = "sunny"
console.log(bar)

// Example of const not letting us change the value of a var
// const z = 13
// z = 4
// console.log(z)

let z = 13
z = 4
console.log(z)

/**
 * Functions
 */

const someVariable = "this will not work"
console.log(someVariable)

// We can call a function before its defined b/c of function hoisting
myName = makeFullName("Adam", "Cahan")
console.log(myName)
console.log(myName + " lives in Chicago")

// Takes first and last name and returns them together 

/**
 * Combine first and last name to return the full name
 * @param {string} firstName 
 * @param {string} lastName 
 * @returns {string}
 */
function makeFullName(firstName, lastName) {
    return firstName + " " + lastName;
}

/**
 * Variable Types / Data Types
 */

// The undefined data type
// Creating a variable but not giving it a value
// `undefined` is a special type of value that a variable can have
let thisHasNoValue;
console.log(thisHasNoValue);

// The null data type
const thisHasAValue = null;
console.log(thisHasAValue);

// Strings
const aStr = "Today's weather is grey in Chicago";
const anotherString = 'Tomorrow\'s weather will be ...'
console.log(aStr + " " + anotherString);

// String Interpolation
const nameOne = "Alice";
const nameTwo = "Bob";
const message = `It is classic in learning programming to use made up alphabetical order names like ${nameOne} and ${nameTwo}`;
console.log(message);
const anotherMessage = `${makeFullName("Adam", "Cahan")} says two plus two equals ${2 + 2}`
console.log(anotherMessage);

const anotherName = "Benjamin"
console.log(anotherName[0]);
console.log(anotherName[4]);

/**
 * Number Data Type
 * - JS just has the number type
 */

console.log(typeof 5);
console.log(typeof 3.14159);
x = 32
console.log(typeof x);

// exponents/power
console.log(Math.pow(3, 2));

// Round down to the floor
console.log(Math.floor(5.23));

/**
 * Booleans
 */
console.log(true || true);    // true
console.log(true || false);   // true, example of short circuiting
console.log(false || true);   // true
console.log(false || false);  // false

const zzz = true || false;
console.log(zzz);

// truthiness
console.log(1 || false);
console.log(0 || false);
console.log(null || false);
let yyyy;
console.log(yyyy || false);
console.log("abc" || false);
console.log("" || false);

/***
 * Arrays
 */

const daysOfTheWeek = ["mon", "tues", "weds"] // an array with three elements
console.log(daysOfTheWeek[0]);
console.log(daysOfTheWeek[1]);
console.log(daysOfTheWeek[2]);

// arrays are objects and have some functions built in to them
daysOfTheWeek.push("thurs")
console.log(daysOfTheWeek)


/**
 * Objects
 */

const dddd = { myKey: 7, anotherKey: "hello" }
console.log(dddd)
console.log(dddd.myKey)
console.log(dddd['myKey'])

const database = {
    457: {
        name: "Tom",
        age: 34
    }, 
    577782: {
        name: "Sally", 
        age: 42,
    },
    something: [3, "hello", { foo: 'bar'}],
    somethingElse: null,
    getFullName: makeFullName,
}

database.something.push('yet another thing');
database[457].name = "Jerry";
console.log(database.getFullName("Alice", "Waters"))





/*
multi line comment
multi line comment
 */

// Single line comment in JS
// Another single line comment