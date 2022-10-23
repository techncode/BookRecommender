from unicodedata import name
from flask import Flask, request
from flask import render_template
from book import Book
from redis_om import Migrator
import csv


app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/addbook")
def addbook():

    with open('bookdata.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                book = Book(
                    isbn = row[0],
                    title = row[1],
                    author = row[2],
                    year = row[3],
                    publisher = row[4]
                )

                book.save()
    return book.key()


@app.route("/booklist")
def getbooks():

    inputted_name = request.args['bookname']
    print("inputted_name = " + str(inputted_name))
    books = Book.find(Book.title % inputted_name).all()
    print(books)
    return render_template('booklist.html', bookname=books)

Migrator().run()

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')