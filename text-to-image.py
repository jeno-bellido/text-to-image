import streamlit as st
import openai

# Set up OpenAI API credentials
openai.api_key = st.secrets["api_key"]


# Define function to generate image from text
def generate_image(prompt):
    response = openai.Image.create(
      prompt=prompt,
      n=1,
      size="1024x1024"
    )

    # Retrieve image URL from API response
    image_url = response['data'][0]['url']

    # Display image
    st.image(image_url, use_column_width=True)

# Set up Streamlit app
st.title("Text to Image")

# Get user input
text_input = st.text_input("Enter text:")

# Generate image when user clicks button
if st.button("Generate Image"):
    generate_image(text_input)
