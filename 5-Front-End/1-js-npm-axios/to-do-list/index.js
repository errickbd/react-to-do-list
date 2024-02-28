/** 
 * The old way to import is require() - CommonJS Modules. Avoid.
 * */
// require() actually runs the code in the file we give it and returns whatever is returned
// by that file
// const tasks = require('./tasks.json');
// require('./foo.js');

/**
 * Importing the new way with ES6 modules. Always do this unless you can't.
 */
import axios from "axios";

// local imports
import tasks from "./tasks.json" assert { type: "json" }
// default export
import someFunction from "./someFile.js";
// default export and named exports
import fancyObject, { sayHello, sayGoodbye, names } from "./sayHello.js";

console.log('hello world');

/**
 * Axios
 */

// Using promises
// axios
//     .get('https://pokeapi.co/api/v2/pokemon/dittooo')
//     .then(response => {
//         // http response status code from server
//         console.log(response.status)
//         // response.data is data sent back in http response
//         // console.log(response.data)
//     }) 
//     // Axios docs on error handling:
//     // https://github.com/axios/axios?tab=readme-ov-file#handling-errors
//     .catch(error => {
//         console.log(error.response.status); // http response code, which will be error
//         console.log(error.response.statusText); // error message
//         console.log(error.toJSON());
//     })

// Using async/await
const getPokemon = async (pokemonName) => {
    try {
        const response = await axios.get(`https://pokeapi.co/api/v2/pokemon/${pokemonName}`);

        const data = response.data;
        console.log(data)

    } catch (error) {
        console.log(error.toJSON())
    }
}

getPokemon('ditto');



// console.log(tasks);
// sayHello(names[0]);
// sayGoodbye(names[1]);
// console.log(names);

// Loop thru the tasks and print the task name and if its completed
// for (let i = 0; i < tasks.length; i++) {
//     const task = tasks[i];
//     console.log(`${task.task} complete: ${task.completed}`);
// }

// for (let task of tasks) {
//     console.log(`${task.task} complete: ${task.completed}`);
// }

/**
 * .map()
 * 
 * Returns a new array, it lets us transform each element in the old one.
 */

// const taskMessages = tasks.map((t) => {
//     const completed = t.completed ? "Yes." : "No."
//     return `${t.id} - ${t.task} - Completed? ${completed}`
// });

// console.log(taskMessages);
// console.log(tasks);

// const numbers = [1,2,3,4,5,6,7,8]

// const doubledNumbers = numbers.map((num) => {
//     console.log(num)
//     const doubled = num * 2;
//     console.log('doubled is ' + doubled);
//     return doubled;
// });

// console.log(numbers);
// console.log(doubledNumbers);

// const firstTask = tasks[0];
// const id = firstTask.id;
// const completed = firstTask.completed;

// We can use object destructuring instead
// const { id, completed } = firstTask;
// console.log(id)
// console.log(completed)

// const taskIds = tasks.map(({ id, completed }) => {
    // return { id, completed };
// });

// const taskIds = tasks.map((task) => task.id);
// console.log(taskIds);

/**
 * 
 * Filter
 */
const completedTasks = tasks.filter((task) => task.completed);

// console.log(completedTasks);

const doneTasks = completedTasks.map(({ id, task }) => {
    return { id, task };
});

// console.log(doneTasks);

const finishedTasks = tasks
    .filter(task => task.completed)
    .map(task => { 
        return {id: task.id, task: task.task }
    });

// console.log(finishedTasks);

// Array destructuring
function returnsSomeArr() {
    return [{foo: 'a', bar: 'b'}, () => console.log('hello')]
}

// const arrWithStuff = returnsSomeArr();
// const myObj = arrWithStuff[0];
// const myFunc = arrWithStuff[1];
// array destructuring
// const [myObj, myFunc] = returnsSomeArr();
// console.log(myObj);
// myFunc();