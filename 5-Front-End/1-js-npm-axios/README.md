# NPM and React + Vite

## Part I

- What is Node.js and npm
- Creating an npm project (`npm init`)
- What is `package.json`
- Installing dependencies
= `package.json` vs `package-lock.json`
- npm scripts and `package.json`
- Importing in JS: `require()` vs `import()`
- Modern JS features & techniques:
    - Mapping
    - Destructuring
    - Filtering
- Axios

### Why Axios > Fetch?

- Promises by Default: Axios uses Promises for handling asynchronous operations, making it easier to work with asynchronous code. In contrast, Fetch uses a callback-based approach that requires additional work for error handling.

- Request and Response Interceptors: Axios supports request and response interceptors, allowing you to transform data or headers before sending a request or after receiving a response. Fetch doesn't provide this functionality natively.
 
- Browser and Node.js Compatibility: Axios is designed to work seamlessly in both the browser and Node.js environments. Fetch, originally intended for browsers, requires extra work to use in Node.js.

- Error Handling: Axios provides detailed error information by default, making it easier to identify issues during requests. Fetch requires additional error handling logic to provide similar information.


## Part II

- What is Vite & Why do we use it?
- What is React
- Creating React project with vite
- Explore project structure
- Create a simple React guessing game