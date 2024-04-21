# 1. Pickling the Model
import pickle

# Save the trained model to a file
with open('model.pkl', 'wb') as file:
    pickle.dump(best_estimator, file)

# 2. Create a Streamlit App (app.py)
import streamlit as st
import pandas as pd
import pickle

# Load the pickled model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Define the Streamlit app
def main():
    st.title('Mobile Price Range Classifier')

    # User input for mobile features
    st.header('Enter Mobile Features:')
    # Add Streamlit components for user input (e.g., sliders, text input)

    # Make predictions based on user input
    if st.button('Predict'):
        # Get user input and preprocess it as necessary
        user_input = {}  # Example: {'battery_power': ..., 'ram': ..., ...}
        input_df = pd.DataFrame(user_input, index=[0])  # Convert to DataFrame

        # Make predictions
        prediction = model.predict(input_df)

        # Display the predicted price range
        st.success(f'Predicted Price Range: {prediction[0]}')

# 3. Deploy the Streamlit App
# Deploy the Streamlit app using a hosting platform like Heroku, Streamlit Sharing, or any other platform of your choice.

