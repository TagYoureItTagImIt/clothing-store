document.addEventListener('DOMContentLoaded', () => {

    // --- Hero Animation on Load ---
    const heroContent = document.querySelector('.hero-content.animate-on-load');
    if (heroContent) {
        // Use a slight delay for a better perceived effect
        setTimeout(() => {
            heroContent.classList.add('visible');
        }, 100); // 100ms delay
    }

    // --- Scroll Animations (Intersection Observer) ---
    const scrollElements = document.querySelectorAll('.animate-on-scroll');

    if ("IntersectionObserver" in window) { // Check if browser supports it
        let observer = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                // When element enters viewport
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-visible');
                    // Optional: Stop observing once it's visible (animation only happens once)
                    observer.unobserve(entry.target);
                }
                // Optional: If you want elements to fade out when scrolled out of view
                // else {
                //     entry.target.classList.remove('is-visible');
                // }
            });
        }, {
            root: null, // relative to document viewport
            threshold: 0.1 // trigger when 10% of the element is visible
            // rootMargin: "0px 0px -50px 0px" // Optional: Adjust the "bounding box"
        });

        scrollElements.forEach(el => {
            observer.observe(el);
        });

    } else {
        // Fallback for older browsers: just make everything visible immediately
        console.log("IntersectionObserver not supported, showing all elements.");
        scrollElements.forEach(el => {
            el.classList.add('is-visible');
        });
    }

});