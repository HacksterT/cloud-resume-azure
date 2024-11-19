// Resume data loading and population
class ResumeManager {
    constructor() {
        this.dataPath = 'data/';
        this.profileData = {
            "name": "Troy E. Sybert",
            "title": "Healthcare Leader & Data Scientist",
            "location": "Tennessee",
            "email": "troy.sybert@example.com",
            "summary": "Healthcare leader and data scientist with expertise in clinical excellence and technological innovation.",
            "social_media": [
                {
                    "platform": "LinkedIn",
                    "url": "https://www.linkedin.com/in/troy-sybert/",
                    "icon": "linkedin"
                },
                {
                    "platform": "GitHub",
                    "url": "https://github.com/troysybert",
                    "icon": "github"
                }
            ]
        };
        this.init();
    }

    async init() {
        try {
            await this.loadProfile();
            await this.loadPublications();
            await this.loadRoles();
            await this.loadCredentials();
            this.setupEventListeners();
        } catch (error) {
            console.error('Error initializing resume:', error);
        }
    }

    async fetchJSON(filename) {
        try {
            const response = await fetch(`${this.dataPath}${filename}`);
            if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
            return await response.json();
        } catch (error) {
            console.error(`Error loading ${filename}:`, error);
            return null;
        }
    }

    async loadProfile() {
        const data = this.profileData;
        if (!data) return;

        // Update profile information
        document.querySelector('.profile-name').textContent = data.name;
        document.querySelector('.profile-title').textContent = data.title;
        document.querySelector('.profile-location').textContent = data.location;
        document.querySelector('.profile-email').textContent = data.email;
        document.querySelector('#summary .section-content p').textContent = data.summary;

        // Update social media links
        const socialLinksContainer = document.querySelector('.social-links');
        socialLinksContainer.innerHTML = data.social_media
            .map(social => `
                <a href="${social.url}" target="_blank" class="social-link ${social.icon}">
                    <i class="fab fa-${social.icon}"></i>
                    ${social.platform}
                </a>
            `).join('');
    }

    async loadPublications() {
        const data = await this.fetchJSON('publications.json');
        if (!data) return;

        // Populate publications
        const publicationsList = document.querySelector('.publication-list');
        publicationsList.innerHTML = data.publications
            .map(pub => `
                <li>
                    <a href="${pub.url}" target="_blank">
                        ${pub.authors.join(', ')}. ${pub.title}. 
                        ${pub.journal} ${pub.year}${pub.volume ? `;${pub.volume}` : ''}
                        ${pub.issue ? `(${pub.issue})` : ''}.
                    </a>
                </li>
            `).join('');

        // Populate presentations
        const presentationsList = document.querySelector('.presentation-list');
        presentationsList.innerHTML = data.presentations
            .map(pres => `
                <li>
                    "${pres.title}"
                    <a href="${pres.video_url}" target="_blank">
                        ${pres.event}, ${pres.location}</a>.
                    ${pres.slides_url ? `<a href="${pres.slides_url}" class="resource-link pdf" target="_blank">PDF</a>` : ''}
                </li>
            `).join('');

        // Populate press mentions
        const pressList = document.querySelector('.press-list');
        pressList.innerHTML = data.press_mentions
            .map(press => `
                <li>
                    <a href="${press.url}" target="_blank">
                        ${press.title}. ${press.publication}. ${press.date}.
                    </a>
                </li>
            `).join('');
    }

    async loadRoles() {
        const data = await this.fetchJSON('roles.json');
        if (!data) return;

        const rolesContainer = document.querySelector('#work .timeline');
        rolesContainer.innerHTML = data.roles
            .map(role => `
                <div class="timeline-item">
                    <div class="timeline-content">
                        <div class="role-header">
                            <h3>${role.title}</h3>
                            <span class="company">${role.company}</span>
                            <span class="dates">${role.dates_display}</span>
                            <span class="location">${role.location}</span>
                        </div>
                        <p class="company-description">${role.company_description}</p>
                        <p class="job-description">${role.job_description}</p>
                        <ul class="accomplishments">
                            ${role.accomplishments.map(acc => `<li>${acc}</li>`).join('')}
                        </ul>
                    </div>
                </div>
            `).join('');
    }

    async loadCredentials() {
        const data = await this.fetchJSON('credentials.json');
        if (!data) return;

        // Populate credentials sections (education, licenses, certifications)
        Object.entries(data).forEach(([section, items]) => {
            const container = document.querySelector(`#credentials .${section}-section .credentials-grid`);
            if (!container) return;

            container.innerHTML = items
                .map(item => `
                    <div class="credential-card">
                        <div class="credential-title">${item.title}</div>
                        <div class="credential-subtitle">
                            ${item.url ? 
                                `<a href="${item.url}" target="_blank">${item.institution}</a>` : 
                                item.institution}
                        </div>
                        <div class="credential-date">${item.date}</div>
                        ${item.description ? `<div class="credential-description">${item.description}</div>` : ''}
                    </div>
                `).join('');
        });
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
