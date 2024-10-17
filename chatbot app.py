%%writefile app.py
import openai
import streamlit as st

# Set your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with your actual API key

# Function to get responses from OpenAI's GPT-3 or GPT-4
def get_response(user_input):
    try:
        # Create a prompt to provide answers about Islamic banking
        prompt = f"You are an expert in Islamic banking. A user asks: {user_input}\nProvide a comprehensive and easy-to-understand response about Islamic banking."

        # Get the response from the model
        response = openai.Completion.create(
            engine="text-davinci-003", # You can also use "gpt-3.5-turbo" or "gpt-4" if available
            prompt=prompt,
            max_tokens=150,
            temperature=0.7,
        )
        message = response.choices[0].text.strip()
        return message
    except Exception as e:
        return "There was an error processing your request. Please try again."

# Streamlit UI setup
st.title("Islamic Banking Chatbot")
st.write("Ask me anything about Islamic banking!")

# Get user input
user_input = st.text_input("Your question:")

# If user input is provided, get the response from the chatbot
if user_input:
    response = get_response(user_input)
    st.write("Chatbot Response:")
    st.write(response)

# Examples section to guide the user
st.write("### Examples:")
st.write("- What is Islamic banking?")
st.write("- Explain the concept of Murabaha.")
st.write("- What is the difference between Riba and profit?")
st.write("- How does Ijarah work in Islamic finance?")
