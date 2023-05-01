from random import randint

from flask import Flask

app = Flask(__name__)

constant = [1, 2, 3]

b = randint(0, 100)

constant.append(b)

del constant[-1]


@app.route("/")
def show_items():
    return f"<h3>Number of books: {constant}!!!<h3>"


@app.route("/add_item")
def add_item():
    return f"<h3>Number of books: {constant.append(b)}!!!<h3>"


@app.route("/delete_item")
def delete_item():
    return f"<h3>Number of books: {constant}!!!<h3>"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)



