import numpy as np
import pickle
import streamlit as st


# loading the saved model
#loaded_model = pickle.load(open('trained_model.sav', 'rb'))


# creating a function for Prediction

def movie_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    return 
  
    
  
def main():
    
    
    # giving a title
    st.title('Movie Recommendation Web App')
    st.text("Rate these films from 1 to 5")
    
    # getting the input data from the user

    Forrest = st.text_input('Forrest Gump (1994)')
    Shawshank = st.text_input('Shawshank Redemption, The (1994)')
    Pulp = st.text_input('Pulp Fiction (1994)')
    Matrix = st.text_input('Matrix, The (1999)')
    Star = st.text_input('Star Wars: Episode IV - A New Hope (1977)')
    Jurassic = st.text_input('Jurassic Park (1993)')
    Braveheart = st.text_input('Braveheart (1995)')
    Terminator = st.text_input('Terminator 2: Judgment Day (1991)')
    Schindler = st.text_input("Schindler's List (1993)")
    Fight = st.text_input('Fight Club (1999)')
    Toy = st.text_input('Toy Story (1995)')
    StarV = st.text_input('Star Wars: Episode V - The Empire Strikes Back (1980)')
    Usual = st.text_input('Usual Suspects, The (1995)')
    American = st.text_input('American Beauty (1999)')
    Seven = st.text_input('Seven (a.k.a. Se7en) (1995)')
    Independence = st.text_input('Independence Day (a.k.a. ID4) (1996)')
    Apollo = st.text_input('Apollo 13 (1995)')
    Raiders = st.text_input('Raiders of the Lost Ark (Indiana Jones) (1981)')
    Lord = st.text_input('Lord of the Rings: The Fellowship of the Ring, The (2001)')
        
    # code for Prediction
    recommendation = ''
    
    # creating a button for Prediction
    
    if st.button('Give Me Recommendations'):
        recommendation = movie_prediction([Forrest, Shawshank, Pulp, Matrix, 
                                           Star, Jurassic, Braveheart, Terminator, 
                                           Schindler, Fight, Toy, StarV, Usual, 
                                           American, Seven, Independence, Apollo, 
                                           Raiders, Lord])
        
        
    st.success(recommendation)
    
    
    
    
    
if __name__ == '__main__':
    main()