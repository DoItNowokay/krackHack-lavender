# from google import generativeai as genai
# from dotenv import load_dotenv
# import os
# import sys
# load_dotenv()

# genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# def get_gemini_response(prompt,query):
#     model=genai.GenerativeModel('gemini-pro')
#     response=model.generate_content([prompt,query])
#     return response.text

# prompt="""
# YOU ARE AN EXPERT HEALTH ADVISOR WHO HAS ALL THE KNOWLEDGE IN MEDICAL FIELD.
# you need to give answer in bullet points preferably.
# you have a strict word limit of 100 words, if word limit not mentioned ahead
# help me in this.
# """

# def generate_outpur(question):
#     return get_gemini_response(prompt,question)

# Import the required libraries
from flask import Flask, request, jsonify

# Your existing Python code for generate_output function
from google import generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

prompt = """
YOU ARE AN EXPERT HEALTH ADVISOR WHO HAS ALL THE KNOWLEDGE IN MEDICAL FIELD.
you need to give answer in bullet points preferably.
you have a strict word limit of 100 words, if word limit not mentioned ahead
help me in this.
"""

def get_gemini_response(prompt, query):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt, query])
    return response.text

def generate_output(question):
    return get_gemini_response(prompt, question)

# Create a Flask app instance
app = Flask(__name__)

# Define a route to handle the AJAX request
@app.route('/process_question', methods=['POST'])
def process_question():
    # Get the question from the AJAX request
    question = request.form['question']
    # Call the generate_output function
    response = generate_output(question)
    # Return the response as JSON
    return jsonify(response=response)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)

