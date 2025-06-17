class VisitorCounter {
    constructor(apiUrl) {
        this.apiUrl = apiUrl; // Initialize the API URL
    }

    async getVisitorCount() {
        try {
            const response = await fetch(this.apiUrl);
            if (!response.ok) {
                throw new Error('Failed to fetch visitor count');
            }
            const data = await response.json();
            return data.count;
        } catch (error) {
            console.error('Error fetching visitor count:', error);
            return '?'; // Default display if there's an error
        }
    }

    async updateDisplay() {
        const count = await this.getVisitorCount();
        const countElement = document.getElementById('visitor-count');
        if (countElement) {
            countElement.innerText = count; // Update the counter in the DOM
        }
    }
}

// Initialize the counter when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    const counter = new VisitorCounter('https://resume-counter-function-sybert.azurewebsites.net/api/GetResumeCounter');
    counter.updateDisplay();
});
