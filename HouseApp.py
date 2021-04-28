import streamlit as st
import numpy as np
import pickle

model = pickle.load(open('model.pkl','rb'))

list_bhk_bath = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

def predict_price(total_sqft,bath,BHK,price_per_sqft):
    
    input=np.array([[total_sqft,bath,BHK,price_per_sqft]]).astype(np.float64)
    
    prediction=model.predict(input)
    return float(prediction)


def main():
    st.markdown("<h1 style='text-align: center; color: black;'>House Price Prediction</h1>", unsafe_allow_html=True)
    st.markdown("## Total Area (sq.ft.) : ")
    total_sqft = st.text_input("")
    st.markdown("## No. of bedrooms:  ")
    BHK = st.select_slider(" ", options=list_bhk_bath, key = "<uniquevalueofsomesort>")
    st.markdown("## No. of bathrooms:  ")
    bath = st.select_slider(" ", options=list_bhk_bath)
    st.markdown("## Price per sq.ft. : ")
    price_per_sqft = st.text_input(" ")
    

    if st.button("Predict (Price in Lakhs)"):
        output=predict_price(total_sqft,bath,BHK,price_per_sqft)
        st.success(round(output))
    
if __name__=='__main__':
    main()
