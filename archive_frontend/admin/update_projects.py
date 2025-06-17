import json
import os
from datetime import datetime
from typing import Dict, List, Optional

class ProjectManager:
    def __init__(self, data_file: str, template_file: str, output_file: str):
        self.data_file = data_file
        self.template_file = template_file
        self.output_file = output_file
        self.projects_data = self._load_data()

    def _load_data(self) -> Dict:
        """Load projects data from JSON file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                return json.load(f)
        return {"projects": []}

    def _save_data(self):
        """Save projects data to JSON file."""
        with open(self.data_file, 'w') as f:
            json.dump(self.projects_data, f, indent=4)

    def add_project(self, 
                   title: str,
                   category: str,
                   technologies: List[str],
                   date_start: str,
                   date_end: str = "present",
                   description: str = "",
                   challenges: List[str] = None,
                   solutions: List[str] = None,
                   outcomes: List[str] = None,
                   github_link: str = "",
                   live_link: str = ""):
        """
        Add a new project to the data.
        
        Args:
            title: Project title
            category: One of "healthcare-it", "clinical-innovation", "process-improvement", "research"
            technologies: List of technologies used
            date_start: Start date in YYYY-MM format
            date_end: End date in YYYY-MM format or "present"
            description: Project description
            challenges: List of challenges faced
            solutions: List of solutions implemented
            outcomes: List of project outcomes/impacts
            github_link: Link to GitHub repository
            live_link: Link to live project
        """
        # Validate category
        valid_categories = ["healthcare-it", "clinical-innovation", "process-improvement", "research"]
        if category not in valid_categories:
            raise ValueError(f"Category must be one of: {', '.join(valid_categories)}")

        # Format dates for display
        date_start_obj = datetime.strptime(date_start, "%Y-%m")
        date_start_display = date_start_obj.strftime("%B %Y")
        
        if date_end.lower() == "present":
            date_end_display = "Present"
        else:
            date_end_obj = datetime.strptime(date_end, "%Y-%m")
            date_end_display = date_end_obj.strftime("%B %Y")

        dates_display = f"{date_start_display} - {date_end_display}"

        # Create new project entry
        new_project = {
            "title": title,
            "category": category,
            "technologies": technologies,
            "date_start": date_start,
            "date_end": date_end,
            "dates_display": dates_display,
            "description": description,
            "challenges": challenges or [],
            "solutions": solutions or [],
            "outcomes": outcomes or [],
            "github_link": github_link,
            "live_link": live_link
        }

        # Add to projects list and sort by date
        self.projects_data["projects"].append(new_project)
        self.projects_data["projects"].sort(
            key=lambda x: (x["date_start"], x["date_end"]),
            reverse=True
        )
        self._save_data()

    def remove_project(self, title: str) -> bool:
        """Remove a project by title."""
        initial_length = len(self.projects_data["projects"])
        self.projects_data["projects"] = [
            project for project in self.projects_data["projects"]
            if not (project["title"] == title)
        ]
        if len(self.projects_data["projects"]) < initial_length:
            self._save_data()
            return True
        return False

    def update_project(self, title: str, updates: Dict) -> bool:
        """Update an existing project."""
        for project in self.projects_data["projects"]:
            if project["title"] == title:
                project.update(updates)
                self._save_data()
                return True
        return False

    def generate_html(self) -> str:
        """Generate HTML for all projects."""
        html_parts = []
        for project in self.projects_data["projects"]:
            challenges_html = "\n".join(
                f'<li>{item}</li>' for item in project["challenges"]
            )
            solutions_html = "\n".join(
                f'<li>{item}</li>' for item in project["solutions"]
            )
            outcomes_html = "\n".join(
                f'<li>{item}</li>' for item in project["outcomes"]
            )
            technologies_html = ", ".join(project["technologies"])
            
            links_html = ""
            if project["github_link"]:
                links_html += f'<a href="{project["github_link"]}" target="_blank" class="project-link github">GitHub</a>'
            if project["live_link"]:
                links_html += f'<a href="{project["live_link"]}" target="_blank" class="project-link live">Live Demo</a>'
            
            project_html = f'''
                <div class="project-item" data-category="{project['category']}" data-date="{project['date_start']}">
                    <div class="project-header">
                        <h3 class="project-title">{project['title']}</h3>
                        <div class="project-meta">
                            <span class="dates">{project['dates_display']}</span>
                            <span class="technologies">{technologies_html}</span>
                        </div>
                        <div class="project-links">{links_html}</div>
                    </div>
                    <div class="project-content">
                        <div class="project-description">{project['description']}</div>
                        <div class="project-details">
                            <div class="challenges">
                                <h4>Challenges</h4>
                                <ul>{challenges_html}</ul>
                            </div>
                            <div class="solutions">
                                <h4>Solutions</h4>
                                <ul>{solutions_html}</ul>
                            </div>
                            <div class="outcomes">
                                <h4>Outcomes</h4>
                                <ul>{outcomes_html}</ul>
                            </div>
                        </div>
                    </div>
                </div>
            '''
            html_parts.append(project_html)

        return "\n".join(html_parts)

    def update_html_file(self):
        """Update the HTML file with generated project content."""
        if not os.path.exists(self.template_file):
            raise FileNotFoundError(f"Template file not found: {self.template_file}")

        with open(self.template_file, 'r') as f:
            template_content = f.read()

        # Generate projects HTML
        projects_html = self.generate_html()

        # Replace placeholder in template with generated content
        updated_content = template_content.replace(
            "<!-- Project items will be added here -->",
            projects_html
        )

        with open(self.output_file, 'w') as f:
            f.write(updated_content)

    def interactive_add_project(self):
        """Interactive command-line interface to add a project."""
        print("\n=== Add New Project ===")
        
        # Get project details
        title = input("Project Title: ")
        print("\nCategories: healthcare-it, clinical-innovation, process-improvement, research")
        category = input("Category: ").lower()
        
        print("\nTechnologies (comma-separated):")
        technologies = [tech.strip() for tech in input().split(",")]
        
        date_start = input("Start Date (YYYY-MM): ")
        date_end = input("End Date (YYYY-MM or 'present'): ")
        
        print("\nProject Description (press Enter twice when done):")
        description = []
        while True:
            line = input()
            if line:
                description.append(line)
            else:
                break
        description = " ".join(description)
        
        print("\nChallenges (one per line, press Enter twice when done):")
        challenges = []
        while True:
            line = input()
            if line:
                challenges.append(line)
            else:
                break
        
        print("\nSolutions (one per line, press Enter twice when done):")
        solutions = []
        while True:
            line = input()
            if line:
                solutions.append(line)
            else:
                break
        
        print("\nOutcomes (one per line, press Enter twice when done):")
        outcomes = []
        while True:
            line = input()
            if line:
                outcomes.append(line)
            else:
                break
        
        github_link = input("\nGitHub Link (optional): ")
        live_link = input("Live Demo Link (optional): ")

        # Add the project
        try:
            self.add_project(
                title=title,
                category=category,
                technologies=technologies,
                date_start=date_start,
                date_end=date_end,
                description=description,
                challenges=challenges,
                solutions=solutions,
                outcomes=outcomes,
                github_link=github_link,
                live_link=live_link
            )
            print("\nProject added successfully!")
        except Exception as e:
            print(f"\nError adding project: {str(e)}")

def main():
    manager = ProjectManager(
        data_file="frontend/data/projects.json",
        template_file="frontend/index_template.html",
        output_file="frontend/index.html"
    )
    
    while True:
        print("\n=== Project Management System ===")
        print("1. Add New Project")
        print("2. Remove Project")
        print("3. Update Project")
        print("4. Generate HTML")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == "1":
            manager.interactive_add_project()
        elif choice == "2":
            title = input("Project Title: ")
            if manager.remove_project(title):
                print("Project removed successfully!")
            else:
                print("Project not found!")
        elif choice == "3":
            print("Feature coming soon...")
        elif choice == "4":
            manager.update_html_file()
            print("HTML generated successfully!")
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
