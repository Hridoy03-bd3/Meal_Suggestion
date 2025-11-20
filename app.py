# app.py

import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('random_forest_model.pkl')

st.title("🍽️ Meal Suggestion Predictor")
st.write("Enter your details below to get a personalized meal suggestion:")

# User-friendly inputs
age_map = {"18-20":0, "21-23":1, "23-26":2}
gender_map = {"Female":0, "Male":1, "Other":2}
height_map = {
    "Below 5 feet 0 inches":0,
    "5 feet 0 inches – 5 feet 3 inches":1,
    "5 feet 4 inches – 5 feet 7 inches":2,
    "5 feet 8 inches – 5 feet 11 inches":3,
    "Above 6 feet":4
}
weight_map = {
    "Below 45 kg":0,
    "45-55 kg":1,
    "56-65 kg":2,
    "66-75 kg":3,
    "76 kg or Above":4
}
smoking_map = {"No":0, "Yes":1, "Occasionally":2, "Used to":3, "Prefer not to say":4}
residential_map = {"No":0, "Yes":1}
marital_map = {"Unmarried":0, "Married":1}
sleep_map = {
    "Low (<5 hours)":0,
    "Moderate (5-6 hours)":1,
    "Optimal (7-8 hours)":2,
    "Excessive (9+ hours)":3
}
stress_map = {
    "Low/Calm":0,
    "Moderate":1,
    "High/Exam Stress":2,
    "Very High":3
}
activity_map = {
    "Sedentary (Mostly sitting/studying)":0,
    "Light (Walking to class/stairs)":1,
    "Moderate (Gym/Sports <60 mins)":2,
    "Vigorous (Sports >60 mins/Heavy labor)":3
}
last_meal_map = {
    "Less than 2 hours ago":0,
    "2-4 hours ago":1,
    "4-6 hours ago":2,
    "More than 6 hours ago":3
}
hunger_map = {
    "Not hungry at all":0,
    "Slightly hungry":1,
    "Moderately hungry":2,
    "Very hungry":3
}
skipped_map = {
    "No":0,
    "Yes, I skipped Breakfast":1,
    "Yes, I skipped Lunch":2,
    "Yes, I skipped Dinner":3,
    "Yes, I skipped multiple meals":4
}

# Streamlit inputs
age = st.selectbox("Age", list(age_map.keys()))
gender = st.selectbox("Gender", list(gender_map.keys()))
height = st.selectbox("Height", list(height_map.keys()))
weight = st.selectbox("Weight", list(weight_map.keys()))
smoking = st.selectbox("Smoking Status", list(smoking_map.keys()))
residential = st.selectbox("Are you a residential student?", list(residential_map.keys()))
marital = st.selectbox("Marital Status", list(marital_map.keys()))
sleep = st.selectbox("How much sleep did you get last night?", list(sleep_map.keys()))
stress = st.selectbox("Current stress/anxiety level", list(stress_map.keys()))
activity = st.selectbox("Physical activity level today", list(activity_map.keys()))
last_meal = st.selectbox("How long ago was your last proper meal?", list(last_meal_map.keys()))
hunger = st.selectbox("Current hunger level", list(hunger_map.keys()))
skipped_meal = st.selectbox("Have you skipped a meal today?", list(skipped_map.keys()))

# Prepare input dataframe for the model
input_data = pd.DataFrame({
    'Age':[age_map[age]],
    'Gender':[gender_map[gender]],
    'Height':[height_map[height]],
    'Weight':[weight_map[weight]],
    'Smoking Status':[smoking_map[smoking]],
    'Are you a residential student (living in a hall/hostel)?':[residential_map[residential]],
    'Marital Status':[marital_map[marital]],
    'How much sleep did you get last night?':[sleep_map[sleep]],
    'How would you describe your current stress/anxiety level?':[stress_map[stress]],
    'What is your estimated physical activity level for today?':[activity_map[activity]],
    'How long ago was your last proper meal (e.g., breakfast)?':[last_meal_map[last_meal]],
    'How would you rate your current feeling of hunger?':[hunger_map[hunger]],
    'Have you already skipped a meal today (Breakfast/Lunch/Dinner)?':[skipped_map[skipped_meal]]
})

# Prediction
if st.button("Get Meal Suggestion"):
    prediction = model.predict(input_data)
    st.success(f"🍽️ Predicted Meal Suggestion: {prediction[0]}")

