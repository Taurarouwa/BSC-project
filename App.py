import streamlit as st
import pickle
import pandas as pd

with open('Pickle Saving.pkl','rb') as mod:
    model = pickle.load(mod)
    
st.image('car2.jpg')
st.title('Car Price Predictor')
st.write('A model to predict car prices')  

def input_var():
    # year = st.number_input('Year',min_value=1980, max_value=2030,value=2025)
    year = st.selectbox('Year', (range(2005, 2050)))      
    kms_driven = st.number_input('KMS Driven')
    present_price = st.number_input('Present Price (₦)')  
    
    owner_check = st.selectbox('Status',('Used Car','Brand New'))
    owner = 0 if owner_check == 'Brand New' else 1
    
    fuel_type = st.selectbox('Fuel Type',('Diesel','Petrol','CNG'))
    fuel_type_diesel = 1 if fuel_type == 'Diesel' else 0
    fuel_type_petrol = 1 if fuel_type == 'Petrol' else 0
    
    seller_type_check = st.selectbox('Seller Type',('Dealer','Individual'))
    seller_type = 1 if seller_type_check == 'Dealer' else 0
    
    transmission = st.selectbox('Transmission Type',('Automatic','Manual'))
    transmission_auto = 1 if transmission == 'Automatic' else 0
    
    data = {
        'Year': year,
        'Present_Price':present_price / 1500,
        'Kms_Driven':kms_driven,
        'Owner':owner,
        'Fuel_Type_Diesel':fuel_type_diesel,
        'Fuel_Type_Petrol':fuel_type_petrol,
        'Seller_Type_Dealer':seller_type,
        'Transmission_Automatic':transmission_auto
    }
    data_input = pd.DataFrame(data, index=[0])
    return data_input

user_input = input_var()
# st.subheader('User Input Features')
# st.write(user_input)

if st.button('Predict Price'):
    prediction = model.predict(user_input)
    predictions = prediction * 1500

    st.subheader('The Predicted Price Will Be:')
    st.success(f'₦{round(predictions[0],2)}')

# if __name__ == '__main__':
    # input_var()