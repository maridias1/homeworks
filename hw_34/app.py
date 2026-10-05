from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# 1. ცხრილი books და ველები: id, title, author, year
class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'year': self.year
        }

# 2. /book - წიგნების დამატება (GET და POST)
@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        # მხარდაჭერა როგორც HTML ფორმისთვის, ასევე JSON-ისთვის
        if request.is_json:
            data = request.get_json()
            title = data.get('title')
            author = data.get('author')
            year = data.get('year')
        else:
            title = request.form.get('title')
            author = request.form.get('author')
            year = request.form.get('year')

        if not title or not author or not year:
            if request.is_json:
                return jsonify({'error': 'ყველა ველი სავალდებულოა!'}), 400
            flash('გთხოვთ შეავსოთ ყველა ველი!', 'danger')
            return redirect(url_for('book'))

        new_book = Book(title=title.strip(), author=author.strip(), year=int(year))
        db.session.add(new_book)
        db.session.commit()

        if request.is_json:
            return jsonify({'message': 'წიგნი წარმატებით დაემატა!', 'book': new_book.to_dict()}), 201

        flash('წიგნი წარმატებით დაემატა!', 'success')
        return redirect(url_for('book'))

    return render_template('create_book.html')

# 3. /update_book/<int:book_id> - წიგნის რედაქტირება
@app.route('/update_book/<int:book_id>', methods=['PUT', 'POST'])
def update_book(book_id):
    book_item = Book.query.get_or_404(book_id)
    data = request.get_json() if request.is_json else request.form

    if 'title' in data and data.get('title'):
        book_item.title = data.get('title').strip()
    if 'author' in data and data.get('author'):
        book_item.author = data.get('author').strip()
    if 'year' in data and data.get('year'):
        book_item.year = int(data.get('year'))

    db.session.commit()
    return jsonify({
        'message': f'წიგნი ID {book_id}-ით განახლდა!',
        'book': book_item.to_dict()
    }), 200

# 4. /get_book/<int:book_id> - კონკრეტული წიგნის მიღება (GET)
@app.route('/get_book/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book_item = Book.query.get_or_404(book_id)
    return jsonify(book_item.to_dict()), 200

# 5. /books - ყველა წიგნის მიღება (GET)
@app.route('/books', methods=['GET'])
def get_books():
    books_list = Book.query.all()
    return jsonify([b.to_dict() for b in books_list]), 200

# 6. /delete_book/<int:book_id> - წიგნის წაშლა (DELETE)
@app.route('/delete_book/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book_item = Book.query.get_or_404(book_id)
    db.session.delete(book_item)
    db.session.commit()
    return jsonify({'message': f'წიგნი ID {book_id}-ით წაიშალა წარმატებით!'}), 200

if __name__ == '__main__':
    app.run(debug=True)