## Mobile Price Range Classifier
![Phone Image](data/images/phot1_image.jpg)

### 1. Overview
This project aims to develop a machine learning model that can classify mobile phones into different price ranges based on their features. The dataset used contains information about various mobile phone specifications and corresponding price ranges. Selecting a mobile phone that aligns with one's budget and requirements can be challenging due to the wide range of options available in the market. This project addresses this challenge by building a predictive model to assist consumers in making informed decisions.

### 2. Dataset Description
The dataset comprises features such as battery power, camera specifications, memory, connectivity options, etc., along with the price range of mobile phones categorized into four classes: low cost, medium cost, high cost, and very high cost.

### 3. Methodology
1. **Data Exploration and Preprocessing**: Handle missing values, outliers, and inconsistencies in the dataset.
2. **Exploratory Data Analysis (EDA)**: Gain insights into the relationships between features and the target variable.
3. **Model Selection and Evaluation**: Choose appropriate machine learning algorithms for classification and evaluate their performance using accuracy metrics.
4. **Model Fine-tuning**: Fine-tune the chosen model to improve its predictive accuracy.
5. **Deployment**: Deploy the model for real-time predictions.

### 4. Conclusion and Recommendations
The Random Forest Classifier achieved the highest accuracy among the models evaluated, making it suitable for predicting mobile phone price ranges. However, continuous monitoring and updates are recommended to ensure the model's performance remains optimal.

### 5. Deployment
The deployed model is available [here](
https://mobile-price-classifier-yb95mfaklhsja2tjswhgq4.streamlit.app/ent_link).

### 6. Instructions for Running Locally
1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the Streamlit app using `streamlit run app.py`.
4. Access the app in your web browser at `http://localhost:8501`.

For more detailed instructions, refer to the deployment section in the notebook file in the repository.