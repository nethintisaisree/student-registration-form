import streamlit as st

# Application title
st.title("Student Registration Form")

# Student details
name = st.text_input("Name of the student")
roll = st.text_input("Roll Number of the student")

age = st.slider("Select Age", 15, 30, 19)

course = st.text_input("Course")
phone = st.text_input("Phone Number")

address = st.text_area("Address")

# Gender selection
gender = st.radio("Gender", ["Female", "Male"])

# Country selection
country = st.selectbox(
    "Country",
    ["INDIA", "USA", "UK", "CANADA", "AUSTRALIA"]
)

# Agreement checkbox
agree = st.checkbox("I Agree")

# Submit button
if st.button("Submit"):
    if name and roll and course and phone and address and agree:
        st.success("Registration Successful!")

        st.write("Student Name:", name)
        st.write("Roll Number:", roll)
        st.write("Age:", age)
        st.write("Course:", course)
        st.write("Phone Number:", phone)
        st.write("Address:", address)
        st.write("Gender:", gender)
        st.write("Country:", country)
    else:
        st.error("Please fill all details and agree.")
