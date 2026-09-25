# 🚗 Car Price Prediction Using Machine Learning
## Major Project
This project predicts the selling price of used cars using Machine Learning regression algorithms.

## Dataset
CarDekho Vehicle Dataset from Kaggle.

## Machine Learning Algorithms
The project compares multiple regression algorithms:

- Linear Regression
- Ridge Regression
- Lasso Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- Extra Trees Regressor

## Evaluation Metrics
The models are evaluated using:

- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

## Features Used
- Manufacturing Year
- Kilometers Driven
- Fuel Type
- Seller Type
- Transmission
- Owner
- Car Age

## Streamlit Application
The trained model is integrated into a Streamlit web application where users can enter car details and receive an estimated selling price.

## Project Structure
```text
Car-Price-Prediction/
│
├── car_price_app.py
├── pipe.pkl
├── df.pkl
├── requirements.txt
└── README.md
