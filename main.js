//document.querySelectorAll("content").style.backgroundColor = '#201F2E' // get all the elements with tag dive
//document.querySelectorAll("content").style.fontFamily = 'Roboto' // get all the elements with tag dive 
//it needs to be specific

document.body.style.backgroundColor = 'pink'; // no need for query selector coz body is given
document.querySelector('.heading').style.fontFamily = 'Roboto'; //query selector since classes are more specific


let first = document.children[0];
console.log(first);

first.innerHTML = 'BROWN BEARS ARE AWESOME!'; //changes everything on the page BUT is HEAD ALSO CHANGED? REMOVED? WHAT IDK

// !!!!!!!!!!!!! first.parentNode.style.backgroundColor = 'beige'; //traversing!!! mistake here!!!!!!!!!!!!!

// 1. create elements 
// 2. add a child element as the parent element’s last child node 

let newParagraph = document.createElement('p'); // why do we need to use document to create everything? it makes no sense logically since this will be an empty element
newParagraph.textContent = "Hello!"
document.body.appendChild(newParagraph)


let newAttraction = document.createElement('li')
newAttraction.id = 'vespa'
newAttraction.innerHTML = 'Rent a Vespa'
// document.body. = i cant do this part this should be done in codecademy!!!


// you can delete or hide elements!
// .removeChild(element to be removed)  and document.getElementById('sign').hidden = true;

let elementToRemove = document.querySelector(".vespa")
// why do i keep having to specify document?
// document.getElementByID("italy-attractions").removeChild(elementToRemove) //failed to open


function clickFuction()
