document.getElementById("img_input").addEventListener('change', function() {
    const submit_img = document.getElementById('img_submit');
    if (submit_img) {
        console.log("Image submitted");
        submit_img.click();  // This triggers the form submission
    } else {
        console.error("There is no submit image");
    }
});

function openModal(tagId) {
    document.getElementById('tag_id').value = tagId; // Set the tag ID in the hidden input
    document.getElementById('deleteModal').style.display = 'block'; // Show the modal
}
function closeModal() {
    document.getElementById('deleteModal').style.display = 'none'; // Hide the modal
}