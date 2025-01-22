import joblib
import numpy as np
import streamlit as st

# Load the model from the file
model = joblib.load('iris_model.pkl')

# Mapping of class labels to class names
class_names = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}

# Streamlit app
st.title('Iris Flower Prediction App')

# Input fields for user to enter data
sepal_length = st.number_input('Sepal Length', min_value=0.0, max_value=10.0, value=3.1)
sepal_width = st.number_input('Sepal Width', min_value=0.0, max_value=10.0, value=4.5)
petal_length = st.number_input('Petal Length', min_value=0.0, max_value=10.0, value=2.4)
petal_width = st.number_input('Petal Width', min_value=0.0, max_value=10.0, value=0.2)

# Button for making prediction
if st.button('Predict'):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)
    prediction_proba = model.predict_proba(input_data)
    predicted_class_name = class_names[prediction[0]]
    predicted_class_proba = prediction_proba[0][prediction[0]]

    st.write(f'Predicted class: {predicted_class_name}')
    st.write(f'Prediction probability: {predicted_class_proba:.2f}')

    # Display additional information about the predicted class
    if predicted_class_name == 'setosa':
        st.write('Setosa is a species of iris that is native to Japan.')
    elif predicted_class_name == 'versicolor':
        st.write('Versicolor is a species of iris that is native to North America.')
    elif predicted_class_name == 'virginica':
        st.write('Virginica is a species of iris that is native to the eastern United States.')