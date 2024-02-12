// Sample data for previously asked questions
const previousQuestions = [
    "How to lower blood pressure?",
    "What are the symptoms of COVID-19?",
    "Is it safe to eat raw eggs?"
];

// Function to initialize the previously asked questions
function initPreviousQuestions() {
    const previousQuestionsList = document.getElementById("previous-questions");
    previousQuestions.forEach(question => {
        const li = document.createElement("li");
        li.textContent = question;
        li.onclick = () => {
            document.getElementById("user-question").value = question;
        };
        previousQuestionsList.appendChild(li);
    });
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
    // Placeholder function to process the question and return result
    const result = processQuestion(userQuestion);
    // Display the result
    resultTextArea.value = result;
}

// Placeholder function to process the question and return result
function processQuestion(question) {
    // Placeholder logic, replace with actual implementation
    return "This is a dummy response. Please replace it with the actual result of processing the user's question.";
}

// Initialize the previously asked questions when the page loads
window.onload = () => {
    initPreviousQuestions();
};

// Submit question when submit button is clicked
document.getElementById("submit-btn").addEventListener("click", submitQuestion);
