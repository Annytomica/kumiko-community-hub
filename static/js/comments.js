const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/** The following js functions were taken from the Code Institute Blog walkthrough
 * project with only minor modifications to suit this present project
*/

/**
* Enables edit functionality for the provided edit buttons.
* 
* Attaches a click event listener to each button in the `editButtons` list, 
* enabling the following behavior:
* - Retrieves the ID of the selected comment from the button's `data-comment_id` attribute.
* - Extracts the existing content of the specified comment for editing.
* - Prefills the `commentText` input/textarea with the extracted content.
* - Updates the submit button label to "Update" to indicate an edit action.
* - Adjusts the form's action URL to point to the appropriate edit endpoint (`edit_comment/{commentId}`).
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("data-comment_id");
    let commentContent = document.getElementById(`comment${commentId}`).innerText;
    commentText.value = commentContent;
    submitButton.innerText = "Update";
    commentForm.setAttribute("action", `edit_comment/${commentId}`);
  });
}


/**
 * Enables the delete functionality for comment delete buttons.
 * 
 * Attaches a click event listener to each button in the `deleteButtons` list, 
 * providing the following behavior:
 * - Retrieves the ID of the selected comment from the button's `data-comment_id` attribute.
 * - Updates the `deleteConfirm` link's href to target the appropriate delete endpoint (`delete_comment/{commentId}`).
 * - Triggers the display of a confirmation modal (`deleteModal`) to ask the user to confirm the deletion.
 */
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let commentId = e.target.getAttribute("data-comment_id");
      deleteConfirm.href = `delete_comment/${commentId}`;
      deleteModal.show();
    });
  }