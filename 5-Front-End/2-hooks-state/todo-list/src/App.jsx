import { useState } from 'react'
import './App.css'
import tasksData from './data/tasks.json';
// Get tasks data from json

// Show the list of tasks

// An input and form so a user can create and add a new task, which we then
// see in the list

function App() {
  const [count, setCount] = useState(0);
  const [showHello, setShowHello] = useState(true);
  const [tasks, setTasks] = useState(tasksData);
  // const [newTaskInput, ]
  
  // console.log('tasks data', tasksData);
  console.log('hello world');
  console.log('tasks', tasks);

  const toggleDisplayMessage = () => setShowHello(!showHello);
  const renderDisplayMessage = () => showHello ? "Hello" : "Goodbye";

  const renderTask = (task) => {
    return `ID: ${task.id}, ${task.task}, COMPLETED: ${task.completed ? "Yes" : "No"}`;
  }

  
  const exampleNewTask = { id: 8, task: "Buy groceries", completed: false };

  const addTaskHandler =() => {
    console.log('add task');
    const newTask = {id: tasks.length +1, task: newTaskInput, completed:false}
    setTasks([ ...tasks, newTask])
  };

  const handleNewTaskInput = (event) => {
    console.log(('handleNewTaskInput'), event.target.value);
    setNewTaskInput(event.target.value)
  }


  return (
    <>
      <h1>{showHello ? "Hello" : "Goodbye"}</h1>
      <h1>{renderDisplayMessage()}</h1>
      <button onClick={toggleDisplayMessage}>Change Display Message</button>
      <button onClick={() => setCount((count) => count + 1)}>
        count is {count}
      </button>
      <h1>Tasks App</h1>
      <ul>
        {tasks.map((task, i) => <li key={i}>{renderTask(task)}</li>)}
      </ul>
      <h2>Create New Task</h2>
      <input placeholder={"Enter Task Description"} onChange={handleNewTaskInput} value={newTaskInput}></input>
      <button onClick={addTaskHandler}>Add Example New Task</button>
      
    </>
  )
}




export default App
