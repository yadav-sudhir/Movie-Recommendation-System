# Movie Recommendation System

## Description
This project is a simple movie recommendation system built with Python and Streamlit. It recommend similar movies based on the user's selection, utilizing a content-based filtering approach.

## Features
- Interactive web interface using Streamlit
- Recommends 5 similar movies based on user's choice
- Uses pre-computed similarity matrix for efficient recommendations

## Installation
1. Clone the repository
2. Navigate to the project directory

## Usage
1. Run the Streamlit app
2. Open your web browser and go to the address shown in the terminal (usually http://localhost:8501)
3. Select a movie from the dropdown list and click 'Recommend' to get similar movie suggestions

## How it Works
1. The system loads a pre-computed list of movies and a similarity matrix
2. When a user selects a movie, the system finds its index in the movie list
3. It then retrieves the similarity scores for that movie from the similarity matrix
4. The top 5 most similar movies are selected and displayed as recommendations

## Files
- `app.py`: Main application file containing the Streamlit interface and recommendation logic
- `movies.pkl`: Pickle file containing the list of movies
- `similarity.pkl`: Pickle file containing the pre-computed similarity matrix

## Technologies Used
- Python
- Streamlit
- Pickle (for data loading)

## Future Improvements
- Implement user-based collaborative filtering
- Add movie posters and additional information to recommendations
- Improve the UI/UX of the application

## Contributing
Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/your-username/Movie-Recommendation-System/issues) if you want to contribute.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
