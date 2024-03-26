// Get the current date and time
let currentDateTime = new Date();

// Format the date and time as a string
let formattedDateTime = currentDateTime.toLocaleString();

// Display the formatted date and time in the HTML element with id "currentDateTime"
document.getElementById("currentDateTime").textContent = formattedDateTime;
