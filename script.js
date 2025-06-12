function blooming() {
            var image = document.getElementById('myImage'); <!-- gets the entire tage element-->
            console.log("BHAIIIIII HERE!!! image element:", image);
            console.log("image src:", image.src);

            if (image.src.includes("images/strawberry.png")) {
                console.log("YES THE == WORKED!");
                image.src = "images/star.png";
            } else {
                image.src = "images/strawberry.png";
            } 
        }   



// document.getElementById("id name") = gives a list of all the elements with that ID (1)
// document.getElementsByClassName("class name") = gives a list of all elements that HAVE this class 
console.log(document.getElementsByClassName("container").length); // there is only 1 element that have this class
//document.getElementsByTagName('li') = gives a list of all the elements whose tag matchs that
// tag = a species of an element like <p> or <img>
//document.body.innerHTML = only works for elements that have both opening and closing tag (will not work for image)

//better! = css selectors = you can be more specific in one go on what you want!
// CSS selectors = originally used in CSS to apply styles! = how you target specific elements

// querySelector()
// querySelectorAll()
//document.querySelector('.blue'); = get the first element with class "blue"
// document.querySelector('#mainText'); =  get the element with id "mainText"

