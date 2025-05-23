import pickle
import streamlit as st
import pandas as pd
import time
import base64
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommend_movies = []
    for i in movie_list:
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies

# Load preprocessed dataimport pickle
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

def set_background_image(image_file):
    with open(image_file, "rb") as file:
        encoded_string = base64.b64encode(file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set background image
set_background_image('image.jpg')

        # Custom CSS for styling
st.markdown("""
    <style>
        /* Background and layout styling */
        .stApp {
            background-color: #2e3b4e; 
            color: white;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        /* Styling the Title */
        .title {
            color: #FFFFFF;
            font-size: 40px;
            font-weight: 1000;
            text-align: center;
            background: linear-gradient(45deg, #3F3F4E, #9897A9);
            padding: 20px;
            border-radius: 10px;
        }

        /* Selectbox dropdown and Button Styling */
        .stSelectbox, .stButton {
            background: linear-gradient(45deg, #3F3F4E, #9897A9);
            color: white;
            font-weight: bold;
            padding: 15px 20px;
            border-radius: 10px;
            font-size: 16px;
        }

        /* Hover effects for buttons and dropdown */
        .stButton:hover, .stSelectbox:hover {
            background: linear-gradient(45deg,#C5C6D0, #696880);
            cursor: pointer;
        }

        /* Styling the movie recommendations */
        .recommendation {
            font-size: 22px;
            color: #FF6347;
            font-weight: 600;
            margin-top: 30px;
            text-align: center;
        }

        .movie-card {
            background-color: #FBFAF2;
            border-radius: 10px;
            padding: 15px;
            margin: 10px 0;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .movie-card:hover {
            transform: scale(1.05);
            box-shadow: 0 8px 12px rgba(0, 0, 0, 0.2);
        }

        .movie-title {
            font-size: 24px;
            font-weight: 800;
            color: #030001;
        }

        .movie-description {
            font-size: 16px;
            color: #030001;
        }

        .loading {
            color: #030001;
            font-size: 18px;
            font-weight: 600;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)


# Streamlit interface with customized title and buttons
st.markdown('<p class="title">🎬 Movie Recommendation System</p>', unsafe_allow_html=True)

# Dropdown to select movie
selected_movie_name = st.selectbox('Select a movie:', movies['title'].values)

if st.button('Recommend'):
    # Show a loading spinner while recommending
    with st.spinner('Generating recommendations...'):
        time.sleep(2)  # Simulate some processing time (optional)

        # Get recommendations
        recommendation = recommend(selected_movie_name)
        st.markdown('<p class="recommendation">Recommended Movies:</p>', unsafe_allow_html=True)

        # Display recommendations with custom styling
        for i, movie in enumerate(recommendation):
            st.markdown(f"""
                <div class="movie-card">
                    <p class="movie-title">{i + 1}. {movie}</p>
                    <p class="movie-description">A fantastic movie you will love!</p>  <!-- You can add descriptions here -->
                </div>
            """, unsafe_allow_html=True)