const signInBtn = document.getElementById("signIn");
const signUpBtn = document.getElementById("signUp");
const fistForm = document.getElementById("form1");
const secondForm = document.getElementById("form2");
const container = document.querySelector(".container");

// Function to handle form submission
document
    .getElementById("form1")
    .addEventListener("submit", function (event) {
        console.log("Form submission intercepted");
        event.preventDefault(); // Prevent default form submission
        console.log(this);
        // Get form data
        const formData = new FormData(this);
        console.log(formData);

        // Send form data to Flask server
        fetch("http://127.0.0.1:5000/donarData", {
            method: "POST",
            body: formData,
        })
            .then((response) => {
                if (!response.ok) {
                    throw new Error("Network response was not ok");
                }
                return response.text();
            })
            .then((data) => {
                console.log(data); // Log response from server
                alert("Form submitted successfully!");
                // You can redirect to another page or perform any other actions upon successful submission
            })
            .catch((error) => {
                console.error(
                    "There was a problem with your fetch operation:",
                    error
                );
                alert("Form submission failed. Please try again.");
            });
    });
document
    .getElementById("form2")
    .addEventListener("submit", function (event) {
        console.log("Form submission intercepted");
        event.preventDefault(); // Prevent default form submission
        console.log(this);
        // Get form data
        const formData = new FormData(this);
        console.log(formData);

        // Send form data to Flask server
        fetch("http://127.0.0.1:5000/receiverData", {
            method: "POST",
            body: formData,
        })
            .then((response) => {
                if (!response.ok) {
                    throw new Error("Network response was not ok");
                }
                return response.text();
            })
            .then((data) => {
                console.log(data); // Log response from server
                alert("Form submitted successfully!");
                // You can redirect to another page or perform any other actions upon successful submission
            })
            .catch((error) => {
                console.error(
                    "There was a problem with your fetch operation:",
                    error
                );
                alert("Form submission failed. Please try again.");
            });
    });

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

