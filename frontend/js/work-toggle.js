document.addEventListener('DOMContentLoaded', function() {
    const categorizedView = document.getElementById('view-categorized');
    const chronologicalView = document.getElementById('view-chronological');
    const timelineItems = document.querySelectorAll('.timeline-item');

    function updateView() {
        if (chronologicalView.checked) {
            // Show all items in chronological order
            timelineItems.forEach(item => {
                item.style.display = 'block';
            });
            // Hide category headers
            document.querySelectorAll('.work-category h3').forEach(header => {
                header.style.display = 'none';
            });
        } else {
            // Show items in their categories
            document.querySelectorAll('.work-category h3').forEach(header => {
                header.style.display = 'block';
            });
            timelineItems.forEach(item => {
                const category = item.getAttribute('data-category');
                item.style.display = item.closest(`.work-category[data-category="${category}"]`) ? 'block' : 'none';
            });
        }
    }

    categorizedView.addEventListener('change', updateView);
    chronologicalView.addEventListener('change', updateView);
});
