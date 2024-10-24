/** The following js function was developed with assitance from ChatGPT
 *  to help simplify the logic and improve functionality **/

document.addEventListener("DOMContentLoaded", function() {
    const likeButton = document.getElementById("likeButton");
    const likeCheckbox = document.querySelector("input[name='like']");
    const likeForm = document.getElementById("likeForm");

    /** Initialises article like/unlike functionality:
     * - retrieves like button status for user for the present article
     * - toggles the status upon user click
     * - changes button appearance to reflect new like status
     * - submits status change to likeForm for update of ArticleLike model
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