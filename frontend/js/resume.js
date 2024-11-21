// Resume data loading and population
class ResumeManager {
    constructor() {
        this.init();
    }

    async init() {
        try {
            this.setupEventListeners();
        } catch (error) {
            console.error('Error initializing resume:', error);
        }
    }

    setupEventListeners() {
        // Navigation active state
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

        window.addEventListener('scroll', updateActiveNavLink);
        updateActiveNavLink();
    }
}

// Initialize the resume when the DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new ResumeManager();
});
