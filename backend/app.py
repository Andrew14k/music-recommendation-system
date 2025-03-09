import os
from flask import Flask, render_template, request, jsonify
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import librosa
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

# Get the database URL from environment variables
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:rootpassword@db/musicdb'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Song(db.Model):
    __tablename__ = 'songs'
    id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(255), nullable=False)
    genre = db.Column(db.String(255), nullable=False)
    song = db.Column(db.String(255), nullable=False)
    bpm = db.Column(db.Integer, nullable=False)
    topic = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Song {self.id} - {self.song}>"

@app.route('/')
def index():
    songs = Song.query.all()
    songs = Song.query.all()
    return render_template('index.html', songs=songs)

@app.route('/', methods=['POST'])
def add_song():
    try:
        data = request.get_json()
        artist_name = data.get('artist_name')
        genre = data.get('genre')
        song = data.get('song')
        bpm = data.get('bpm')
        topic = data.get('topic')

        if not artist_name or not genre or not song or not bpm or not topic:
            return jsonify({"error": "Missing fields in the request"}), 400

        new_song = Song(
            artist_name=artist_name, 
            genre=genre, 
            song=song, 
            bpm=bpm, 
            topic=topic
        )

        db.session.add(new_song)
        db.session.commit()

        return jsonify({
            "id": new_song.id,
            "artist_name": new_song.artist_name,
            "genre": new_song.genre,
            "song": new_song.song,
            "bpm": new_song.bpm,
            "topic": new_song.topic
        }), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/', methods=['GET'])
def recommend_song():
    # Extract query parameters from the GET request
    genre = request.args.get('genre')
    bpm = request.args.get('bpm', type=int)
    topic = request.args.get('topic')
    
    # Query the database for songs matching the criteria
    query = Song.query
    if genre:
        query = query.filter(Song.genre == genre)
    if bpm:
        query = query.filter(Song.bpm == bpm)
    if topic:
        query = query.filter(Song.topic == topic)
    
    songs = query.all()
    
    # Return the result as a JSON response
    songs_list = [{"artist": song.artist, "song": song.song, "bpm": song.bpm, "topic": song.topic} for song in songs]
    
    return jsonify(songs_list)

def analyze_bpm_librosa(audio_file_path):
    y, sr = librosa.load(audio_file_path)
    tempo, _ = librosa.beat.beat_track(y, sr=sr)
    return tempo

def get_lyrics_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # This is a basic example; adjust it based on the website structure
    lyrics = soup.find("div", class_="lyrics").get_text()
    
    return lyrics

@app.route('/recommend_song', methods=['POST'])
def recommend_song_post():
    data = request.get_json()
    
    # Extract song URL or file path from the request
    song_url = data.get('song_url')
    bpm = None

    # If it's a URL to an audio file, analyze its BPM
    if song_url.endswith(".mp3"):
        bpm = analyze_bpm_librosa(song_url)
    elif song_url.endswith(".wav"):
        bpm = analyze_bpm_librosa(song_url)
    
    # If the URL is for lyrics scraping (use the Genius API or BeautifulSoup)
    lyrics = None
    if "genius.com" in song_url:
        lyrics = get_lyrics_from_url(song_url)
    else:
        lyrics = get_lyrics_from_url(song_url)
    
    # Insert the data into the DB or use it for recommendation logic
    
    recommendations = recommend_song()  # Use the GET logic for song recommendations
    
    return jsonify({'recommendations': recommendations})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
