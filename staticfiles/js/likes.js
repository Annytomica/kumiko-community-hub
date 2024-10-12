document.addEventListener("DOMContentLoaded", function() {
    const likeButton = document.getElementById("likeButton");
    const likeCheckbox = document.querySelector("input[name='like']");
    const likeForm = document.getElementById("likeForm");

    likeButton.addEventListener("click", function() {
        // Toggle the like state
        likeCheckbox.checked = !likeCheckbox.checked;

        // Change button appearance based on like state
        if (likeCheckbox.checked) {
            likeButton.innerHTML = '<i class="fa-solid fa-heart"></i>';
        } else {
            likeButton.innerHTML = '<i class="far fa-heart"></i>';
        }

        // Submit the form to save the new like status
        likeForm.submit();
    });
});