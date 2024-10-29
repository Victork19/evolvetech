from createDB import db_init, db
from flask_migrate import Migrate
from flask import Flask, render_template, request, url_for, flash


app = Flask(__name__,static_url_path='/static', static_folder='static')


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///event-site.db'

@app.route('/')
def home():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)