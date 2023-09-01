import streamlit as st
import pandas as pd
import sklearn
import numpy as np
import pickle
pipe=pickle.load(open('pipe.pkl','rb'))
teams=['Australia','Pakistan',
      'India','New Zealand',
      'England','South Africa',
      'Bangladesh','Afghanistan',
      'Sri Lanka','Netherlands']
cities=['Mirpur',
 'London',
 'Colombo',
 'Sydney',
 'Abu Dhabi',
 'Rangiri',
 'Melbourne',
 'Centurion',
 'Adelaide',
 'Dubai',
 'Birmingham',
 'Perth',
 'Auckland',
 'Cardiff',
 'Pallekele',
 'Brisbane',
 'Wellington',
 'Johannesburg',
 'Hamilton',
 'Sharjah',
 'Chandigarh',
 'Cape Town',
 'Durban',
 'Southampton',
 'Nottingham',
 'Manchester',
 'Port Elizabeth',
 'Leeds',
 'Karachi',
 'Napier',
 'Christchurch',
 'Hambantota',
 'Hobart',
 'Chester-le-Street',
 'Nagpur',
 'Mumbai',
 'Lahore',
 'Mount Maunganui',
 'Chittagong',
 'Delhi',
 'Fatullah',
 'Dunedin',
 'Rajkot',
 'Jaipur',
 'Kolkata',
 'Nelson',
 'Ahmedabad',
 'Hyderabad',
 'Bristol',
 'Canberra',
 'Harare',
 'Kanpur',
 'Bloemfontein']
st.title('Projected Score Predicter')
col1,col2=st.columns(2)
with col1:
    batting_team=st.selectbox('Select the Batting Team',sorted(teams))
with col2:
    bowling_team=st.selectbox('Select the Bowling Team',sorted(teams))
city=st.selectbox('Select City',sorted(cities))
col3,col4,col5=st.columns(3)
with col3:
    current_score=st.number_input('Current Score')
with col4:
    overs_done=st.number_input('Overs Done(works for overs>10)')
with col5:
    wickets=st.number_input('Wickets Out')
last_ten=st.number_input('Runs Scored in Last 10 Overs')
if st.button('Predict Score'):
    balls_left=300-(overs_done*6)
    wickets_left=10-wickets
    crr=current_score/overs_done
    input_df=pd.DataFrame({
        'batting_team':[batting_team],'bowling_team':[bowling_team],
        'city':[city],'current_score':[current_score],
        'balls_left':[balls_left],'wickets_left':[wickets_left],
        'crr':[crr],'last_ten':[last_ten]
    })
    st.table(input_df)
    result=pipe.predict(input_df)
    st.header('Predicted Score :' + str(int(result[0])))

