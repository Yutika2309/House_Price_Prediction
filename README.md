# House Price Prediction:

Link to the web API: https://share.streamlit.io/yutika2309/house_price_prediction/main/HouseApp.py

# About:
* The data set used for the project is called "Bengaluru_House_Data.csv" from Kaggle.

* The data has been subjected to rigourous pre-processing hence the Linear Regression model produces an optimal R^2 value of 91%.

* This project was built using Streamlit. The web API involves the user entering 4 values namely: **Total Area**, **No. of Bedrooms**, **No. of Bathrooms** and **Price per sq. ft.**  in order for the Linear Regression model to predict the price of the house.

### Note:

* This API provides the output of house price in "Lakhs". So, e.g. "706 Lakhs" could be read as 7.06 crores. 

* It is advised to enter input values of bigger houses as opposed to smaller because the data set is in itself biased towards bigger values.

# Libraries used:

* Pandas -> 1.0.5

* Numpy -> 1.18.5

* Matplotlib -> 3.2.2

* Streamlit -> 0.70.0
