import pandas as pd
import matplotlib.pyplot as plt
from pandas.io.parsers import read_csv
import seaborn as sns

import streamlit as st
from scipy.spatial.distance import euclidean, cityblock, cosine

# read data file
def get_data():
    anime = pd.read_csv('anime_data/anime.csv')
    anime=anime.set_index('anime_id')
    anime_genre = pd.read_csv('anime_data/anime_preprocessed.csv')
    anime_genre=anime_genre.set_index('anime_id')
    rating = pd.read_csv('anime_data/rating.csv')
    return anime, anime_genre, rating

# generate recommendation
def anime_recommender(distance, anime_id, N):
    # dataframe to store distance between animes 
    anime_distance = pd.DataFrame (data = anime_genre.index)

    # drop row of the input anime_id
    anime_distance = anime_distance[anime_genre.index != anime_id]

    # Calculate distance and store in distance columnm
    if distance == 'euclidean':
        anime_distance['distance'] = anime_distance['anime_id'].apply(lambda x: euclidean(anime_genre.loc[x],anime_genre.loc[anime_id]))
    elif distance == 'manhattan':
        anime_distance['distance'] = anime_distance['anime_id'].apply(lambda x: cityblock(anime_genre.loc[x],anime_genre.loc[anime_id]))
    elif distance == 'cosine':
        anime_distance['distance'] = anime_distance['anime_id'].apply(lambda x: cosine(anime_genre.loc[x],anime_genre.loc[anime_id]))
    anime_distance.sort_values(by='distance', inplace= True)
    
    return (anime_distance.head(N))

# print out anime information
def result(id):
    st.text('Title: ' + anime.loc[r, 'name']+ '      Rating: '+ str(anime.loc[r, 'rating']))
    st.text('Genre: '+ anime.loc[r, 'genre'])
    st.text(' ')


anime, anime_genre, rating = get_data()

st.title ('Anime Recommendation')
st.text ('This application will make anime recommendation')
st.text (' base on user previous favourite anime.')

# Sidebar - Obtain user input 
distance = st.sidebar.selectbox ('Distance method: ', ['euclidean','manhattan','cosine'])
anime_name = st.sidebar.selectbox('Previous Favourite : ',anime['name'].tolist())
num_re = st.sidebar.slider('Number of recommendation : ',min_value=1, max_value =10, step =1)
user_id = st.sidebar.number_input('Enter your user id: (key 0 if you are not a member)')

#Recommendation
st.title('Recommendation')
recommendation = anime_recommender(distance, anime[anime['name']==anime_name].index[0], num_re)

#Display result
# for first-time user 
if user_id not in rating['user_id']: 
    st.subheader('You may like the below animes...')
    for r in recommendation['anime_id']:
        result(r)

# for user with watching record
else: 
    watched = rating[rating['user_id']==user_id]
    st.subheader('You may like the below animes...')
    for r in recommendation['anime_id']:
        if r not in watched['anime_id']:
            result(r)

    st.subheader('You may also re-watched the below animes...')
    for r in recommendation['anime_id']:
        if r in watched['anime_id']:
            result(r)
