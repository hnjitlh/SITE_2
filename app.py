from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return render_template('pages/index.html')


if __name__ == '__main__':
    app.run()
