from flask import Flask 
from helper import pets

app = Flask("__name__")

@app.route("/")
def index():
    return '''<h1>Adopt a Pet!</h1> 
    <p>Browse through the links below to find your new furry friend: </p>
    <ul>

    <li>    <a href="/animals/dogs">Dogs</a> </li>
    <li>    <a href="/animals/cats">Cats</a> </li>
    <li>    <a href="/animals/rabbits">Rabbits</a> </li>

    </ul>
    '''


@app.route('/animals/<string:pet_type>')
def animals(pet_type):
    html = f'<h1>List of {pet_type}</h1>'
    html = html + "<ul>"
    numberOfPets = len(pets[pet_type])
    for eachPet in range(0, numberOfPets):
        print(pets[pet_type][eachPet]["name"])
        name = pets[pet_type][eachPet]["name"]
        htmlName = f'<li> <a href="/animals/{pet_type}/{eachPet}">{name}</a></li>'
        html = html + htmlName
    
    html = html + "</ul>"
    return html

@app.route('/animals/<string:pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
    #index position = pet_id
    pet = pets[pet_type][pet_id]
    
    petName = pets[pet_type][pet_id]["name"]
    picUrl = pets[pet_type][pet_id]["url"]
    petDescription = pets[pet_type][pet_id]["description"]
    petBreed = pets[pet_type][pet_id]["breed"]
    petAge = pets[pet_type][pet_id]["age"]
    
    html = f"<h1>{petName}</h1>"
    html = html + f'<img src="{picUrl}">'
    html = html + f'<p>{petDescription}</p>'
    html = html + f'<ul> <li>Age: {petAge}</li> <li>Breed: {petBreed}</li>  </ul>'
    return html
    print(pet)
