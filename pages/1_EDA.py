import streamlit as st
# import pandas as pd

st.set_page_config(
    layout="centered",
    page_title="EDA",
    page_icon=":writing_hand:",
    initial_sidebar_state="collapsed"
)

st.title('Somewhat noteable things')

st.header('Percentage of drinkers by volume')
st.image('assets/images/drinkers_pie.png')

st.header('Data correlation heatmap')
st.image('assets/images/heatmap.png')

st.header('Lowest and Highest GPA in each drinking bracket')
st.image('assets/images/min_max_gpa.png')

st.header('Average and Median GPA in each drinking bracket')
st.image('assets/images/avg_median_gpa.png')

st.header('Average and Highest GPA per study hour bracket')
st.image('assets/images/study_hrs_avg_max.png')

st.header('Comparison of the effect of drinking and study hours on average and modal GPA')
st.image('assets/images/study_to_drinks.png')

st.header('K Nearest Neighbour Regression model accuracy visualisation')
st.image('assets/images/knnreg.png')
with st.expander('KNN Regression accuracy data'):
    st.write(f'Mean Squared Error: {round(44.94231051440329, 2)}')
    st.write(f'R-squared: {round(0.10558104972582494, 2)}')