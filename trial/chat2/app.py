# Import the required libraries
from flask import Flask, request, jsonify
from chatbot import generate_output

# Create a Flask app instance
app = Flask(__name__)

# Define a route to handle the AJAX request
@app.route('/process_question', methods=['POST'])
def process_question():
    # Get the question from the AJAX request
    question = request.form['question']
    # Call the generate_output function from your chatbot.py file
    response = generate_output(question)
    # Return the response as JSON
    return jsonify(response=response)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
