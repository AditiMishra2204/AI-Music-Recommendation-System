# 🎵 AI Music Recommendation System

An AI-powered Music Recommendation System built using Python, Scikit-Learn, and Streamlit. The system recommends similar songs based on song metadata such as artist, genre, and album using a content-based filtering approach.

## 🚀 Features

- Recommend top 5 similar songs
- Interactive Streamlit web interface
- Content-based recommendation engine
- Album artwork display
- Fast and user-friendly UI
- Machine Learning powered recommendations

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Streamlit
- Pickle
- CountVectorizer
- Cosine Similarity

## 📂 Project Structure

```text
MRS/
│
├── data/
│   └── ex.csv
│
├── scripts/
│   ├── app.py
│   ├── preprocess_data.py
│   └── models/
│       ├── musicrec.pkl
│       └── similarities.pkl
│
└── README.md
```

## ⚙️ How It Works

### 1. Data Collection
The dataset contains:
- Song Name
- Artist/Singer
- Genre
- Album/Movie

### 2. Feature Engineering

The following columns are combined into a single tags column:

```python
Song Name + Singer + Genre + Album
```

### 3. Vectorization

CountVectorizer converts text data into numerical vectors.

```python
CountVectorizer()
```

### 4. Similarity Calculation

Cosine Similarity is used to measure similarity between songs.

```python
cosine_similarity()
```

### 5. Recommendation

When a user selects a song:
- Similarity scores are calculated
- Songs are ranked
- Top 5 recommendations are displayed

## 🧠 Machine Learning Approach

This project uses:

- Content-Based Filtering
- CountVectorizer
- Cosine Similarity

Instead of predicting ratings, the system recommends songs based on metadata similarity.

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/AI-Music-Recommendation-System.git
```

Move into the project directory:

```bash
cd AI-Music-Recommendation-System
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run preprocessing:

```bash
python preprocess_data.py
```

Run the Streamlit application:

```bash
streamlit run app.py
```

## 📸 Application Preview

### Home Screen
- Select a song
- Click Recommend
- View similar songs with album artwork

## 🎯 Future Enhancements

- Spotify API Integration
- Mood-based recommendations
- User authentication
- Playlist generation
- Real-time music database
- Full-stack React + FastAPI version

## 👩‍💻 Author

**Aditi Mishra**

B.Tech Robotics & Artificial Intelligence

## ⭐ Project Highlights

- Machine Learning based recommendation engine
- Interactive Streamlit dashboard
- Real-world application of NLP techniques
- Beginner-friendly AI project
- Suitable for academic projects and resume showcase
