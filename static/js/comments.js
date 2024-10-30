function toggleDropdown(element) {
  const dropdown = element.nextElementSibling;
  dropdown.style.display = dropdown.style.display === "none" ? "block" : "none";
}

let commentIdToDelete = null;

function openModal(commentId) {
  commentIdToDelete = commentId; // Store the comment ID to delete
  var modal = document.getElementById("deleteModal");
  if (modal) {
      modal.style.display = "block"; // Show the modal
  }
}

function closeModal() {
  document.getElementById("deleteModal").style.display = "none"; // Hide the modal
}

function handleDeleteClick(commentId,deleteUrl,button) {
  closeDropdown(button); // Hide the dropdown
  openModal(commentId); // Show the modal
  // Update the form action URL dynamically
  var deleteForm = document.getElementById('deleteCommentForm');
  deleteForm.action = deleteUrl;  // Set the action URL for form submission
}

function closeDropdown(button) {
  const dropdown = button.closest('.dropdown-menu');
  if (dropdown) {
    dropdown.style.display = "none"; // Hide the dropdown
  }
}

// No need to manually update the href here, the form submission will handle it
document.getElementById("confirmDeleteButton").onclick = function() {
  // The form will be submitted via the delete button's form submission
  document.getElementById('deleteCommentForm').submit(); // Submit the form
}
