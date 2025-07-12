7. 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #to supress warning
db = SQLAlchemy(app)

#declaring the Book model
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
    return "Congrats! You have just initialized your database!"



3>
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #to supress warning
db = SQLAlchemy(app)

#declaring the Book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True) #primary key column, automatically generated IDs
    title = db.Column(db.String(80), index = True, unique = True) # book title
    author_name = db.Column(db.String(50), index = True, unique = False) #author name added
    author_surname = db.Column(db.String(80), index = True, unique = False) #author surname
    month = db.Column(db.String(20), index = True, unique = False) #the month of book suggestion
    year = db.Column(db.Integer, index = True, unique = False) #tthe year of boook suggestion
    
    #Get a nice printout for Book objects
    def __repr__(self):
        return "{} in: {},{}".format(self.title, self.month,self.year)


@app.route('/')
@app.route('/home')
def home():
    return "Congrats! You have just made your first Flask-SQLAlchemy model declaration!"



4. 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #to supress warning
db = SQLAlchemy(app)

#declaring the Book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True) #primary key column
    title = db.Column(db.String(80), index = True, unique = True) # book title
    author_name = db.Column(db.String(50), index = True, unique = False) #author name
    author_surname = db.Column(db.String(80), index = True, unique = False) #author surname
    month = db.Column(db.String(20), index = True, unique = False) #the month of the book suggestion
    year = db.Column(db.Integer, index = True, unique = False) #tthe year of the book suggestion
    
    #Get a nice printout for Book objects
    def __repr__(self):
        return "{} in: {},{}".format(self.title, self.month,self.year)

#Add your columns for the Reader model here below.
class Reader(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(50), index = True, unique = False)
  surname = db.Column(db.String(80), unique = False, index = True)
  email = db.Column(db.String(120), unique = True, index = True)
  
  #get a nice printout for Reader objects
  def __repr__(self):
      return "Reader: {}".format(self.email)




#some routing for displaying the home page
@app.route('/')
@app.route('/home')
def home():
    return "Congrats! You have just made a Flask-SQLAlchemy model declaration all by yourself!"



5. 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #to supress warning
db = SQLAlchemy(app)

#declaring the Book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True) #primary key column
    title = db.Column(db.String(80), index = True, unique = True) # book title
    author_name = db.Column(db.String(50), index = True, unique = False)
    author_surname = db.Column(db.String(80), index = True, unique = False) #author surname
    month = db.Column(db.String(20), index = True, unique = False) #the month of the book suggestion
    year = db.Column(db.Integer, index = True, unique = False) #the year of the book suggestion
    reviews = db.relationship('Review', backref = 'book', lazy = 'dynamic') #relationship of Books and Reviews
    
    #Get a nice printout for Book objects
    def __repr__(self):
        return "{} in: {},{}".format(self.title, self.month,self.year)

#Add your columns for the Reader model here below.
class Reader(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), index = True, unique = False)
    surname = db.Column(db.String(80), unique = False, index = True)
    email = db.Column(db.String(120), unique = True, index = True)
    reviews = db.relationship('Review', backref = 'reviewer', lazy = 'dynamic')
  
    #get a nice printout for Reader objects
    def __repr__(self):
        return "Reader: {}".format(self.email)


6.

#some routing for displaying the home page
@app.route('/')
@app.route('/home')
def home():
    return "Congrats! You are making your first one-to-many relationship in Flask-SQLAlchemy!"

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #to supress warning
db = SQLAlchemy(app)

#declaring the Book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True) #primary key column
    title = db.Column(db.String(80), index = True, unique = True) # book title
    author_name = db.Column(db.String(50), index = True, unique = False)
    author_surname = db.Column(db.String(80), index = True, unique = False) #author surname
    month = db.Column(db.String(20), index = True, unique = False) #the month of the book suggestion
    year = db.Column(db.Integer, index = True, unique = False) #the year of the book suggestion
    reviews = db.relationship('Review', backref = 'book', lazy = 'dynamic') #relationship of Books and Reviews
    
    #Get a nice printout for Book objects
    def __repr__(self):
        return "{} in: {},{}".format(self.title, self.month, self.year)

#Add your columns for the Reader model here below.
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
    id = db.Column(db.Integer, primary_key = True) #primary key column, automatically generated IDs
    stars = db.Column(db.Integer, unique = False) #a review's rating
    text = db.Column(db.String(200), unique = False) #a review's text
    #here below is the foreign key column linking to the primary key (id) of the Book model (book). 
    #Note the lower case here: 'book.id' instead of 'Book.id'
    book_id = db.Column(db.Integer, db.ForeignKey('book.id')) #foreign key column
    #your code here
    reviewer_id = db.Column(db.Integer, db.ForeignKey('reader.id'))
    #get a nice printout for Review objects
    def __repr__(self):
        return "Review: {} stars: {}".format(self.text, self.stars)


#some routing for displaying the home page
@app.route('/')
@app.route('/home')
def home():
    return "Congrats! You have just made a foreign key column in your Flask-SQLAlchemy model!"


8. 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #to supress warning
db = SQLAlchemy(app)

#declaring the Book model
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
    return "Congrats! You have just initialized your database!"
