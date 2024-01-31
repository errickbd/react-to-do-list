/**
 * Intermediate JS and testing with Jest
 * 
 * - More advanced JS language features
 *      - Syntactic Sugar: an easier way to type something
 * - Intro to Testing and testing with Jest
 */

/**
 * Arrow functions
 */

// Functions are "first class" in Javascript. This sometimes is called "first class functions"
function sayHello(name) {
    return `hello ${name}`
}

const hi = sayHello;
const myObj = {
    sayHi: sayHello,
}

hi();
myObj.sayHi();

function helloWorld(messageFunc, name) {
    console.log(`${messageFunc(name)}. How are you ${name}?`);
}

helloWorld(sayHello, "Bob");

// Arrow functions

// Single line arrow function; no arrow brackets or return statement needed.
const makeFullName = (firstName, lastName) => `${firstName} ${lastName}`;
console.log(makeFullName("Carol", "King"));

// Multi line arrow function with curly brackets. 
const makeNamePlusMore = (firstName, lastName, job) => {
    full = `${firstName} ${lastName}`;
    console.log(full);
    return `${full} is a ${job}`
}

console.log(makeNamePlusMore("Carol", "King", "singer"));

// Example of an arrow function with a first class function
const nums = [1, 2, 3];

const doubles = nums.map((x) => x * 2);

console.log(doubles); // [2, 4, 6]

/**
 * Destructuring
 */

// Destructuring Arrays

// Older way
const myArray = ["x", "y", "z"]
const x = myArray[0];
const y = myArray[1];
const z = myArray[2];

// Newer way with destructuring
const [a, b, c] = ["x", "y", "z"]
console.log(a);
console.log(b);
console.log(c);

// Destructuring Objects

// The not-destructuring way
const myObject = { a: 45, b: "hello", c: true };
const aa = myObject.a;
const bb = myObject.b;
const cc = myObject.c;
console.log(aa);
console.log(bb);
console.log(cc);

// Destructuring an object to get its keys
const { d, e, f } = { d: 45, e: "hello", f: true }
console.log(d);

// This is the better to do object destructuring
const someThing = { xx: 12, yy: "foo", zz: "bar" }

const { xx, yy } = someThing;
console.log(xx);
console.log(yy);

/**
 * The Spread Operator
 */

const arr = [1, 2, 3]

const copyOfArr = [ ...arr, 4, 5, 6 ];
console.log(copyOfArr)

console.log(arr);

const someObj = { a: 'hi', b: 'bye', c: 'foo'}

const anotherObj = { ...someObj, foo: 'bar'}
console.log(anotherObj);

console.log(someObj);

/**
 * Importing and exporting
 */

function reallyImportantMessage(message) {
    return `This is important: ${message}.`
}

function anotherMessage(message) {
    return `This message is less important: ${message}`
}

// Exporting one thing
// module.exports = reallyImportantMessage;

module.exports = {
    reallyImportantMessage,
    anotherMessage,

    // Don't need to do this because of syntactic sugar
    // reallyImportantMessage: reallyImportantMessage,
    // anotherMessage: anotherMessage,
};