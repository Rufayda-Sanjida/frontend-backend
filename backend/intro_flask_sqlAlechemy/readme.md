database schema: the way a database is organized in entities, attributes and relationships, without data being present

Entities: objects (tables)
Attributes (noun): properties of entities (columns of tables); contrained to a type (ex. string or num or cannot be non)
Relationships (verb): represented as arrows when things are related


primary key column: uniquely identify entries in the table (all the indivuals of the people table)
foreign key column: represent references to the primary keys of other tables



models = classes that mirror the database tables 
entity/table = class
attributes = instance attributes
indivual entries in table (rows) = instances of class (object)

ex. book class has attribute and instance attribute of ID
now you can make many book objects and all these objects are simply rows in a table

the attributes are declared LIKE class variables but its not!! sqlAlchemy used metaclass to design a class to accept that!


1 to many relationship (syntax + concept explanation):

1️⃣ This line in the Review model:
python
Copy
Edit
reader_id = db.Column(db.Integer, db.ForeignKey('reader.id'))
🔗 This is the actual link that tells SQLAlchemy:

"Review is connected to the Reader table."

It means:

"This review belongs to one Reader, whose ID is stored here."

That’s how SQLAlchemy figures out how to join the tables.

2️⃣ This line in the Reader model:
python
Copy
Edit
reviews = db.relationship('Review', backref='reader')
🔍 This does two things:

Tells SQLAlchemy that:

"Reader is on the one side of a one-to-many relationship with Review"

Adds a review.reader attribute for reverse access — that’s what backref='reader' is for

✅ So Why Does It Work?
SQLAlchemy looks at:

All the ForeignKeys in the Review model

Sees that one of them (reader_id) points to reader.id

So when you say db.relationship('Review'), it uses that foreign key to link the two models

Then, when you add backref='reader', you’re just saying:

“Please also give me .reader on every review, so I can go backwards.”



making instances of classes = rows in table = instances
make it in a separate file