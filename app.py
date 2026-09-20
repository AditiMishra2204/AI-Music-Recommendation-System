import streamlit as st
st.set_page_config(
    page_title="AI Music Recommender",
    page_icon="🎵",
    layout="wide"
)
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import requests

# Load the preprocessed data
new_df = pickle.load(open('models/musicrec.pkl', 'rb'))
similarity = pickle.load(open('models/similarities.pkl', 'rb'))


# Function to get song details from Deezer (free, no API key needed)
def get_song_details(song_name):
    # Try Deezer first
    try:
        url = f"https://api.deezer.com/search?q={song_name}&limit=1"
        response = requests.get(url, timeout=10)
        data = response.json()
        if data.get('data') and len(data['data']) > 0:
            cover = data['data'][0]['album'].get('cover_big')
            if cover:
                return cover
    except Exception as e:
        print("Deezer error:", e)

    # Fallback: try iTunes
    try:
        url = f"https://itunes.apple.com/search?term={song_name}&limit=1&entity=song"
        response = requests.get(url, timeout=10)
        data = response.json()
        if data.get('results') and len(data['results']) > 0:
            cover = data['results'][0].get('artworkUrl100')
            if cover:
                # Get higher resolution version
                return cover.replace('100x100', '500x500')
    except Exception as e:
        print("iTunes error:", e)

    # Final fallback: reliable placeholder
    return "https://placehold.co/250x250/1DB954/white?text=No+Image"


# Define recommendation function
def recommend(song):
    song_index = new_df[new_df['title'] == song].index[0]
    distances = similarity[song_index]
    recommended_songs = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommendations = []
    for i in recommended_songs:
        song_name = new_df.iloc[i[0]].title
        song_poster = get_song_details(song_name)
        recommendations.append({'song_name': song_name, 'song_poster': song_poster})
    return recommendations


# Streamlit UI
st.markdown(
    "<h1 style='text-align:center;'>🎵 AI Music Recommendation System</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;'>Discover songs similar to your favorite tracks</p>",
    unsafe_allow_html=True
)
lmhol,l;;

selected_song = st.selectbox('Select a song:', new_df['title'].tolist())

if st.button('Recommend'):
    recommendations = recommend(selected_song)

    cols = st.columns(5)
    for i, song in enumerate(recommendations):
        with cols[i % 5]:
            st.write(f"**{song['song_name']}**")
            if song['song_poster']:
                st.image(song['song_poster'], use_container_width=True)
            else:
                st.write("🎵 No image available")
