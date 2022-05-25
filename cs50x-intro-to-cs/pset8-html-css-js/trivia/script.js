// Multiple questions HTML elements as objects
const firstChoice = document.querySelector("#choice1");
const secondChoice = document.querySelector("#choice2");
const thirdChoice = document.querySelector("#choice3");
const fourthChoice = document.querySelector("#choice4");
const fifthChoice = document.querySelector("#choice5");
const btnsArray = [
  firstChoice,
  secondChoice,
  thirdChoice,
  fourthChoice,
  fifthChoice,
];
const correct = fifthChoice;
const multipleLabel = document.querySelector(".multiple-result-label");

// Function that changed a button color when clicked on
// If a user clicks on a button with an incorrect answer, the button should turn red and text should appear beneath the question that says “Incorrect”.
// If a user clicks on a button with the correct answer, the button should turn green and text should appear beneath the question that says “Correct!”.
function changeColor(btn) {
  if (btn === correct) {
    btn.style.cssText = "background-color: lightgreen";
    multipleLabel.textContent = "Correct!";
    multipleLabel.removeAttribute("hidden");
    revertAll(btn);
  } else {
    btn.style.cssText = "background-color: red";
    multipleLabel.textContent = "Incorrect";
    multipleLabel.removeAttribute("hidden");
    revertAll(btn);
  }
}

function revertAll(btn) {
  for (let button of btnsArray) {
    if (button != btn) {
      button.style.cssText = "background-color: #d9edff";
    }
  }
}

// Generating event listeners to change the color of clicked button
firstChoice.addEventListener("click", function () {
  changeColor(firstChoice);
});

secondChoice.addEventListener("click", function () {
  changeColor(secondChoice);
});

thirdChoice.addEventListener("click", function () {
  changeColor(thirdChoice);
});

fourthChoice.addEventListener("click", function () {
  changeColor(fourthChoice);
});

fifthChoice.addEventListener("click", function () {
  changeColor(fifthChoice);
});

// Free answer html elements as objects
const correctFreeAnswer = "switzerland";
const freeAnswer = document.querySelector("#answer");
const chkAnswerBtn = document.querySelector(".free");
const freeLabel = document.querySelector(".free-result-label");

// If the user types an incorrect answer and presses the confirmation button, the text field should turn red and text should appear
// beneath the question that says “Incorrect”.
// If the user types the correct answer and presses the confirmation button, the input field should turn green and text
// should appear beneath the question that says “Correct!”.
chkAnswerBtn.addEventListener("click", function () {
  let ans = freeAnswer.value.toLowerCase();
  if (ans === correctFreeAnswer) {
    freeAnswer.style.cssText = "background-color: lightgreen";
    freeLabel.removeAttribute("hidden");
    freeLabel.textContent = "Correct!";
  } else {
    freeAnswer.style.cssText = "background-color: red";
    freeLabel.removeAttribute("hidden");
    freeLabel.textContent = "Incorrect";
  }
});
