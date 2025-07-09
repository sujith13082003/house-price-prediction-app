# House Price Prediction App

This project is a machine learning-based web application that predicts the **selling price of houses** based on various input features like area, number of bedrooms, garage capacity, and year built. It is built using the **Kaggle House Prices - Advanced Regression Techniques** dataset and deployed via **Streamlit**.


## Dataset Source

- [Kaggle Competition: House Prices - Advanced Regression Techniques](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)
- File used: `train.csv`

##  Features

- Predicts house price based on user input
- Trained on Random Forest Regressor using cleaned and feature-engineered data
- Interactive web UI using Streamlit
- Model input and training features are kept consistent using saved column schema
- Ready for deployment or local use


##  Machine Learning Workflow

1. Data Cleaning & Feature Engineering (`notebooks/eda_and_modeling.ipynb`)
2. One-Hot Encoding for categorical features
3. Model Training with `RandomForestRegressor`
4. Evaluation using RMSE
5. Export model using `joblib`
6. Save feature columns to ensure consistent inputs
7. Streamlit UI for prediction using minimal inputs


##  Project Structure

house_price_prediction_app/
│
├── data/
│   └── train.csv
│
├── notebooks/
│   └── eda_and_modeling.ipynb
│
├── app.py                      # Streamlit web app
├── house_price_model.pkl      # Trained model
├── model_features.pkl         # Feature columns used during training
├── requirements.txt           # Python dependencies
├── README.md                  # Project overview


##  Future Enhancements

- Include more user input features for better prediction
- Improve UI styling
- Add model selector and explanation (e.g., SHAP or LIME)


##  License

This project is open source and free to use under the MIT License.


##  Author

** A.Sujith Kumar**  

