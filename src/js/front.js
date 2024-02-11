const signInBtn = document.getElementById("signIn");
const signUpBtn = document.getElementById("signUp");
const fistForm = document.getElementById("form1");
const secondForm = document.getElementById("form2");
const container = document.querySelector(".container");

// Function to clear the form fields
function clearFormFields(form) {
    const inputs = form.querySelectorAll('input');
    inputs.forEach(input => {
        input.value = '';
    });
}

signInBtn.addEventListener("click", () => {
    container.classList.remove("right-panel-active");
});

signUpBtn.addEventListener("click", () => {
    container.classList.add("right-panel-active");
});

// Add event listener to the first form for submission
fistForm.addEventListener("submit", (e) => {
    e.preventDefault(); // Prevent default form submission
    clearFormFields(fistForm); // Clear form fields after submission
});

// Add event listener to the second form for submission
secondForm.addEventListener("submit", (e) => {
    e.preventDefault(); // Prevent default form submission
    clearFormFields(secondForm); // Clear form fields after submission
});
