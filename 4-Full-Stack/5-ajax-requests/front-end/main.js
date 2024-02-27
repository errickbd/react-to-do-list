// let students = [
//     {'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'age': '18', 'grade': 'A'},
//     {'id': '2', 'first_name': 'Jane', 'last_name': 'Smith', 'age': '19', 'grade': 'B'},
//     {'id': '3', 'first_name': 'Bob', 'last_name': 'Johnson', 'age': '20', 'grade': 'C'},
//     {'id': '4', 'first_name': 'Emily', 'last_name': 'Williams', 'age': '18', 'grade': 'A'},
//     {'id': '5', 'first_name': 'Michael', 'last_name': 'Brown', 'age': '19', 'grade': 'B'}
// ]

const createStudentItem = (stud) => {
    let studentContainer = document.getElementById('studentContainer')
    let li = document.createElement('li')
    li.innerText = `ID: ${stud.id} | Name: ${stud.first_name} ${stud.last_name} | Age: ${stud.age} | Grade: ${stud.grade}`
    li.addEventListener('mouseover', (event)=>{
        event.target.style.backgroundColor = 'yellow'
        event.target.style.fontSize = '30px'
    })
    li.addEventListener('mouseout',(event)=>{
        event.target.style.backgroundColor = null
        event.target.style.fontSize = null
    })
    li.addEventListener('click', (event)=>{
        event.target.style.textDecoration = 'line-through'
    })
    studentContainer.appendChild(li)
}

const addStudent = (event) => {
    event.preventDefault()
    let data = new FormData(event.target)
    let formattedData = Object.fromEntries(data)
    formattedData['id'] = 1
    createStudentItem(formattedData)
}

const fillColor = (event, clr) => {
    event.stopPropagation()
    let elmnt = event.target
    console.log(event)
    elmnt.style.backgroundColor = clr
}

const getStudents = async() => {
    let response = await fetch("http://127.0.0.1:5000/api/v1/students/")
    let students = await response.json()
    students.map((stud) => {
        // let {id, first_name, last_name, age, grade} = stud
        createStudentItem(stud)
    })
}

const addImage = (url) => {
    // let img = document.body.children[1].children[0].children[0]
    let img = document.getElementById("pokemonImg")
    console.log(img)
    console.log(img.src)
    img.src = url
    img.style.border = 'solid black 5px'
    console.log(img.src)
    let txts = document.getElementsByClassName("randText")
    let query = document.querySelectorAll(".randText")
    console.log(query)
    console.log(txts)
}

const changeGreeting = () => {
    let header = document.body.children[0].children[0]
    let evening = "Good Evening Whiskey"
    let morning = "Hello Whiskey"
    if (header.textContent == morning){
        header.textContent = evening
    }
    else{
        header.textContent = morning
    }
}