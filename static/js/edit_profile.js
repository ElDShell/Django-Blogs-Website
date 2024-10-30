// Change event for the image input
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('profile_img').addEventListener('change', function() {
        const submitButton = document.getElementById('submit_img');
        if (submitButton) {
            console.log('Submit button found');
            submitButton.click();
        } else {
            console.error('Submit button not found');
        }
    });
});
