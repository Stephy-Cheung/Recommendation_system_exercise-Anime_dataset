<img src="img/Example.png" width="600">

# Exercise-Streamlit_Anime_dataset

## Objective
This is an exercise to develop an anime recommendation app on Streamlit. Recommendation will be made base on user favourite anime, user_id and similarity distance measure method. <br>

'Recommend_app(streamlit)' is code for the Streamlit ap. <br>
'Preprocessing' is code for the pre-processing on dataset. <br>

Data is from kaggle dataset: https://www.kaggle.com/CooperUnion/anime-recommendations-database

## Pre-processing on dataset 
There is two data file in this dataset. <br>

'Anime.csv' contain the information of the anime, including the anime_id, name of anime, genre, type, rating and number of episodes. <br>

'Rating.csv' records the anime that watched by the user and the rating. Rating is marked as '-1' if user did not rate the anime. <br>

Three data file prepared for the streamlit app. 

### anime.csv
Contain basic details of the anime. Index by 'anime_id', followed by the name, genre and rating. 
<img src="" width="600">

### anime_genre.csv
Datafile generated from Anime.csv for similarity distance measure. Genre and typ columns are One-Hot Encoded and rating is scaled to 0-1, index by 'anime_id'.
<img src="" width="600">

### rating.csv
No preprocessing on this datafile.
<img src="" width="600">


## Application
User are able to input the below for recommendation. 
- Distance method
- Previous favourite anime
- Number of recommendation wanted
- user_id 

## Result:
Recommendations that haven't been watched by user will show on the first part and followed by recommendation for the re-watch as the second part. The print out order is according to the similarity distance of user favourite anime.
<img src="image/Example.png" width="400">

## Next Step:
1. User Input: 
    Instead of input guest favourite anime, the input parameters can be changed to the preferred genre for more flexibility on the selection on anime. 

2. Rating:
    A content-based recommendation is used in this application as the genre and type of anime is completed, while there is large among of missing values in the rating.csv. A lot of the users didn't rate the anime that they have watched. A collaborative filtering recommendation can be develop if a more completed rating data obtained in the future.

