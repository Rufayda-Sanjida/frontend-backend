from app import db, Book, Reader, Review

reviews = Review.query.all()

#query word to get all the rows:
for review in reviews:
  print(review.text)
  
book_1 = Book.query.get(12)


#retrieving:
print("\nCheckpoint 1: fetch all the reviews made for a book with id = 13.")
#book_13 = 
#[print(book.id) for book in book_13]
book_13 = Book.query.get(13).reviews.all()

print("\nCheckpoint 2: fetch all the annotations made for a book with id = 19.")
book_19_an = Book.query.get(19).annotations.all()
#[print(annotation.id) for annotation in book_19_an]

