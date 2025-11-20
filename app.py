import streamlit as st
import numpy as np
import pandas as pd
import joblib

# ---------------------------
# Load saved model and encoders
# ---------------------------
model = joblib.load("model.pkl")
label_encoders = joblib.load("label_encoders.pkl")

# ---------------------------
# Helper function to encode inputs
# ---------------------------
def encode_input(column_name, value):
    if column_name in label_encoders:
        return int(label_encoders[column_name].transform([value])[0])
    return value

# ---------------------------
# Streamlit UI
# ---------------------------
st.title("Meal Suggestion Predictor 🍽️")
st.write("Enter your details to get a personalized meal suggestion:")

# User inputs
age = st.selectbox("Age", ["18-20", "21-23", "23-26"])
gender = st.selectbox("Gender", ["Male", "Female"])
height = st.selectbox("Height (in feet and inch)", [
    "Below 5 feet 0 inches",
    "5 feet 0 inches – 5 feet 3 inches",
    "5 feet 4 inches – 5 feet 7 inches",
    "5 feet 8 inches – 5 feet 11 inches"
])
weight = st.selectbox("Weight (kg)", [
    "Below 45 kg (Potentially Underweight)",
    "45 kg – 55 kg",
    "56 kg – 65 kg",
    "66 kg – 75 kg",
    "76 kg or Above (Potentially Overweight/Obese)"
])
smoking = st.selectbox("Smoking Status", ["Yes", "No"])
residential = st.selectbox("Are you a residential student (living in a hall/hostel)?", ["Yes", "No"])
marital_status = st.selectbox("Marital Status", ["Unmarried", "Married"])
sleep_hours = st.selectbox("How much sleep did you get last night?", [
    "Low Sleep (Less than 5 hours)",
    "Moderate (5-6 hours)",
    "Optimal (7-8 hours)",
    "Excessive (9+ hours)"
])
stress_level = st.selectbox("How would you describe your current stress/anxiety level?", [
    "Low/Calm", "Moderate", "High/Exam Stress"
])
physical_activity = st.selectbox("Estimated physical activity level today", [
    "Sedentary (Mostly sitting/studying )",
    "Light (Walking to class/stairs)",
    "Moderate (Gym/Sports less than 60 mins)",
    "Vigorous (Sports more than 60 mins/Heavy labor)"
])
last_meal_time = st.selectbox("How long ago was your last proper meal?", [
    "Less than 2 hours ago",
    "2-4 hours ago",
    "4-6 hours ago (Optimal hunger)",
    "More than 6 hours ago (Skipped meal/High hunger)"
])
hunger_level = st.selectbox("Current feeling of hunger", [
    "Not hungry at all",
    "Slightly hungry",
    "Moderately hungry (Ready to eat)",
    "Very hungry (Feeling weak/distracted)"
])
skipped_meal = st.selectbox("Have you skipped a meal today?", [
    "No, I have not skipped a meal.",
    "Yes, I skipped Breakfast",
    "Yes, I skipped Lunch",
    "Yes, I skipped Dinner"
])
next_meal = st.selectbox("What meal are you likely to take next?", [
    "Breakfast", "Lunch", "Dinner"
])

# ---------------------------
# Prepare input for prediction
# ---------------------------
user_input = {
    "Age": age,
    "Gender": gender,
    "Height (in feet and inch)": height,
    "Weight (kg)": weight,
    "Smoking Status": smoking,
    "Are you a residential student (living in a hall/hostel)?": residential,
    "Marital Status": marital_status,
    "How much sleep did you get last night?": sleep_hours,
    "How would you describe your current stress/anxiety level?": stress_level,
    "What is your estimated physical activity level for today?": physical_activity,
    "How long ago was your last proper meal (e.g., breakfast)?": last_meal_time,
    "How would you rate your current feeling of hunger?": hunger_level,
    "Have you already skipped a meal today (Breakfast/Lunch/Dinner)?": skipped_meal,
    "What meal are you likely to take next?": next_meal
}

# Encode inputs
encoded_input = [encode_input(col, val) for col, val in user_input.items()]
input_array = np.array([encoded_input])

# ---------------------------
# Prediction
# ---------------------------
if st.button("Get Meal Suggestion 🍴"):
    prediction = model.predict(input_array)[0]
    st.success(f"Recommended Meal Suggestion: {prediction}")
