# streamlit
import streamlit as st

st.set_page_config(page_title="growth mindset project" )
st.title("Growth Mindset Challenge:Web App with Streamlit")
st.header("Welcome to Your Growth Journey !")
st.write("Embrace challenges, learn from mistakes, and unlock your full potential. This AI -powered app helps you build a growth mind set with reflection,challengesand achievements !")

# quotes section
st.header("Today's Growth Mindset Quote")
st.write(" Success is not final, failure is not fatal: it is the courage to continue that counts."+"Winston Chuchill")
st.header("What's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing:")

# condition 
if user_input:
    st.success(f"you re facing: {user_input}. Keep pushing forward towards your goal !")
else:
    st.warning("Tell us about your challenge to get started")    

 # reflexing 
    st.header("Reflect on Your Learning")
    reflection = st.text_area("Write your reflections here")

if reflection:
    st.success(f"Great Insight ! Your reflection:{reflection}")
else:
    st.info("Reflecting on past experience help you to grow ! Share your defficulties")    

 # acheivements
    st.header("Celebrate Your Wins !") 
    acheivement = st.text_input  ("Share somethingyou have recently accomplished:")

    if acheivement:
      st.success(f"Amazing You acheived: {acheivement}")  
    else:
      st.info("Big or small  , every acheivement counts ! Share one Now !")  

 # footer
      st.write("- - -")  
      st.write("Keep believing in yourself. Growth is a journey, not a destination !")  
      st.write("Created by Nida Siddiqui") 
