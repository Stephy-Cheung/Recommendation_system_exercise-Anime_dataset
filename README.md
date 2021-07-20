<img src="image/Banner.png" width="600">

# Exercise-Streamlit_Anime_dataset

## Objective
This is an exercise to develop an anime recommendation system. Recommendation will be made base on user favourite anime, user_id and similarity distance measure method. Streamlit will be used for app framework. <br>

'Recommend_app(streamlit)' is code for the Streamlit ap. <br>
'Preprocessing' is code for the pre-processing on dataset. <br>

Data is from kaggle dataset: https://www.kaggle.com/CooperUnion/anime-recommendations-database

## Pre-processing on dataset 
There is two data file in the dataset. <br>

'Anime.csv' contain the information of the anime, including the anime_id, name of anime, genre, type, rating and number of episodes. <br>

'Rating.csv' records the anime that watched by the user and the rating. Rating is marked as '-1' if user did not rate the anime. <br>

Three data file prepared to develop the streamlit application. 

### anime.csv
Contain basic information of the anime. Indexed by 'anime_id', followed by the name, genre and rating. <br>
<img src="image/anime_csv.png" width="800">

### anime_genre.csv
Data file generated from Anime.csv for similarity distance measure. Genre and type columns are One-Hot Encoded and rating is scaled to 0-1, indexed by 'anime_id'. <br>
<img src="image/anime_genre_csv.png" width="800">

### rating.csv
No preprocessing on this datafile.<br>
<img src="image/rating_csv.png" width="300">


## Application
User are able to input the below for recommendation. 
- Distance method
- Previous favourite anime
- Number of recommendation wanted
- user_id 

## Result:
Recommendations will be displaced according to ascending order of the similarity distance to user favourite anime. <br>

Anime that haven't been watched will be on top. <br>

Suggestion for re-watch will be at the bottom. <br>

<img src="image/Example.png" width="800">

## Next Step:
1. User Input: 
    Instead of input favourite anime, application can be modified to input parameters of preferred genre for more flexibility on the recommendation on anime. <br>

2. Rating:
    A content-based recommendation is used in this application as the data file has detailed genre and type information of each anime. On the other hand, the data file for individual rating is not completed as a lot of the users didn't rate the anime that they have watched (with a lot of value '-1'). A collaborative filtering recommendation can be develop if a more detailed rating data obtained from the users in the future. 

