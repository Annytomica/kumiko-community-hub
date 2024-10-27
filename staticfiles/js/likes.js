/** The following js function was developed with assitance from ChatGPT
 *  to help simplify the logic and improve functionality **/

document.addEventListener("DOMContentLoaded", function() {
    const likeButton = document.getElementById("likeButton");
    const likeCheckbox = document.querySelector("input[name='like']");
    const likeForm = document.getElementById("likeForm");

    /**
     * Sets up the like/unlike functionality for the article.
     * 
     * Attaches a click event listener to the `likeButton`, enabling the following behavior:
     * - Checks the current like status for the user on the specific article.
     * - Toggles the like state whenever the button is clicked.
     * - Updates the button's appearance to reflect the new like or unlike status.
     * - Submits the updated like state via the `likeForm` to update the `ArticleLike` model.
     */

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