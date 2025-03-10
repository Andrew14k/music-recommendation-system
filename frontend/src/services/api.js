const API_URL = 'http://localhost:5000'; // Adjust the URL based on your backend

export const getRecommendations = async (artist, genre, audioFile) => {
    const formData = new FormData();
    formData.append('artist', artist);
    formData.append('genre', genre);
    formData.append('audio', audioFile);

    const response = await fetch(`${API_URL}/recommendations`, {
        method: 'POST',
        body: formData,
    });

    if (!response.ok) {
        throw new Error('Failed to fetch recommendations');
    }

    return response.json(); // Assuming backend returns JSON with recommendations
};
