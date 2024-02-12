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
async function submitQuestion() {
    const userQuestion = document.getElementById("user-question").value;
    const resultTextArea = document.getElementById("result");
    // Check if input is empty
    if (!userQuestion.trim()) {
        resultTextArea.value = "NO INPUT GIVEN";
        return;
    }
    // Save the question
    saveQuestion(userQuestion);
    try {
        // Process the question and get the result
        const result = await processQuestion(userQuestion);
        // Display the result
        resultTextArea.value = result;
    } catch (error) {
        console.error("Error submitting question:", error);
        resultTextArea.value = error;
    }
}

// Function to process the question and return result
async function processQuestion(question) {
    const genAI = new GoogleGenerativeAI("AIzaSyAzrTxXGz0bx3KCxdQziTGhkUU7qRsEkdA");
    try {
        // For text-only input, use the gemini-pro model
        const model = genAI.getGenerativeModel({ model: "gemini-pro" });
        
        // Start a chat session with the model
        const chat = model.startChat({
            generationConfig: {
                maxOutputTokens: 100,
            },
        });
        
        // Send the question to the chat session
        const result = await chat.sendMessage(question);
        const response = await result.response;
        const text = await response.text();
        
        return text;
    } catch (error) {
        console.error("Error processing question:", error);
        return "Error processing question";
    }
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
