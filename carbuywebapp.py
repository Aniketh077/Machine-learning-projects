# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 13:57:04 2022

@author: Aniketh
"""

import numpy as np
import pickle
import streamlit as st


loaded_model = pickle.load(open('C:/Users/Aniketh/Desktop/ML A TO Z FULL/1.savedmodels/trained_model.sav','rb'))



# creating a function for Prediction

def carbuy_prediction(input_data):
    
    #changing input data to numpy array
    input_data_as_numpyarray = np.asarray(input_data)
    #reshape the array as we predicted for one instance
    input_data_reshaped = input_data_as_numpyarray.reshape(1,-1)
    prediction =loaded_model.predict(input_data_reshaped)
    print(prediction)
    if (prediction[0] == 0):
      return 'person not buy a car'
    else:
        return 'person bought  car'
    

  
    
  
def main():
    
    
    # giving a title
    st.title('Car Buy Prediction App')
    
    
    # getting the input data from the user
    
    
    Age = st.text_input('Enter The Age')
    EstimatedSalary = st.text_input('Enter the salary')
  
    
    
    # code for Prediction
    Purchased = ''
    
    # creating a button for Prediction
    
    if st.button('Enter For Result'):
        Purchased = carbuy_prediction([Age, EstimatedSalary])
        
        
    st.success(Purchased)
    
    
    
    
    
if __name__ == '__main__':
    main()