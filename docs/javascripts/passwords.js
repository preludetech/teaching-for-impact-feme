const password = "teaching";

const userInput = prompt("Enter password:");

if (userInput !== password) {
  document.body.innerHTML = "<h1>Access denied</h1>";
}