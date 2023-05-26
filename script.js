document.addEventListener("DOMContentLoaded", function() {
    var form = document.querySelector("form");
    var placeholderImage = document.getElementById("workout-image");
    var table = document.getElementById("workout-table");

    form.addEventListener("submit", function(event) {
        event.preventDefault(); // Prevent form submission

        // Hide the placeholder image
        placeholderImage.style.display = "none";

        // Show the table
        table.style.display = "table";
    });
});
