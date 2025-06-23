#flask = microframework because it has minimal  minimal built-in components and requirements but can be used to built a full fledge app

#we are importing the module (flask) that includes all the classes and functions 
#from that module we are importing a class called FLASK = needed to create the main application object
#whats the difference between library and module?
from flask import Flask

#need an instance of the Flask class
#when we make a flask app, we need to put in the name of the application
# __name__ = the value depends on how we execute the script [if directly than it will be __main__] if we import it to another python program as module, then it will be replaced with filename
myApp = Flask(__name__)

print(__name__) #__main__

#routing! 
# handling requests to different URLs, we create different endpoints to take care of the different URLs

# view function: takes care of request to a URL(s): processing the request and generating a response
# you need to bind URLs to view functions with a route decorator: takes the URL path as parameter, or the part of the URL that follows the domain name. 
# URL = starts with ("/")
# multiple URLS can be bind to the same end points 

@myApp.route("/")
@myApp.route("/home")
def home():
    return 'Hello, World!'

#end points can be HTML pages too! (multi line = ''' insert here ''')
@myApp.route("/home1")
def home1():
    return '''<h1>Hello, World!</h1> 
    <p>hi </p> '''


#Dynamic routes: routes can include variables and it will be processed in the view function 
@myApp.route('/<name>/<int:age>')
def name(name, age):
    return(f"hello {name} and I am {age} years old")


@myApp.route("/returnHome")
def returnHome():
    return '<a href="/">Return back to home page</a>'


#whats a URL slug??
@myApp.route("/article/<string:article_name>")
def article(article_name):
    myList = list(article_name)
    newString = ""
    for x in myList:
        if x == "-":
            newString = newString + " "
        else:
            newString = newString + x
    
    return f''' <p>{newString}</p> '''
