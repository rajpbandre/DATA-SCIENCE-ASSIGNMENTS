# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 17:08:00 2024

@author: 91762
"""

import pickle
import streamlit as st

# open model in read binary mode
load = open('clf.pkl','rb')
model = pickle.load(load)


# Define predict function
def predict(preg,plas,pres,skin,test,mass,pedi,age):
    prediction = model.predict([[preg,plas,pres,skin,test,mass,pedi,age]])
    # pass arguments in 2 dimensions using 2 square brackets
    return prediction

def main():
    st.title('Pima Indian Diabetes')
    # Accept values from user through browser
    preg = st.number_input('Pregnancy: ')
    plas = st.number_input('Plasma: ')
    pres = st.number_input('Pres: ')
    skin = st.number_input('Skin: ')
    test = st.number_input('Test: ')
    mass = st.number_input('Mass: ')
    pedi = st.number_input('Pedigree: ')
    age = st.number_input('Age: ')
    
    if st.button('Predict'): 
        result = predict(preg,plas,pres,skin,test,mass,pedi,age)
        if result==0:
            st.success("Non-Diabetic Person")
        else:
            st.success("Diabetic Person")
            
            
            
if __name__ == '__main__':
    main()           