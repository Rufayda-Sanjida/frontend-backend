from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#database configuration
app = Flask(__name__) #application instance

#we are setting the SQLALCHEMY_DATABASE_URI variable (variable that stores the path to file that will hold the database so when the sqlalchemy is looking for a file to store the database, it goes to this URI)
# specify What database system you're using (e.g., SQLite, PostgreSQL, MySQL) and Where the database lives (a file path, server address, etc.)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db' #using sqlite and storing in a file called myDB.db

#we are setting another configuration variable to false
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #to supress warning


#the Flask-SQLAlchemy extension takes the location of the application’s database from the SQLALCHEMY_DATABASE_URI configuration variable so thats why we set it up above so it knows where it is
db = SQLAlchemy(app) #database instance


#declaring the Book model
class Book(db.Model):
    author_name = db.Column(db.String(50), unique = False) #looks like class variable but the formatting is acceptable because of metaclass 

class Reader(db.Model):
  name = db.Column(db.String(50), index = True, unique = False)
  surname = db.Column(db.String(80), index = True, unique = False)
  email = db.Column(db.String(120), index = True, unique = True)

#some routing for displaying the home page
@app.route('/')
@app.route('/home')
def home():
    return "Congrats! You have just created your first Flask application supporting databases!"
