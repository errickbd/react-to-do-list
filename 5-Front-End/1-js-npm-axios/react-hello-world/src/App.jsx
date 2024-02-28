import './App.css'

function App() {
  const randomNumber = Math.floor(Math.random() * 100 + 1);
  const gameName = "Random Number Game";

  const guessNumber = (e) => {
    e.preventDefault();
    const userInput = document.getElementById("userInput").value;
    console.log(userInput);
  }

  return (
    <>
      <h1>{gameName}</h1>
      <div className="card">
        <p>This is in the card class</p>
        <input id="userInput"></input>
        <button onClick={guessNumber}>
          Guess Number 
        </button>
      </div>
    </>
  )
}

export default App
