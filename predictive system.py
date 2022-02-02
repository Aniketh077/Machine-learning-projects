# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle


loaded_model = pickle.load(open('C:/Users/Aniketh/Desktop/ML A TO Z FULL/1.savedmodels/trained_model.sav','rb'))

input_data = (32,150000)
#changing input data to numpy array
input_data_as_numpyarray = np.asarray(input_data)
#reshape the array as we predicted for one instance
input_data_reshaped = input_data_as_numpyarray.reshape(1,-1)
prediction =loaded_model.predict(input_data_reshaped)
print(prediction)
if (prediction[0] == 0):
  print('person have not buy a car')
else:
    print('person bought a car')