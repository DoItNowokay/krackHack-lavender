// Function to initialize the previously asked questions

function initPreviousQuestions() {
    const previousQuestions = localStorage.getItem('previousQuestions');
    if (previousQuestions) {
        const previousQuestionsList = document.getElementById("previous-questions");
        previousQuestions.split('\n').forEach(question => {
            const li = document.createElement("li");
            li.textContent = question;
            
            // Add delete button
            const deleteButton = document.createElement("button");
            deleteButton.textContent = "Delete";
            deleteButton.onclick = () => {
                deleteQuestion(question);
                // Remove the deleted question from the list
                previousQuestionsList.removeChild(li);
            };
            
            // Add the question and delete button to the list item
            li.appendChild(deleteButton);
            previousQuestionsList.appendChild(li);
        });
    }
}

// Function to save a question to localStorage
function saveQuestion(question) {
    let previousQuestions = localStorage.getItem('previousQuestions');
    if (!previousQuestions) {
        previousQuestions = '';
    }
    previousQuestions += question + '\n';
    localStorage.setItem('previousQuestions', previousQuestions);
}

// Function to submit a question
function submitQuestion() {
    const userQuestion = document.getElementById("user-question").value;
    const resultTextArea = document.getElementById("result");
    // Check if input is empty
    if (!userQuestion.trim()) {
        resultTextArea.value = "NO INPUT GIVEN";
        return;
    }
    // Save the question
    saveQuestion(userQuestion);
    // Placeholder function to process the question and return result
    const result = processQuestion(userQuestion);
    // Display the result
    resultTextArea.value = result;
}

// Placeholder function to process the question and return result
// Function to process the question and return result
// Function to process the question and return result
function processQuestion(question) {
    // Create a new FormData object
    const formData = new FormData();
    // Append the question to the FormData object
    formData.append('question', question);

    // Make a fetch request to the server-side endpoint
    fetch('/process_question', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        // Check if the response is successful
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        // Parse the JSON response
        return response.json();
    })
    .then(data => {
        // Handle the response data
        console.log(data.response);
        // Do something with the response, like display it on the page
    })
    .catch(error => {
        // Handle errors
        console.error('There was a problem with the fetch operation:', error);
    });
}



// Function to delete a question from localStorage
function deleteQuestion(questionToDelete) {
    let previousQuestions = localStorage.getItem('previousQuestions');
    if (!previousQuestions) {
        return;
    }
    // Remove the question from the list
    const questionArray = previousQuestions.split('\n');
    const index = questionArray.indexOf(questionToDelete);
    if (index !== -1) {
        questionArray.splice(index, 1);
        previousQuestions = questionArray.join('\n');
        localStorage.setItem('previousQuestions', previousQuestions);
    }
}

// Clear history when the clear history button is clicked
function clearHistory() {
    localStorage.removeItem('previousQuestions');
    // Clear the list of previous questions displayed on the frontend
    document.getElementById("previous-questions").innerHTML = "";
}

// Initialize the previously asked questions when the page loads
initPreviousQuestions();

// Submit question when submit button is clicked
document.getElementById("submit-btn").addEventListener("click", submitQuestion);
