import React, { useState, useEffect } from "react";

const Home = () => {
  const [songs, setSongs] = useState([]);

  useEffect(() => {
    // Fetch data from the backend API
    fetch("http://localhost:5000")  // Replace with actual backend URL if needed
      .then(response => response.json())
      .then(data => setSongs(data))
      .catch(error => console.error("Error fetching songs:", error));
  }, []);

  return (
    <div>
      <h2>Home</h2>
      <p>Testing content</p>
      <ul>
        {songs.length > 0 ? (
          songs.map((song, index) => (
            <li key={index}>{song.artist} - {song.song}</li>
          ))
        ) : (
          <p>Loading songs...</p>
        )}
      </ul>
    </div>
  );
};

export default Home;
