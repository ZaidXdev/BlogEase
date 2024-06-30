// script.js
// Get the button
let scrollToTopBtn = document.getElementById("scrollToTopBtn");

// Show the button when scrolling down 20px from the top of the document
window.onscroll = function() { scrollFunction(); };

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        scrollToTopBtn.classList.add("show");
    } else {
        scrollToTopBtn.classList.remove("show");
    }
}

// When the user clicks on the button, scroll to the top of the document smoothly using logarithmic decrement
scrollToTopBtn.addEventListener("click", function() {
    let start = window.scrollY;
    let startTime = null;

    function scrollStep(timestamp) {
        if (!startTime) startTime = timestamp;
        let progress = timestamp - startTime;
        let remaining = start - (start * Math.log(progress + 10) / Math.log(start + 10));
        window.scrollTo(0, remaining);

        if (remaining > 0) {
            window.requestAnimationFrame(scrollStep);
        } else {
            window.scrollTo(0, 0); // Ensure it reaches exactly the top
        }
    }

    window.requestAnimationFrame(scrollStep);
});
