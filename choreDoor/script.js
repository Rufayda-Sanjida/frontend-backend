let doorImage1;
let doorImage2;
let doorImage3;

let door1 = document.getElementById('door1');

let door2 = document.getElementById('door2')

let door3 = document.getElementById('door3')

let startButton = document.getElementById('start');


let numClosedDoors = 3;
let currentlyPlaying = false;


// door = closed -> true else false
function isClicked(door){
    if (door.src.includes("closedDoor.jpg")) {
        console.log("True and the door you clicked is " + door.id)
        return true
    } else{
        console.log("False and the door you clicked is " + door.id)
        return false
    }
}

// door = bot door -> true else false
function isBot(door){
    if (door.src.includes("botDoor.jpg")) {
        console.log("A bot door and the door you clicked is " + door.id)
        return true
    } else{
        console.log("Not a bot door and the door you clicked is " + door.id)
        return false
    }
}

function gameOver(status){
    let currentlyPlaying = false;
    if (status == "win"){
        startButton.innerHTML = 'You win! The remaining door had the bot door. Click here to play again.'
    } else{
        startButton.innerHTML = 'You Lost! Game over! Click here to play again.'
    }
}

function checks(door){

    if (numClosedDoors == 1){
        console.log("numClosedDoors: " + numClosedDoors)
        gameOver('win')
        currentlyPlaying = false
    }
    
    if (isBot(door) === true){
        console.log("we are herererererere")
        gameOver()
        currentlyPlaying = false
    }
    
} 




// // // is the door i clicked on, open or closed?
// // // is the door i clicked, the chore door?
// // // game over function, simply when the game is over - display whether the user lost or won

// // //overall game loop:
// // // 3 closed doors
// // // each time a door is clicked, numClosedDoor goes down by 1
// // // if the numClosedDoor = 0 then the player won the game
// // // if bot door is clicked then player lost


function randomChoreDoorGenerator() {
  const botDoor = Math.floor(Math.random() * 3);

  if (botDoor === 0) {
    doorImage1 = "./images/botDoor.jpg";
    doorImage2 = "./images/openDoor.jpg";
    doorImage3 = "./images/openDoor.jpg";
  } else if (botDoor === 1) {
    doorImage2 = "./images/botDoor.jpg";
    doorImage1 = "./images/openDoor.jpg";
    doorImage3 = "./images/openDoor.jpg";
  } else {
    doorImage3 = "./images/botDoor.jpg";
    doorImage1 = "./images/openDoor.jpg";
    doorImage2 = "./images/openDoor.jpg";
  }
}



function startRound(){
    console.log("started round!")
    door1.src = "./images/closedDoor.jpg"
    door2.src = "./images/closedDoor.jpg"
    door3.src = "./images/closedDoor.jpg"
    numClosedDoors = 3
    currentlyPlaying = true
    startButton.innerHTML = "we are currently playing! Click here to restart"
    randomChoreDoorGenerator()
}


function doorClicked(door){
    if (currentlyPlaying === true){
        numClosedDoors--;
        console.log(numClosedDoors)
        console.log("door.src is", door.src);

        //show the door that is clicked on
        if (door.id === "door1") {
            door.src = doorImage1;
            checks(door)
        } else if (door.id === "door2") {
            door.src = doorImage2;
            checks(door)
        } else {
            door.src = doorImage3;
            checks(door)
        }
    } else{
        startButton.innerHTML = "we are not playing! Click here to restart"
    }
}