// first way to trigger events based on actions: can trigger multiple events
let element = document.getElementById('button1')

element.addEventListener('click', functionHandler)

function functionHandler(){
    console.log("function handler works!")
}


// ////////////////////////////////////////////////////////////////////////////////////////////////////////////


// second way to trigger events based on actions: only 1 event is triggered
let element2 = document.getElementById('button2')

element2.onclick = functionHandler2;

function functionHandler2(){
    console.log("second way of handling events workds")
}

// ////////////////////////////////////////////////////////////////////////////////////////////////////////////


// third way to trigger events 
// theres an onclick in html page:
function functionHandler3(){
    console.log("third way of handling functions babyyyy")
}


// ////////////////////////////////////////////////////////////////////////////////////////////////////////////



// events have properties and you can access them

let element4 = document.getElementById('button4')

function eventHandlerFunctionProperties(event){
   console.log("time" + event.timeStamp);
   console.log("this is the type of " + event.type);
   console.log("this is the element:" + event.target); // you can access this and make changes
}

element4.addEventListener('click', eventHandlerFunctionProperties);


// not all events depend on user interaction!

// when an en event happens, the browser creates an event object that holds infor about the event