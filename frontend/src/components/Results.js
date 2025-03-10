// src/components/Results.js
import React from "react";

const Results = ({ recommendations }) => {
  return (
    <div>
      <h2>Recommended Songs</h2>
      {recommendations && recommendations.length > 0 ? (
        <ul>
          {recommendations.map((item, index) => (
            <li key={index}>
              {item.artist} - {item.song}
            </li>
          ))}
        </ul>
      ) : (
        <p>No recommendations available</p>
      )}
    </div>
  );
};

export default Results;
