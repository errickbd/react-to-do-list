// Importing just one thing
// const reallyImportantMessage = require("./js-pt-2-testing-scratch");

// Importing the exports object and destructuring it
const { reallyImportantMessage, anotherMessage} = require("./js-pt-2-testing-scratch");

console.log(reallyImportantMessage("yay!"))
console.log(anotherMessage("yay!"))