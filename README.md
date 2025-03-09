## Rebuilding previous dissertation project of same content - hence fast pushes/development
## 1 - Build project structure
Initialise git repository, create frontend, backend and database.
Set up dockerfile and docker compose configuration for containerisation.

## 2 - Set up database - MySQL
Design database schema and tables. 
Set up MySQL instance with docker.
Populate the database.

## 3 - Backend development - Python
Create REST API endpoints using Python and Flask (POST for inputs and GET for recommendations)
Set up MySQL connection (maybe use mysql-connector-python or SQLAlchemy)
Implement audio analysis - pydub or librosa for BPM analysis. For lyric analysis scrape lyrics if URL input (BeautifulSoup or APIs such as Genius)
Set up python script to handle input and return recommendations.

## 4 - Frontend development - React, HTML, CSS, JavaScript
Set up react app, and then build home page and results page for recommendations.
Use react state to manage input data and recommendations. Make AJAX/HTTP requests to backend to send inputs and recieve recommendations - use fetch() or a library such as axios.
Implement forms for artist name, genre and audio file uploads etc.

## 5 - Containerisation with Docker
create dockerfile for backend and frontend to build containers.
Set up docker-compose.yml to manage the full container setup. Will need frontend, backend and MySQL containers.
Ensure all components interact and test application works.

## 6 - Ensure all components are produced and integrated.
Implement error handling and loading states. 
Ensure frontend and backend interact correctly, with the user inputs being sent and recommendations sent.

## 7 - Testing
Unit testing, integration testing and user testing necessary.

## 8 - Deployment
Deploy backend - use AWS or Heroku.
Deploy frontend = use Netlify or Vercel
Ensure MySQL is hosted and accessible to the backend
Set up environment variables for production (API URLs, DB credentials).
