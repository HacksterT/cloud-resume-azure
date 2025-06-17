// Resume navigation and page-specific functionality

class ResumeManager {
    constructor() {
        this.init(); // Initialize navigation functionality
    }

    async init() {
        try {
            this.setupEventListeners(); // Set up navigation active-state logic
        } catch (error) {
            console.error('Error initializing resume:', error);
        }
    }

    setupEventListeners() {
        // Handle navigation active state
        const navLinks = document.querySelectorAll('.nav-menu a');
        const sections = document.querySelectorAll('.section');

        const updateActiveNavLink = () => {
            const fromTop = window.scrollY + 100;

            sections.forEach(section => {
                const link = document.querySelector(`.nav-menu a[href="#${section.id}"]`);
                if (!link) return;

                const { top, bottom } = section.getBoundingClientRect();
                const sectionTop = top + window.pageYOffset;
                const sectionBottom = bottom + window.pageYOffset;

                if (fromTop >= sectionTop && fromTop <= sectionBottom) {
                    link.classList.add('active');
                } else {
                    link.classList.remove('active');
                }
            });
        };

        // Update active state on scroll
        window.addEventListener('scroll', updateActiveNavLink);
        updateActiveNavLink(); // Initial check to set active state
    }
}

// Initialize the ResumeManager when the DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new ResumeManager();
});
