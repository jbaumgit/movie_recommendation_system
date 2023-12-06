import numpy as np
import pandas as pd
import streamlit as st
from surprise import SVD
from surprise import Reader
from surprise import Dataset
reader = Reader(rating_scale=(1, 5))

# loading the dataframes
movies_df = pd.read_csv('data/movies.csv')
ratings_df = pd.read_csv('data/ratings.csv')
ratings_df = ratings_df.drop("timestamp", axis = 1)
movie_list20 = [ 356,  318,  296,  593, 2571,  260,  480,  110,  589,  527, 2959, 1, 1196, 2858,   50,   47,  780,  150, 1198, 4993]

# creating a function for Prediction

# return the top n recommendations using the 
def recommended_movies(user_ratings,movie_title_df,n):
    full_text = ""
    for idx, rec in enumerate(user_ratings):
        title = movie_title_df.loc[movie_title_df['movieId'] == int(rec[0])]['title']
        text = (str(title.values[0]) + '\n')
        full_text = full_text + "\n" + text
        n-= 1
        if n == 0:
            break
    return full_text


def rate_and_rec(user_rating, ratings_df, movies_df, genre=None):
    
    ## add the new ratings to the original ratings DataFrame
    user_ratings_df = pd.DataFrame(user_rating)
    ratings_df = pd.concat([ratings_df, user_ratings_df], axis=0)
    new_data = Dataset.load_from_df(ratings_df, reader)
    best_algo = SVD(n_factors= 200, n_epochs= 80, lr_all= 0.01, reg_all= 0.1)
    best_algo.fit(new_data.build_full_trainset())

    # make predictions for the user
    # you'll probably want to create a list of tuples in the format (movie_id, predicted_score)
    recc_movies = []
    for m_id in ratings_df['movieId'].unique():
        if (m_id in movie_list20): 
            continue
        else:
            prediction = best_algo.predict(1000,m_id)[3]
            recc_movies.append( (m_id, prediction) )
    
    # order the predictions from highest to lowest rated
    ranked_movies = sorted(recc_movies, key=lambda x:x[1], reverse = True)
    
    return recommended_movies(ranked_movies,movies_df,5)
  
    
  
def main():
    
    
    # giving a title
    st.title("Flix Finder")
    '''
    ## A Movie Recommender for FlixNet
    ### Rate these films from 1 to 5
    _If you haven't seen a film, leave the slider at 0_
    '''
    
    # getting the input data from the user

    Forrest = st.slider('Forrest Gump (1994)', min_value=0, max_value=5)
    Shawshank = st.slider('Shawshank Redemption, The (1994)', min_value=0, max_value=5)
    Pulp = st.slider('Pulp Fiction (1994)', min_value=0, max_value=5)
    Silence = st.slider('Silence of the Lambs, The (1991)', min_value=0, max_value=5)
    Matrix = st.slider('Matrix, The (1999)', min_value=0, max_value=5)
    Star = st.slider('Star Wars: Episode IV - A New Hope (1977)', min_value=0, max_value=5)
    Jurassic = st.slider('Jurassic Park (1993)', min_value=0, max_value=5)
    Braveheart = st.slider('Braveheart (1995)', min_value=0, max_value=5)
    Terminator = st.slider('Terminator 2: Judgment Day (1991)', min_value=0, max_value=5)
    Schindler = st.slider("Schindler's List (1993)", min_value=0, max_value=5)
    Fight = st.slider('Fight Club (1999)', min_value=0, max_value=5)
    Toy = st.slider('Toy Story (1995)', min_value=0, max_value=5)
    StarV = st.slider('Star Wars: Episode V - The Empire Strikes Back (1980)', min_value=0, max_value=5)
    Usual = st.slider('Usual Suspects, The (1995)', min_value=0, max_value=5)
    American = st.slider('American Beauty (1999)', min_value=0, max_value=5)
    Seven = st.slider('Seven (a.k.a. Se7en) (1995)', min_value=0, max_value=5)
    Independence = st.slider('Independence Day (a.k.a. ID4) (1996)', min_value=0, max_value=5)
    Apollo = st.slider('Apollo 13 (1995)', min_value=0, max_value=5)
    Raiders = st.slider('Raiders of the Lost Ark (Indiana Jones) (1981)', min_value=0, max_value=5)
    Lord = st.slider('Lord of the Rings: The Fellowship of the Ring, The (2001)', min_value=0, max_value=5)
        
    # code for Prediction
    recommendation = ''
    
    # creating a button for Prediction
    
    if st.button('Give Me Recommendations'):
        user_rating = [{'userId': 1000, 'movieId': 356, 'rating': Forrest}, 
                       {'userId': 1000, 'movieId': 318, 'rating': Shawshank},
                       {'userId': 1000, 'movieId': 296, 'rating': Pulp}, 
                       {'userId': 1000, 'movieId': 593, 'rating': Silence},
                       {'userId': 1000, 'movieId': 2571, 'rating': Matrix},
                       {'userId': 1000, 'movieId': 260, 'rating': Star}, 
                       {'userId': 1000, 'movieId': 480, 'rating': Jurassic},
                       {'userId': 1000, 'movieId': 110, 'rating': Braveheart}, 
                       {'userId': 1000, 'movieId': 589, 'rating': Terminator},
                       {'userId': 1000, 'movieId': 527, 'rating': Schindler}, 
                       {'userId': 1000, 'movieId': 2959, 'rating': Fight},
                       {'userId': 1000, 'movieId': 1, 'rating': Toy}, 
                       {'userId': 1000, 'movieId': 1196, 'rating': StarV},
                       {'userId': 1000, 'movieId': 2858, 'rating': Usual}, 
                       {'userId': 1000, 'movieId': 50, 'rating': American},
                       {'userId': 1000, 'movieId': 47, 'rating': Seven}, 
                       {'userId': 1000, 'movieId': 780, 'rating': Independence},
                       {'userId': 1000, 'movieId': 150, 'rating': Apollo}, 
                       {'userId': 1000, 'movieId': 1198, 'rating': Raiders},
                       {'userId': 1000, 'movieId': 4993, 'rating': Lord}]
        recommendation = rate_and_rec(user_rating, ratings_df, movies_df, genre=None)
        
    st.success(recommendation)
    
    
    
    
    
if __name__ == '__main__':
    main()