# Air_Quality_Prediction

## Introduction:
  Machine Learning project to predict the Air Quality Index of a region. This is a guided project.
  
#### Data Collection:
  The explanatory variables are scrapped from en.tutiempo.net between the years 2013 to 2015.
  I have written a web scrapper function that scraps the data from the web and creates a HTML file for each month for the years 2013-2015
  
  ######  The Explanatory variables used:
    T-	Average Temperature (°C)
    
    TM-	Maximum temperature (°C)
    
    Tm-	Minimum temperature (°C)
    
    SLP-	Atmospheric pressure at sea level (hPa)
    
    H-	Average relative humidity (%)
    
    PP-	Total rainfall and / or snowmelt (mm)
    
    VV-	Average visibility (Km)
    
    V-	Average wind speed (Km/h)
    
    VM-	Maximum sustained wind speed (Km/h)
  
  
  The outcome variable is from a paid API and it was recorded hourly each day for all the years.
  
#### Data cleaning and Preprocessing:
The outcome variable was averaged for each day. The null and improper data was cleaned and then both the predictor variables and the outcome variable was combined together to 
create a csv file.

The missing values were dropped and the outliers were removed.

After preprocessing, the data was split into training and testing set. 

The model will learn the patterns from the training set and the testing set will be used to validate the model's performance.

#### Models:
I have tried various algorithms like Linear Regression, Decision Tree regressor and Random Forest Regressor and after hyperparameter tuning the Random Forest Regressor
performed the best out of the three models and therefore have used it to make the predictions.

The Coefficient of Determination(r2 score) is used as a accuracy measure for validating the model's performance.
