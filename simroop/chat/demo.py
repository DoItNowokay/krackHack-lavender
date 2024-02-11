import streamlit as st
import chatbot

def main():
    # Title and welcome message
    st.title("Health Chatbot")
    st.write("Welcome to the Health Chatbot! Feel free to ask any health-related questions.")

    # Input box for asking questions
    user_question = st.text_input("Ask your question here:")
    
    # Button to submit the question
    if st.button("Submit"):
        # Function to process user's question and return result
        if(user_question==''):
            st.text_area("Result:","NO INPUT GIVEN")
        else:
            save_question(user_question)
            result = process_question(user_question)
            # Display the result
            st.text_area("Result:", result,height=200)
    # Display column of all previously asked questions
    st.sidebar.title("Previously Asked Questions")
    # You can replace the example questions below with your own data
    previous_questions = load_questions()
    for question in previous_questions:
        st.sidebar.write(question)


def load_questions():
    # Read previously asked questions from file
    try:
        with open("simroop/chat/user_asked_questions.txt", "r") as file:
            previous_questions = file.readlines()
        # Return the list of questions, removing any newline characters
        return [question.strip() for question in previous_questions]
    except FileNotFoundError:
        # If the file doesn't exist yet, return an empty list
        return []
    
def save_question(question):
    # Save the question to a file
    with open("simroop/chat/user_asked_questions.txt", "a") as file:
        file.write(question + "\n")


def process_question(question):
    # Placeholder function to process the question and return result
    # You'll need to implement your own logic here based on your backend or API
    # For now, let's just return a dummy response
    return chatbot.generate_outpur(question)

if __name__ == "__main__":
    main()
