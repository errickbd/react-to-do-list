export const sayHello = (name) => {
    console.log('Hello ' + name);
}

export const sayGoodbye = (name) => {
    console.log('Goodbye ' + name);
}

export const names = ['Alice', 'Bob']

// Default export
const fancyObject = {
    foo: 'bar',
    baz: () => console.log('fancy object')
}

export default fancyObject