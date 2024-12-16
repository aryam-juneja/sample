import streamlit as st

# Set the title of the app
st.title("Simple Streamlit App")

# Create a text input widget
user_input = st.text_input("Enter some text:")

# Create a button
if st.button("Submit"):
    # Display the input text when the button is clicked
    st.write("You entered:", user_input)
