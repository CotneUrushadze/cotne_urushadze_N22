from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

Harry_potter = {"id": 1, "title": "Harry potter", "author": "J. K. Rowling", "year": "2001"}
America = {"id": 2, "title": "America", "author": "franz_kafka", "year": "1927"}

book_list = [Harry_potter, America]


@app.route('/')
def home():
    return render_template('index.html', book_list=book_list)


@app.route('/book/<book_id>')
def book(book_id):
    book_to_pass = {}
    for obj in book_list:
        if obj["id"] == int(book_id):
            book_to_pass = obj
    return render_template('book.html', book_id=int(book_id), book=book_to_pass)


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        book_id = request.form.get("id")
        title = request.form.get("title")
        author = request.form.get("author")
        year = request.form.get("year")

        new_book = {
            "id": book_id,
            "title": title,
            "author": author,
            "year": year
        }

        book_list.append(new_book)
        return redirect(url_for('home'))

    return render_template('add_book.html')


if __name__ == '__main__':
    app.run(debug=True)
