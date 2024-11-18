import json
import os
from datetime import datetime
from typing import Dict, List, Optional

class RoleManager:
    def __init__(self, data_file: str, template_file: str, output_file: str):
        self.data_file = data_file
        self.template_file = template_file
        self.output_file = output_file
        self.roles_data = self._load_data()

    def _load_data(self) -> Dict:
        """Load roles data from JSON file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                return json.load(f)
        return {"roles": []}

    def _save_data(self):
        """Save roles data to JSON file."""
        with open(self.data_file, 'w') as f:
            json.dump(self.roles_data, f, indent=4)

    def add_role(self, 
                 category: str,
                 title: str,
                 company: str,
                 location: str,
                 date_start: str,
                 date_end: str = "present",
                 company_description: str = "",
                 job_description: str = "",
                 accomplishments: List[str] = None):
        """
        Add a new role to the data.
        
        Args:
            category: One of "administrative", "clinical", "academic"
            title: Job title
            company: Company name
            location: Job location
            date_start: Start date in YYYY-MM format
            date_end: End date in YYYY-MM format or "present"
            company_description: Description of the company
            job_description: Description of the role
            accomplishments: List of accomplishments/responsibilities
        """
        # Validate category
        if category not in ["administrative", "clinical", "academic"]:
            raise ValueError("Category must be one of: administrative, clinical, academic")

        # Format dates for display
        date_start_obj = datetime.strptime(date_start, "%Y-%m")
        date_start_display = date_start_obj.strftime("%B %Y")
        
        if date_end.lower() == "present":
            date_end_display = "Present"
        else:
            date_end_obj = datetime.strptime(date_end, "%Y-%m")
            date_end_display = date_end_obj.strftime("%B %Y")

        dates_display = f"{date_start_display} - {date_end_display}"

        # Create new role entry
        new_role = {
            "category": category,
            "date_start": date_start,
            "date_end": date_end,
            "title": title,
            "company": company,
            "location": location,
            "dates_display": dates_display,
            "company_description": company_description,
            "job_description": job_description,
            "accomplishments": accomplishments or []
        }

        # Add to roles list and sort by date
        self.roles_data["roles"].append(new_role)
        self.roles_data["roles"].sort(
            key=lambda x: (x["date_start"], x["date_end"]),
            reverse=True
        )
        self._save_data()

    def remove_role(self, company: str, title: str) -> bool:
        """Remove a role by company and title."""
        initial_length = len(self.roles_data["roles"])
        self.roles_data["roles"] = [
            role for role in self.roles_data["roles"]
            if not (role["company"] == company and role["title"] == title)
        ]
        if len(self.roles_data["roles"]) < initial_length:
            self._save_data()
            return True
        return False

    def update_role(self, company: str, title: str, updates: Dict) -> bool:
        """Update an existing role."""
        for role in self.roles_data["roles"]:
            if role["company"] == company and role["title"] == title:
                role.update(updates)
                self._save_data()
                return True
        return False

    def generate_html(self) -> str:
        """Generate HTML for all roles."""
        html_parts = []
        for role in self.roles_data["roles"]:
            accomplishments_html = "\n".join(
                f'<li>{item}</li>' for item in role["accomplishments"]
            )
            
            role_html = f'''
                <div class="timeline-item" data-category="{role['category']}" data-date="{role['date_start']}">
                    <div class="role-title">{role['title']}</div>
                    <div class="company-name">{role['company']}</div>
                    <div class="role-meta">
                        <span class="dates">{role['dates_display']}</span>
                        <span class="location">{role['location']}</span>
                    </div>
                    <div class="company-description">
                        {role['company_description']}
                    </div>
                    <div class="job-description">
                        {role['job_description']}
                    </div>
                    <ul class="accomplishments">
                        {accomplishments_html}
                    </ul>
                </div>
            '''
            html_parts.append(role_html)

        return "\n".join(html_parts)

    def update_html_file(self):
        """Update the HTML file with generated role content."""
        if not os.path.exists(self.template_file):
            raise FileNotFoundError(f"Template file not found: {self.template_file}")

        with open(self.template_file, 'r') as f:
            template_content = f.read()

        # Generate roles HTML
        roles_html = self.generate_html()

        # Replace placeholder in template with generated content
        # You'll need to add appropriate placeholder comments in your HTML template
        updated_content = template_content.replace(
            "<!-- Timeline items will be added here -->",
            roles_html
        )

        with open(self.output_file, 'w') as f:
            f.write(updated_content)

# Example usage
if __name__ == "__main__":
    manager = RoleManager(
        data_file="data/roles.json",
        template_file="index_template.html",
        output_file="index.html"
    )

    # Example: Add a new role
    # manager.add_role(
    #     category="administrative",
    #     title="Chief Medical Information Officer",
    #     company="Healthcare Innovation Partners",
    #     location="Austin, Texas",
    #     date_start="2020-01",
    #     company_description="A leading healthcare technology consulting firm...",
    #     job_description="Led strategic initiatives...",
    #     accomplishments=[
    #         "Spearheaded the implementation...",
    #         "Developed and executed..."
    #     ]
    # )
