from google import generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def get_gemini_response(prompt,query):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt,query])
    return response.text

prompt="""
YOU ARE AN EXPERT HEALTH ADVISOR WHO HAS ALL THE KNOWLEDGE IN MEDICAL FIELD.
you need to give answer in bullet points preferably.
you have a strict word limit of 100 words, if word limit not mentioned ahead
help me in this.
"""

def generate_outpur(question):
    return get_gemini_response(prompt,question)
