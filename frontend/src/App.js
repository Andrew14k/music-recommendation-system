import React, { useState, useEffect } from "react";
import Home from "./components/Home";
import Results from "./components/Results";

function App() {
  const [recommendations, setRecommendations] = useState([]);

  useEffect(() => {
    // Fetch recommendations (you can replace this with actual logic)
    fetch("http://localhost:5000/artist=Drake") // Example endpoint
      .then((response) => response.json())
      .then((data) => setRecommendations(data))
      .catch((error) => console.error("Error fetching recommendations:", error));
  }, []);

  return (
    <div>
      <h1>Music Recommendation System</h1>
      <Home />
      {/* Pass recommendations as a prop to Results */}
      <Results recommendations={recommendations} />
    </div>
  );
}

export default App;
