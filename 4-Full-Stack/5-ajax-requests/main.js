// const getPokemon = () => {
//     fetch("https://pokeapi.co/api/v2/pokemon/ipsuhgvf")
//     .then((response)=> response.json())
//     .then((responseData)=>console.log(responseData))
//     .catch((error)=>{
//         console.error(error.message)
//         console.log("You made a mistake")
//     })
// }

const getPokemon = async(event) => {
    try{
        event.preventDefault()
        let form = new FormData(event.target)
        let formData = Object.fromEntries(form)
        console.log(typeof(formData), console.log(formData))
        let response = await fetch(`https://pokeapi.co/api/v2/pokemon/${formData.pokemon}`)
        let responseData = await response.json()
        console.log(responseData.sprites)
        let img = document.getElementById("pokemonImg")
        let name = document.getElementById("pokemonName")
        name.innerText = responseData.name.toUpperCase()
        img.src = responseData.sprites.front_default
        img.style.border = "5px yellow solid"
        img.style.borderRadius = "20px"
        img.style.height = "200px"
    } 
    catch(err){
        console.log(err.message)
    }
}

