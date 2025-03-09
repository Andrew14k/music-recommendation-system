import os
from flask import Flask
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Get the database URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL", "mysql://root:rootpassword@db:3308/musicdb")
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL

db = SQLAlchemy(app)

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(255), nullable=False)
    genre = db.Column(db.String(255), nullable=False)
    song = db.Column(db.String(255), nullable=False)
    bpm = db.Column(db.Integer, nullable=False)
    topic = db.Column(db.String(255), nullable=False)

@app.route('/')
def index():
    songs = Song.query.all()
    return str(songs)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
