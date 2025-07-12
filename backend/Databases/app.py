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


class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True) #primary key column
    title = db.Column(db.String(80), index = True, unique = True) 
    author_name = db.Column(db.String(50), index = True, unique = False)
    author_surname = db.Column(db.String(80), index = True, unique = False) 
    month = db.Column(db.String(20), index = True, unique = False) 
    year = db.Column(db.Integer, index = True, unique = False) 
    reviews = db.relationship('Review', backref = 'book', lazy = 'dynamic') 
    
    #Get a nice printout for Book objects
    def __repr__(self):
        return "{} in: {},{}".format(self.title, self.month, self.year)

#Declaring the Reader model
class Reader(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), index = True, unique = False)
    surname = db.Column(db.String(80), unique = False, index = True)
    email = db.Column(db.String(120), unique = True, index = True)
    reviews = db.relationship('Review', backref='reviewer', lazy = 'dynamic')
  
    #get a nice printout for Reader objects
    def __repr__(self):
        return "Reader: {}".format(self.email)

#declaring the Review model
class Review(db.Model):
    id = db.Column(db.Integer, primary_key = True) #primary key column, 
    stars = db.Column(db.Integer, unique = False) #a review's rating
    text = db.Column(db.String(200), unique = False) #a review's text
    book_id = db.Column(db.Integer, db.ForeignKey('book.id')) #foreign key 
    reviewer_id = db.Column(db.Integer, db.ForeignKey('reader.id'))

    #get a nice printout for Review objects
    def __repr__(self):
        return "Review: {} stars: {}".format(self.text, self.stars)




#some routing for displaying the home page
@app.route('/')
@app.route('/home')
def home():
    return "Congrats! You have just created your first Flask application supporting databases!"


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
