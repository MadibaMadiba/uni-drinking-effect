import streamlit as st
import pickle
import pandas as pd

filename = 'assets/knn.pkl'
with open(filename, 'rb') as file:
    gpa_pred = pickle.load(file)

st.set_page_config(
    layout="centered",
    page_title="Home",
    page_icon=":champagne:",
    initial_sidebar_state="collapsed"
)

st.title("GPA Prediction")

sex0 = st.radio("Gender", ["Male", "Female"])
sex = 0 if sex0 == "Male" else 1

study_year_input = st.selectbox("Study Year",
    ["1st Year", "2nd Year", "3rd Year", "4th Year", "Post Graduate"])
study_year_mapping = {"1st Year": 0, "2nd Year": 1, "3rd Year": 2, "4th Year": 3, "Post Graduate": 4}
study_year = study_year_mapping[study_year_input]

faculty_input = st.selectbox("Faculty",
    ["AgriSciences", "Arts & Social Sciences", "Economic & Management Sciences ", "Education", "Engineering", "Law", "Medicine and Health Services", "Science"])
faculty_mapping = {"AgriSciences": 0, "Arts & Social Sciences": 1, "Economic & Management Sciences ": 2, "Education": 3, "Engineering": 4, "Law": 5, "Medicine and Health Services": 6, "Science": 7}
faculty = faculty_mapping[faculty_input]

accomodation_input = st.radio("Accomodation", ["Private", "Non-private"])
accomodation = 1 if accomodation_input == "Private" else 0

allowance_input = st.selectbox("Monthly Allowance",
    ["Ksh 30k - 35k", "Ksh 36k - 42k", "Ksh 43k - 50k", "Ksh 51k - 57k", "Ksh 57k+"])
allowance_mapping = {"Ksh 30k - 35k": 0, "Ksh 36k - 42k": 1, "Ksh 43k - 50k": 2, "Ksh 51k - 57k": 3, "Ksh 57k+": 4}
allowance = allowance_mapping[allowance_input]

scholarship_input = st.radio("Scholarship?", ["No", "Yes"])
scholarship = 1 if scholarship_input == "Yes" else 0

weekly_study_hrs_input = st.select_slider("Weekly study hours", 
    [0, "1-3", "3-5", "5-8", "8+"], 0)
weekly_study_hrs_mapping = {0: 0, "1-3": 1, "3-5": 2, "5-8": 3, "8+": 4}
weekly_study_hrs = weekly_study_hrs_mapping[weekly_study_hrs_input]

socializing_freq_input = st.selectbox("Days spent socializing per week", 
    [0, 1, "Only Weekends", 2, 3, "4+"], 0)
socializing_freq_mapping = {0: 0, 1: 1, 2: 2, 3: 3, "4+": 4, "Only Weekends": 5}
socializing_freq = socializing_freq_mapping[socializing_freq_input]

drinks_per_night_input = st.select_slider("Drinks per night", 
    [0, "1-3", "3-5", "5-8", "8+"], 0)
drinks_per_night_mapping = {0: 0, "1-3": 1, "3-5": 2, "5-8": 3, "8+": 4}
drinks_per_night = drinks_per_night_mapping[drinks_per_night_input]

missed_classes_input = st.select_slider("Missed classes", 
    [0, 1, 2, 3, "4+"], 0)
missed_classes_mapping = {0: 0, 1: 1, 2: 2, 3: 3, "4+": 4}
missed_classes = missed_classes_mapping[missed_classes_input]

failed_modules_input = st.select_slider("Failed modules", 
    [0, 1, 2, 3, "4+"], 0)
failed_modules_mapping = {0: 0, 1: 1, 2: 2, 3: 3, "4+": 4}
failed_modules = failed_modules_mapping[failed_modules_input]

relationship_input = st.radio("Are you in a relationship?", ["Yes", "No"])
relationship = 0 if relationship_input == "Yes" else 1

approval_input = st.radio("Do your parents approve of youu drinking alcohol?", ["Yes", "No"])
approval = 0 if approval_input == "Yes" else 1

parent_strength_input = st.selectbox("How is your relationship with your parents?", 
    ["Distant", "Fair", "Close", "Very Close"])
parent_strength_mapping = {"Distant": 3, "Fair": 2, "Close": 1, "Very Close": 0}
parent_strength = parent_strength_mapping[parent_strength_input]

# Create a DataFrame with all the input features
input_data = pd.DataFrame({
    'sex': [sex],
    'study_year': [study_year],
    'faculty': [faculty],
    'accomodation': [accomodation],
    'allowance': [allowance],
    'scholarship': [scholarship],
    'weekly_study_hrs': [weekly_study_hrs],
    'socializing_freq': [socializing_freq],
    'drinks_per_night': [drinks_per_night],
    'missed_classes': [missed_classes],
    'failed_modules': [failed_modules],
    'relationship': [relationship],
    'approval': [approval],
    'parent_strength': [parent_strength]
})

if st.button("Run"):
    gpa_prediction = gpa_pred.predict(input_data)[0]
    st.success(f"Based on the information provided your predicted GPA is {gpa_prediction}")
