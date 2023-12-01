import numpy as np
import pandas as pd
import joblib
import streamlit as st
import base64

reg=joblib.load('bmw_model.pkl')

def predict_car_price(model,year,transmission,mileage,fuelType,tax,mpg,engineSize):
    prediction=reg.predict(pd.DataFrame({'model':[model],'year':[year],'transmission':[transmission],'mileage':[mileage],
                                          'fuelType':[fuelType],'tax':[tax],'mpg':[mpg],'engineSize':[engineSize]}))
    return prediction
def main():
    def add_bg_from_local(image_file):
        with open(image_file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        st.markdown(
        f"""
            <style>
            .stApp {{
                background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
                background-size: cover
            }}
            </style>
            """,
            unsafe_allow_html=True
            )
    add_bg_from_local("C:\\Users\\tasne\\Downloads\\bmw.jpg")  
     
    st.title('BMW Cars Price Estimation')
   # html_temp="""
            #  <div style="background-color:white">
            #  <h2 style="color:black;text-align:center;">Apply the features</h2>
             # </div>
              
            #  """         
    st.markdown(html_temp,unsafe_allow_html=True)
    model=st.selectbox('choose the model',['5 Series', '6 Series', '1 Series', '7 Series', '2 Series','4 Series', 'X3',
                                           '3 Series', 'X5', 'X4', 'i3', 'X1', 'M4', 'X2','X6', '8 Series', 'Z4', 'X7', 'M5', 'i8', 'M2', 
                                           'M3', 'M6', 'Z3'])
    year=st.selectbox('year',[2014, 2018, 2016, 2017, 2015, 2019, 2013, 2020, 2002, 2004, 2007,
       2008, 2011, 2012, 2009, 2006, 2010, 2003, 2001, 2005, 2000, 1999,
       1996, 1997, 1998])
    transmission=st.selectbox('choose transmission type',['Automatic', 'Manual', 'Semi-Auto'])
    mileage=st.text_input('mileage','write the mileage')
    fuelType=st.selectbox('fueltype',['Diesel', 'Petrol', 'Other', 'Hybrid', 'Electric'])
    tax=st.text_input('tax','enter the tax')
    mpg=st.text_input('mpg','enter mpg')
    engineSize=st.text_input('engine size','enter engine size')
    result=""
    if st.button('predict'):
        result=predict_car_price(model,year,transmission,mileage,fuelType,tax,mpg,engineSize)
    st.success('The car price is {} Euro'.format(result))
    
if __name__=="__main__":
    main()

