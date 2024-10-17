import streamlit as st
import time
Easy = ['A', 'B', 'C', 'D', 'E']
Medium = ['125', '55', '97', '357', '102', '10' ]
Hard = ['2FE', 'X0k', '32bt', 'We1come']
st.title("Sequence memory game!")
button = st.button("RULES") 
if button == True:
    t=st.write("Starting game...")
    st.write("Rules:")
    st.write("1. Select difficulty to start the game.")
    st.write("2. You will be shown a sequence of numbers, letters or symbols for a short time, and you must recall the sequence in the correct order. With each round, the sequence length increases.")
    option = 0

sequence = Easy
easy_bt = st.button("EASY")
medium_bt = st.button("MEDIUM")
hard_bt = st.button("HARD")

if easy_bt == True:
    sequence = Easy
elif medium_bt == True:
    sequence = Medium
elif hard_bt == True:
    sequence = Hard
st.write(sequence)


inp = st.text_input("Enter your Answer here: ")
if inp ==  sequence:
    st.write("Correct :-)")
else:
    st.write("Incorrect :-(")