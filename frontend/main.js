window.addEventListener('DOMContentLoaded', (event) => {
    getVisitCount();
});

const functionApiUrl = 'https://resume-counter-function-sybert.azurewebsites.net/api/GetResumeCounter';

const getVisitCount = () => {
    fetch(functionApiUrl)
        .then(response => {
            if (!response.ok) {
                throw Error('Error fetching visitor count');
            }
            return response.json();
        })
        .then(response => {
            console.log("Website called function API.");
            const count = response.count;
            document.getElementById('visitor-count').innerText = count;
        })
        .catch(function(error) {
            console.log(error);
            document.getElementById('visitor-count').innerText = '?';
        });
}