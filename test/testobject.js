

const person = {
    name : "Melvin",
    age : 19,
    "favorite drink" : "red velvet",
}

function deleteFavDrink(person) {
    delete person["favorite drink"]
}

function deleteAge(person) {
    delete person.age
}

